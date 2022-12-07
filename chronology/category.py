from phonology.feature import Feature
from phonology.sound import Sound
from phonology.constraints import add_defaults_to_sound, validate_sound, FeatureRequirementException
from phonology.features import Consonant, Vowel

# An Object to match many sounds based on their features
class Category:
    def __init__(self, include_features : set[Feature], exclude_features : set[Feature]) -> None:
        self.include_features = include_features
        self.exclude_features = exclude_features
    
    def is_match(self, other : Sound):
        for ft in self.include_features:
            if ft not in other.features:
                return False
        
        for ft in self.exclude_features:
            if ft in other.features:
                return False
            
        return True

    def sound(self) -> Sound:
        sound = Sound(self.include_features)
        add_defaults_to_sound(sound)

        for ft in self.exclude_features:
            sound.add_feature(-ft)

        validate_sound(sound)
        return sound
    
    def __repr__(self) -> str:
        letter = 'V' if Vowel in self.include_features else ('C' if Consonant in self.include_features else '?')
        features = ''

        for ft in self.include_features:
            if ft != Vowel and ft != Consonant:
                features = f'{features}+{ft},'
        
        for ft in self.exclude_features:
            features = f'{features}-{ft},'
        
        if features == '':
            return letter
        else:
            return f'{letter}[{features[:-1]}]'
    
    def copy(self):
        return Category(self.include_features.copy(), self.exclude_features.copy())

def make_cat(*features : Feature) -> Category:
    pos = set()
    neg = set()

    for ft in features:
        if ft.is_negative:
            neg.add(-ft)
        else:
            pos.add(ft)
    
    return Category(pos, neg)

def C(*features : Feature) -> Category:
    return make_cat(Consonant, *features)

def V(*features : Feature) -> Category:
    return make_cat(Vowel, *features)