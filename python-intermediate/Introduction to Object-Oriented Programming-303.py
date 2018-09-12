## 2. Creating a Class and an Instance ##

class MusicArtist():
    pass 
beyonce = MusicArtist()
ed_sheeran = MusicArtist()
kanye_west = MusicArtist()

## 3. Defining Variables within a Class ##

class MusicArtist(object):
    pass

ed_sheeran = MusicArtist()
beyonce = MusicArtist()

ed_sheeran.name = "Ed Sheeran" 
ed_sheeran.genre = "Pop" 
ed_sheeran.song = "Thinking out Loud" 

beyonce.name = "Beyonce" 
beyonce.genre = "R&B" 
beyonce.song = "Halo"  

print(ed_sheeran.name)
print(ed_sheeran.genre)
print(ed_sheeran.song) 

print(beyonce.name)
print(beyonce.genre)
print(beyonce.song)

## 4. Defining our attributes using the __init__() method ##

class MusicArtist():
    def __init__(self,name,genre,song):
        self.name = name
        self.genre = genre; 
        self.song = song
        
ed_sheeran = MusicArtist("Ed Sheeran", "Pop", "Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B", "Halo")

## 5. Accessing instance variables ##

class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

print(ed_sheeran.name + " is singing " + ed_sheeran.song + " tonight ")
print(beyonce.name + " is singing " + beyonce.song+ " tonight ")

## 6. Adding methods to our class ##

class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song

        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

print("{name} is singing {song} tonight".format(name = ed_sheeran.name, song = ed_sheeran.song))
print("{name} is singing {song} tonight".format(name = beyonce.name, song = beyonce.song))
class MusicArtist():
    def __init__(self, name, genre, song):
        self.name = name
        self.genre = genre
        self.song = song
    
    def sing(self):
        print("{name} will be singing {song} tonight".format(name = self.name, song = self.song))
        
ed_sheeran = MusicArtist("Ed Sheeran","Pop","Thinking out Loud")
beyonce = MusicArtist("Beyonce", "R&B","Halo")

ed_sheeran.sing()
beyonce.sing()