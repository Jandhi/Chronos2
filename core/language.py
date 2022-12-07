from chronology.sound_change import SoundChange, sc
from core.word import Word
from orthography.sipa import SIPA

class Language:
    def __init__(self, name : str, short_form : str) -> None:
        self.name = name
        self.short_form = short_form

        self.parent : Language = None
        self.change_from_parent : LanguageChange = None
        self.children : list[Language] = []

    def derive(self, word : Word, depth = 0, verbose = False, tab_amount = 2):
        if isinstance(word, str):
            word = SIPA.word(word)

        word = word.copy()
        tab = ' ' * tab_amount
        
        if depth != 0:
            word = self.change_from_parent.apply(word, tab * depth, verbose)
        
        print(f'{tab * depth}{self.short_form}: {word}')

        for child in self.children:
            child.derive(word, depth + 1, verbose, tab_amount)

class LanguageChange:
    def __init__(self, parent : Language, child : Language, *steps) -> None:
        child.parent = parent
        parent.children.append(child)
        child.change_from_parent = self
        self.steps = []

        for step in steps:
            self.add_step(*step)
    
    def add_step(self, name, *sound_changes : SoundChange):
        self.steps.append((name, [sc(*contents) for contents in sound_changes]))
    
    def apply(self, word : Word, tab = '', verbose = False) -> Word:
        if isinstance(word, str):
            word = SIPA.word(word)

        word = word.copy()

        for (name, sound_changes) in self.steps:
            old_word = word

            for sc in sound_changes:
                sc : SoundChange
                new_word = sc.apply(word)
                

                word = new_word

            if old_word != word and verbose:
                print(f'{tab}{SIPA.transcribe(old_word)} -> {SIPA.transcribe(word)} [{name}]')
            
            old_word = word
        
        return word