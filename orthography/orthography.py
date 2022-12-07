from phonology.sound import Sound
from phonology.feature import Feature
from chronology.category import Category
from core.validate import validate_category, validate_sound
from core.word import Word
from core.exception import ChronosException

class Diacritic:
    def __init__(self, symbol : str, features : set[Feature], category : Category) -> None:
        if isinstance(features, Feature):
            features = set([features])
        
        self.symbol = symbol
        self.features = features
        self.category = validate_category(category)

class Letter:
    def __init__(self, symbol : str, sounds : list[Sound]) -> None:
        if isinstance(sounds, Category):
            sounds = [sounds.sound()]
        
        if isinstance(sounds, Sound):
            sounds = [sounds]
        
        self.symbol = symbol
        self.sounds = sounds

        for i in range(len(self.sounds)):
            self.sounds[i] = validate_sound(self.sounds[i])

class Orthography:
    def __init__(self, name, diacritics : list[Diacritic], letters : list[Letter]) -> None:
        self.name = name
        self.diacritics = diacritics
        self.letters = letters
    
    # Maximal Munch
    def transcribe(self, word : Word) -> str:
        word = word.copy()

        index = 0
        length = len(word)
        s = ''

        while True:
            added = False

            if index >= len(word):
                return s

            combining = ''

            if length == 1:
                for diacritic in self.diacritics:
                    # if the diacritic isn't relevant, continue
                    if not diacritic.category.is_match(word[index]):
                        continue

                    # if sound doesn't have the features the diacritic is used for, continue
                    if not all(ft in word[index] for ft in diacritic.features):
                        continue
                    
                    for ft in diacritic.features:
                        if ft.is_negative:
                            word[index].add(-ft)
                        else:
                            word[index].remove(ft)
                    
                    combining += diacritic.symbol

            for letter in self.letters:
                if len(letter.sounds) == length and all((letter.sounds[i].features == word[index + i].features for i in range(len(letter.sounds)))):
                    s += letter.symbol + combining
                    index = index + length
                    length = len(word) - index + 1 # +1 for length sub
                    added = True
                    break
            
            if not added and length == 1:
                raise ChronosException(f'Orthography {self.name} could not translate sound {word[index]}!')

            length -= 1

    def sound(self, input : str) -> Sound:
        word = self.word(input)

        if len(word) != 1:
            raise ChronosException(f'{input} doesn\'t create one sound!')

        return word[0]
        
    def word(self, input : str) -> Word:
        word = Word([])

        index = 0
        length = len(input)

        while True:
            added = False # tracker for infinite loops
        
            if index >= len(input):
                return word

            for letter in self.letters:
                if letter.symbol == input[index:index+length]:
                    sounds = [snd.copy() for snd in letter.sounds]

                    for snd in sounds:
                        word.sounds.append(snd)
                    
                    index = index + length
                    length = len(input) - index
                    added = True
                    break

            for diacritic in self.diacritics:
                if diacritic.symbol == input[index:index+length]:
                    for ft in diacritic.features:
                        word[-1].add(ft)
                    
                    index = index + length
                    length = len(input) - index
                    added = True
                    break
            
            if length == 0 and not added:
                raise ChronosException(f'Couldn\'t translate letter {input[index]}')

            if not added:
                length -= 1
    
def orth(name, diacritics, letters) -> Orthography:
    dlist = []
    llist = []

    for item in diacritics:
        symbol = item[0]
        features = item[1]
        category = None

        if len(item) == 3:
            category = item[2]
        
        dlist.append(Diacritic(symbol, features, category))
    
    for item in letters:
        llist.append(Letter(item[0], item[1]))
    
    return Orthography(name, dlist, llist)