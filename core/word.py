from phonology.sound import Sound
from chronology.category import Category
from core.exception import ChronosException

class Word:
    word_to_string = None

    def __init__(self, sounds : list[Sound]) -> None:
        self.sounds = sounds

    def __len__(self) -> int:
        return len(self.sounds)

    def __getitem__(self, index):
        return self.sounds[index]
    
    def subword(self, startIndex = 0, length = -1):
        if length == -1:
            length = len(self) - startIndex
        
        return Word(self.sounds[startIndex : startIndex + length])
    
    def __iter__(self):
        return self.sounds.__iter__()
    
    def __add__(self, other):
        if isinstance(other, Word):
            return Word(self.sounds + other.sounds)
        elif isinstance(other, Sound):
            new_sounds = self.sounds.copy()
            new_sounds.append(other)
            return Word(new_sounds)
        else:
            raise ChronosException('You cannot add this type to a word!')
    
    def copy(self):
        return Word([snd.copy() for snd in self.sounds])
    
    def mirror(self, other):
        self.sounds = other.sounds
    
    def __eq__(self, __o: object) -> bool:
        if len(__o.sounds) != len(self.sounds):
            return False
        
        for i in range(len(self.sounds)):
            if __o[i] != self[i]:
                return False
        
        return True
    
    def __repr__(self) -> str:
        return Word.word_to_string(self)


def make_word(*items):
    sounds = []

    for item in items:
        if isinstance(item, Sound):
            sounds.append(item)
        elif isinstance(item, Category):
            sounds.append(item.sound())
        else:
            raise ChronosException('Words can only be made of Sounds or Categories')
    
    return Word(sounds)