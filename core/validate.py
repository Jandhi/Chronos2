from phonology.sound import Sound
from chronology.category import C, V, Category

def validate_category(cat) -> Category:
    if cat == C:
        return C()
    if cat == V:
        return V()
    if cat is None:
        return Category([], [])
    return cat

def validate_sound(snd) -> Sound:
    if isinstance(snd, Category):
        return snd.sound()
    
    return snd