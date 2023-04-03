from core.language import Language, LanguageChange
from volodnian.southwest.southwest_volodnian import SouthwestVolodnian
from core.chronos import *

WestVolodnian = Language('West Volodnian', 'WVol')
SWVol_to_WVol = LanguageChange(SouthwestVolodnian, WestVolodnian,
    ('Umlaut',
        (V(-Front), V(Front), (Pos, O(C), O(C), A(V(Front, Close), 'j'))),
    ),

    ('Silibant Shift',
        (C(Alveolar, Fricative), C(Dental)),
        (C(Postalveolar), C(Alveolar))
    ),

    ('Deaffrication',
        (C(Affricate), C(Fricative)),
    ),

    ('Onglide change',
        ('je', 'ja'),
    ),
)