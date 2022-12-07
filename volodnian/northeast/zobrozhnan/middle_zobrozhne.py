from core.language import Language, LanguageChange
from volodnian.northeast.zobrozhnan.old_zobrozhne import OldZobrozhne
from core.chronos import *


MiddleZobrozhne = Language('Middle Zobrozhne', 'MZob')
OZob_to_MZob = LanguageChange(OldZobrozhne, MiddleZobrozhne,
    ('Close-mid vowel shift',
        (V(Close_mid, Front, -Long), ('j', V(Open_mid)), Pos, (Pos, 'j')),
        (V(Close_mid, Back, -Long), V(Open_mid)),
    ),

    ('Glide shift',
        (V(Open, Central), V(Open_mid, Front), ('j', Pos)),
    ),

    ('Diphthong merger',
        (V(Close_mid), V(Open_mid), (Pos, 'j')),
        (V(Open, Central), V(Open_mid, Back, Rounded), (Pos, 'j')),
    ),

    ('Palatal Simplification',
        ('j', None, (C(Palatalized), Pos)),
        ('jj', 'j'),
        ('j', None, (C(Postalveolar), Pos)),
        ((C(Alveolar), 'j'), C(Palatalized)),
        (C(Lateral, Palatalized), 'j'),
    ),

    ('Long Vowel Loss',
        (V(Long), V(-Long)),
    ),

    ('Palatalized A Shift',
        (V(Open), V(Open_mid, Front), (C(Palatalized), Pos)),
        (V(Open), V(Open_mid, Front), ('j', Pos)),
    ),

    ('Middle Zobrozhne Palatal Change',
        (C(Alveolar, Palatalized, Nasal), C(-Palatalized, Palatal)),
        (C(Alveolar, Palatalized, -Trill, -Plosive), C(-Palatalized, Alveopalatal)),
        (C(Alveolar, Palatalized, Plosive), C(-Palatalized, Affricate, Alveopalatal)),
    ),

    ('High Vowel Shift',
        (V(Central, Close), V(Front, -Rounded))
    ),

    ('Intervocalic Lenition',
        (C(Fricative, -Postalveolar, -Voiced), C(Voiced), (V, Pos, V(-Stressed)))
    ),
)