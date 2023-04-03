from core.language import Language, LanguageChange
from volodnian.northeast.northeast_volodnian import NortheastVolodnian
from core.chronos import *

NorthVolodnian = Language('North Volodnian', 'NVol')
NEVol_to_NVol = LanguageChange(NortheastVolodnian, NorthVolodnian,
    ('North Volodnian Stress Shift',
        # Single Syllable
        (V, V(Stressed), (End, O(C), O(C), Pos, O(C), O(C), End)),
        # Heavy Start
        (V(Long), V(Stressed), (End, O(C), O(C), Pos)),
        (V(Lengthened), V(Stressed), (End, O(C), O(C), Pos)),
        (V(Overlong), V(Stressed), (End, O(C), O(C), Pos)),
        (V, V(Stressed), (End, O(C), O(C), Pos, C, C)),
        # Light Heavy
        (V(Long), V(Stressed), (End, O(C), O(C), V(-Long, -Lengthened, -Overlong), C, Pos)),
        (V(Lengthened), V(Stressed), (End, O(C), O(C), V(-Long, -Lengthened, -Overlong), C, Pos)),
        (V(Overlong), V(Stressed), (End, O(C), O(C), V(-Long, -Lengthened, -Overlong), C, Pos)),
        (V, V(Stressed), (End, O(C), O(C), V(-Long, -Lengthened, -Overlong), C, Pos, C, A(C, End))),

        # Light Light
        (V, V(Stressed), (End, O(C), O(C), Pos, C, V(-Stressed))),
    ),

    ('Lengthened Merger',
        (V(Lengthened, Close), V(Close_mid)),
    ),

    ('Deaffrication',
        (C(Affricate, Voiced), C(Fricative))
    ),

    ('Velar Fricative Assimilation',
        (C(Velar, Fricative), C(Postalveolar), (Pos, C(Postalveolar))),
        (C(Velar, Fricative), C(Postalveolar), (C(Postalveolar), Pos)),
    ),
)