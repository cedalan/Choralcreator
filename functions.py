#Author: Christian Elias Anderssen Dalan
#Autumn 2022

import numpy as np

def chord_translator(input):
    """
    Function that takes a chord and translates it into the notes that makes up the chord.

    The following formats are supported (all chords are shown with C as the tonic):
    
    Minor chord - Cm
    Major chord - C
    7th chords - Cm7 and C7
    Major 7th chords - Cm(maj7) and Cmaj7
    Augmented chords - C+
    Diminished chords - Co
    Diminished 7th chords - Co7
    Half diminished chords - Cø
    Suspended chords - Csus2 or Csus4

    Parameters:
    -----------

    input:
    The input that will be translated. A chord will be input as a string, while notes will be input as a list of notes.

    Returns:
    output - Translated chord or notes.
    """

    notes_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notes_flat =  ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    chords = {
        "": [0, 4, 7],
        "m": [0, 3, 7],
        "m7": [0, 3, 7, 10],
        "7": [0, 4, 7, 10],
        "m(maj7)": [0, 3, 7, 11],
        "maj7": [0, 4, 7, 11],
        "+": [0, 4, 8],
        "o": [0, 3, 6],
        "o7": [0, 3, 6, 9],
        "ø": [0, 3, 6, 10],
        "sus2": [0, 2, 7],
        "sus4": [0, 5, 7]
    }

    if type(input) == str:
        output = []

        #Check if note is part of the "sharp" or "flat" side of the circle of fifths.
        if input[0] in notes_sharp:
            sharp = True
            notes = notes_sharp
        else:
            sharp = False
            notes = notes_flat
        output.append(input[0])

        #Translate chord name into relationships from root in half notes
        chord_notes = chords[input[1:]]
        chord_notes = chord_notes + notes.index(input[0])
        chord_notes = [((chord_notes[i] - 12) if (chord_notes[i] > 12) else chord_notes[i]) for i in range(len(chord_notes))]
        chord_notes = [notes[chord_notes[i]] for i in range(len(chord_notes))]

        return output 

    else:
        output = ""

        return output

def find_possible_voicings(chord):
    """
    Parameters:
    -----------
    chord:
    The chord we want to find voicings for. I. ex: Dm

    Returns:
    --------
    voicings - possible voicings of the chord
    """
    voicings = []
    return voicings

def check_consecutives(chord_voicing1, chord_voicing2):
    """
    Parameters:
    -----------
    chord_voicing1:
    The "starting chord" and how it is voiced.

    chord_voicing2:
    The following chord and how it is voiced.

    Returns:
    consecutives - True if there are consecutive fifths, octaves or unisons.
    """
    consecutives = False

    leaps = [c1 - c2 for c1, c2 in zip(chord_voicing1, chord_voicing2)]

    for i in range(len(leaps)):
        for j in range(j):
            if i != j:
                #If we are comparing two voices, check if leap the same distance:
                diff = np.abs(leaps[i] - leaps[j])
                if diff == 0:
                    #Since we start at soprano and compare downwards we have to use inverted intervals.
                    interval = chord_voicing1[i] - chord_voicing1[j]
                    if interval == 0 or interval == 7 or interval == 12 or interval == 19 or interval == 24:
                        consecutives = True
                
                #Check antiparalells:
                
    return consecutives

def check_voicing_distance(voicing):
    """
    Parameters:
    -----------
    voicing:
    The voicing of a chord.

    Returns:
    --------
    reasonable_distance - True if the distances between the different voices are okay, False if the distance between two voices
    are too high.
    """
    reasonable_distance = True 

    for i in range(3):
        if i < 2:
            if np.abs(voicing[i] - voicing[i+1]) > 12: #Octave between Soprano and Alto, and Alto and Tenor
                reasonable_distance = False
        else:
            if np.abs(voicing[i] - voicing[i+1]) > 19:#Octave + fifth between Tenor and Bas
                reasonable_distance = False

    return reasonable_distance

def check_voice_leaping(chord_voicing1, chord_voicing2):
    """
    You generally want to voice leaps to be small and simple to promote ease of singing. This function checks if the leaps
    between two chords are allowed. 

    Parameters:
    chord_voicing1:
    The "starting chord" and how it is voiced.

    chord_voicing2:
    The following chord and how it is voiced.

    Returns:
    --------
    reasonable_leaps - True if leaps between two notes (note: in the same voice) are under a tritone. The bass can move pretty freely.
    """
    resonable_leaps = True

    max_leap_SAT = 7

    max_leap_B = 12

    voice_number = 0
    for v1, v2 in zip(chord_voicing1, chord_voicing2):
        if voice_number < 3: #SAT voicing check
            if np.abs(v1 - v2) > max_leap_SAT and np.abs(v1 - v2) != 12: #Check for too large leaps
                reasonable_leaps = False

            if np.abs(v1 - v2) == 6: #Check for tritone leap
                reasonable_leaps = False

            voice_number += 1
        
        else: #Bass voicing check
            if np.abs(v1 - v2) > max_leap_B or np.abs(v1 - v2) == 6:
                reasonable_leaps = False

    return resonable_leaps

def check_voice_landslide(chord_voicing1, chord_voicing2):
    """
    Checks if all voices move in the same direction. This works by comparing each voice pair, and giving them a value
    based on if they move up or down. If a voice moves up it gains the value 1, if it moves down it gains the value 0, this means
    if the toal value is 4 (all voices up) or 0 (all voices down) we have a landslide.

    Parameters:
    -----------
    chord_voicing1:
    The "starting chord" and how it is voiced.

    chord_voicing2:
    The following chord and how it is voiced.

    Returns:
    --------
    voice_landslide - True if all voices move in the same direction, False if otherwise.
    """
    voice_landslide = False

    total_movement_value = 0

    for v1, v2 in zip(chord_voicing1, chord_voicing2):
        if v1 < v2:
            total_movement_value += 1
    
    if total_movement_value == 4 or total_movement_value == 0:
        voice_landslide = True

    return voice_landslide 