from chronology.target import Target
from chronology.environment import Environment, env, Pos, SpecialItem
from chronology.result import Result, res
from core.word import Word
from util import wrap, default

Reversed = SpecialItem('reversed')

class SoundChange:
    def __init__(self, target : Target, result : Result, environments : list[Environment], exceptions : list[Environment] = None, applies_backwards = False) -> None:
        self.target = target
        self.result = result
        self.environments = environments
        self.exceptions = exceptions
        self.applies_backwards = applies_backwards

    def apply(self, word : Word) -> Word:
        return self.__apply(word, 0 if not self.applies_backwards else len(word) - len(self.target), self.applies_backwards)

    def __apply(self, word : Word, index = 0, reversed = False) -> Word:
        if len(word) < len(self.target):
            return word
        
        i = index
        while 0 <= i and i + len(self.target) <= len(word):
            pre = word.subword(0, i)
            input = word.subword(i, len(self.target))
            post = word.subword(i + len(self.target))

            correct_env = any(env.is_match(pre, post) for env in self.environments) and (self.exceptions is None or all(not env.is_match(pre, post) for env in self.exceptions))

            if self.target.is_match(word, i) and correct_env:

                output = self.result.transform(input)

                new_word = pre + output + post
                new_index = i + len(self.target) if not reversed else i - len(self.target)

                if new_index < 0 or new_index + len(self.target) > len(word):
                    return new_word

                return self.__apply(new_word, new_index, reversed)
            
            if reversed:
                i -= 1
            else:
                i += 1
        
        return word

def sc(target, result, environment = None, exceptions = None, reversed = False):
    # If reversed token added last, make it reversed
    if environment == Reversed:
        reversed = True
        environment = None
    
    if exceptions == Reversed:
        reversed = True
        exceptions = None

    
    environment = default(environment, Pos)
    target = Target(*wrap(target))
    result = res(*wrap(result))
    evs = env(*wrap(environment))
    exc = env(*wrap(exceptions)) if exceptions is not None else None
    return SoundChange(target, result, evs, exc, reversed)