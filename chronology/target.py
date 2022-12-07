from phonology.sound import Sound
from core.word import Word
from chronology.environment import A, MatcherInterface
from chronology.category import C, V, Category
from orthography.sipa import SIPA

class Target:
    def __init__(self, *items : MatcherInterface) -> None:
        self.items = list(items)

        # Cleanse list of uncalled functions
        i = 0
        while i < len(self.items):
            if isinstance(self.items[i], str):
                word = SIPA.word(self.items[i])
                self.items.pop(i)

                for sound in word:
                    self.items.insert(i, sound)
                    i += 1
                
                i -= 1

            elif self.items[i] == A:
                self.items[i] = Category()
            elif self.items[i] == C:
                self.items[i] = C()
            elif self.items[i] == V:
                self.items[i] = V()
            
            i += 1
    
    def is_match(self, word : Word, index : int) -> bool:
        if index + len(self.items) > len(word):
            return False
        
        for i in range(len(self.items)):
            if not self.items[i].is_match(word[index + i]):
                return False
        
        return True

    def __len__(self) -> int:
        return len(self.items)