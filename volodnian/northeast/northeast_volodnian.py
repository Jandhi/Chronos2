from core.language import Language, LanguageChange
from volodnian.greater_volodnian import GreaterVolodnian
from core.chronos import *

NortheastVolodnian = Language('Northeast Volodnian', 'NEVol')
GVol_to_NEVol = LanguageChange(GreaterVolodnian, NortheastVolodnian,
    ('Diphthong Merger',
        (V(Close_mid), 'a', (Pos, V)),
    ),
    
    ('Diphthong reduction',
        ('au^n', 'O^_^n'),
        ('au', 'O^_'),
        ('ai^n', 'E^_^n'),
        ('ai','E^_'),
    ),

    ('Great Collapse',
        ((V, C, V(Close, -Long)), (IF_ELSE(0, V(Long), V(Overlong), V(Lengthened)), IF_ELSE(2, V(Front), I(1, Palatalized), I(1))), Reversed),
        ((C(Trill), V(Close, -Lengthened, -Long, -Overlong)), IF_ELSE(1, V(Front), I(0, Palatalized), I(0)), Pos),
        ((C(Lateral), V(Close, -Lengthened, -Long, -Overlong)), IF_ELSE(1, V(Front), I(0, Palatalized), I(0)), Pos),
        ((C, V(Close, -Lengthened, -Long, -Overlong)), IF_ELSE(1, V(Front), I(0, Palatalized), I(0)), Pos, (C, Pos)),
        (C(-Palatalized), C(Palatalized), (Pos, V(Front, Close, Lengthened))),

        # Cleaning up illegal palatals
        (C(Palatalized, Postalveolar), X(-Palatalized)), 
        (C(Palatalized, Palatal), X(-Palatalized)),

        
    ),

    ('Voicing Assimilation',
        (C(-Voiced, -Approximant, -Nasal, -Trill), C(Voiced), (Pos, C(Voiced, -Trill, -Approximant))),
        (C(Voiced, -Approximant, -Nasal, -Trill), C(-Voiced), (Pos, C(-Voiced))),
    ),

    ('R L Syncope',
        (V(-Long), Ø, (V, C(Plosive), Pos, A(C(Trill), C(Lateral)), V)),
    ),

    ('Palatal Assimilation',
        (C(-Palatalized, -Postalveolar, -Palatal), C(Palatalized), (Pos, C(Palatalized))),
        (C(-Palatalized, -Postalveolar, -Palatal), C(Palatalized), (C(Palatalized), Pos)),
    )
)