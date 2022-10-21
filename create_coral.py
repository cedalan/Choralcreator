import functions as fc
def create_choral(melody, progression, harmonic_function):
    """
    Parameters:
    -----------

    melody:
    The melody of the piece.

    progression:
    The chord progression of the piece.

    harmonic_function:
    The harmonic function of each chord in the progression. 

    Returns:
    --------
    """
    """
    Chord notes are identified by a number, depending on the intervals the different voices can sing. 
    The default for an amateur choir is:
    
    Soprano: b - f2
    Alto: f - c2
    Tenor: B - f1
    Bass: F - c1
    
    We default to identifying the lowest possible note for a bass as 0, and work our way chromatically from there.
    Ex: d2 will have the identity 33, since the distance from F to d2 is two octaves + M6, which is 24 + 9 semitones
    from F. 
    """
    
    #Soprano setup:
    soprano = melody
    soprano_max = 36
    soprano_min = 17
    
    #Alto setup:
    alto = []
    alto_max = 31
    alto_min = 12
    
    #Tenor setup:
    tenor = []
    tenor_max = 24
    tenor_min = 5
    
    #Bass setup:
    bass = []
    bass_max = 19
    bass_min = 0