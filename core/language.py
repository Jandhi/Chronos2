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

    def derive(self, words : list[Word], depth = 0, verbose = False, tab_amount = 2):
        for i in range(len(words)):
            if isinstance(words[i], str):
                words[i] = SIPA.word(words[i])

        tab = ' ' * tab_amount
        
        if depth != 0:
            words = self.change_from_parent.apply(words, tab * depth, verbose)
        
        word_str = ''
        for word in words:
            word_str = f'{word_str} {word}'

        print(f'{tab * depth}{self.short_form}:{word_str}')

        for child in self.children:
            child.derive(words, depth + 1, verbose, tab_amount)

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
    
    def apply(self, words : list[Word], tab = '', verbose = False) -> Word:

        for i in range(len(words)):
            if isinstance(words[i], str):
                words[i] = SIPA.word(words[i])

        words = [word.copy() for word in words]

        for (name, sound_changes) in self.steps:
            changed = False
            old_words = [word.copy() for word in words]

            for i in range(len(words)):
                for sc in sound_changes:
                    sc : SoundChange
                    old_word = words[i].copy()
                    words[i] = sc.apply(words[i])

                    if any(not s1.is_match(s2) for (s1, s2) in zip(old_word.sounds, words[i].sounds)):
                        changed = True

            if changed and verbose:
                old_str = ''
                for word in old_words:
                    old_str = f'{old_str}{word} '
                
                new_str = ''
                for word in words:
                    new_str = f'{new_str}{word} '

                grey = '\033[38;5;8m'
                reset = '\033[0m'

                print(f'{grey}{tab}{old_str}-> {new_str}[{name}]{reset}')
        
        return words