from core.language import Language, LanguageChange
from volodnian.eastern_volodnian import EasternVolodnian
from core.chronos import *

SouthwestVolodnian = Language('Southwest Volodnian', 'SWVol')
GVol_to_SWVol = LanguageChange(EasternVolodnian, SouthwestVolodnian,
    ('Syncope',
        (V(-Long), None, (V, C, Pos, C, V)),
    ),

    ('Coarticulate Shift',
        ((C(Velar), 'v'), C(Labialized))
    ),

    ('Labial Shift',
        (C(Labiodental), C(Bilabial))
    ),

    ('Long Vowel Shift',
        (V(Open, Central, Long), V(Open_mid, Front), (C(Alveolar, -Lateral), Pos)),
        (V(Open, Central, Long), V(Open_mid, Back, Rounded)),
        ((V(Open), V(Close)), V(Long)),
    ),
)