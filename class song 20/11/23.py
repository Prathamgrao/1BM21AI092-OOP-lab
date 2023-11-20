class song():
    lyrics=[]
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing(self):
        for i in lyrics:
            print(i)
lyrics=["happy happy","birthday","have a","gr8 day"]
s1=song(lyrics)
s1.sing()
