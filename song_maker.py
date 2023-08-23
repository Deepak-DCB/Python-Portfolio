
class Song:
    def __init__(self, name, primary_artist, bpm, chords):
        """
        Initializes class song
        """
        self.name = name
        self.artist = primary_artist
        self.bpm = bpm
        self.chords = chords
    
    def associated_artists(self, other_artists):
        """
        Appends other_artists to self.artist
        """
        self.artist = self.artist + ", " + other_artists
    
        
    def change_beat(self, increase, change):
        """
        Increases or decreases bpm
        """
        if increase is True:
            self.bpm = self.bpm + change
        elif increase is False:
            self.bpm = self.bpm - change
    
        
    def modulate(self, steps):
        """
        Modulates chords
        """

        #notes list extends/repeats after B so that modulating a b chord is possible or any chord that would exceed the range of list with a given steps value is possible
        notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        
        #chords reset at 6 steps, so to ensure that a user can enter any number of steps and not exceed notes list range, subtract 6 until under 6
        while steps > 6:
            steps = steps - 6


        #list of modulates chords
        mod_chords = []

        #converting steps into number of chords needed to go over, meaning a half step now equals 1 and a full step equals 2
        steps = float(steps) / .5
        steps = int(steps)


        for chord in self.chords:

            #parses through notes using index and range. Once note and chord match, modulated chord equals index position + number of half steps
            for i in range(0, len(notes), 1):
                if chord == notes[i]:
                    new = notes[i + steps]
                    mod_chords.append(new)
                    break


        #class chords now equal modulated chords
        self.chords = mod_chords



    def info(self):
        """
        Prints a message displaying the name of the song, the artist, bpm, and the chords used. 
        """
        print('Name: ', self.name)
        print('Artists: ', self.artist)
        print('BPM: ', self.bpm)
        print('Chords: ', self.chords)

  
  
#use_song
#Driver: Deepak Binkam
#Observer: Nicholas Urquhart
  from song import Song
def main():
    #testing song class
    chords = ['C', 'D', 'B', 'C#', 'A#']
    s1 = Song("A Song", "John Smith", 50, chords)
    s1.info()
    print("\n")
    s1.change_beat(True, 50)
    s1.modulate(9)
    s1.associated_artists("Another Artist")
    s1.info()

if __name__ == "__main__":
    main()