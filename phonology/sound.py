from phonology.features import Feature, FeatureSet
from phonology.constraints import validate_sound
from util import default

class Sound:
    def __init__(self, features = None) -> None:
        self.features : set[Feature] = default(set(features), set())
    
    def __contains__(self, item):
        if isinstance(item, FeatureSet):
            fset = item
            return any((ft in fset for ft in self.features))
        else:
            feature : Feature = item

            if feature.is_negative:
                return -feature not in self.features
            else:
                return feature in self.features
    
    def __iter__(self):
        return self.features.__iter__()
    
    def __repr__(self) -> str:
        return str(self.features)

    def add(self, *features : Feature):
        for ft in features:
            self.add_feature(ft)
    
    def add_feature(self, feature : Feature) -> bool:
        if feature.is_negative:
            return self.remove_feature(-feature)

        if feature.set.is_exclusive:
            self.remove_all(feature.set)

        self.features.add(feature)
        validate_sound(self)
    
    def add_default_feature(self, feature : Feature) -> bool:
        if feature.set.is_exclusive and any(ft in feature.set for ft in self.features):
            return
        
        self.add(feature)

    def remove(self, *features : Feature):
        for ft in features:
            self.remove_feature(ft)

    def remove_all(self, fset : FeatureSet):
        to_remove = set()

        for ft in self.features:
            if ft.set == fset:
                to_remove.add(ft)
        
        for ft in to_remove:
            self.features.remove(ft)

    def remove_feature(self, feature : Feature) -> bool:
        if feature in self.features:
            self.features.remove(feature)
            return True

        return False
    
    def is_match(self, other) -> bool:
        return self.features == other.features
    
    def copy(self):
        return Sound(self.features.copy())
    
    def generate(self, word, sounds : list):
        sounds.append(self.copy())