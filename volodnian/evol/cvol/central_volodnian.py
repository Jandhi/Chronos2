from core.language import Language, LanguageChange
from volodnian.evol.east_volodnian import EastVolodnian
from core.chronos import *

CentralVolodnian = Language('Central Volodnian', 'CVol')

LanguageChange(EastVolodnian, CentralVolodnian, 
    ('W Hardening',
        ('w', 'v'), 
    ),

    ('Deaffrication',
        ('d+Z', 'Z'), 
    ),

    ('Nasal Vowel Merger',
        (V(Close_mid, Nasalized), V(Open, Central, -Rounded)), 
    ),

    ('The Great Collapse',
        ((V(-Long), C, V(-Long, -Overlong, -Lengthened, -Nasalized)), (V(Lengthened), C, IF(2, V(Front), 'j')), Reversed),
        ((V( Long), C, V(-Long, -Overlong, -Lengthened, -Nasalized)), (V(Overlong), C, IF(2, V(Front), 'j')), Reversed),

        ('u', None, Pos, (V, Pos)),
        ((C, 'i'), (C(Palatalized))),
        ('i', None, Pos, (V, Pos)),


        # Corrections
        ('j', None, (A(C(Palatal), C(Postalveolar)), Pos)),
        (C(Palatalized, Postalveolar), C(-Palatalized)),
        (C(Palatalized, Palatal), C(-Palatalized)),
    ),

    ('Central Volodnian Vowel Shift',
        (V(Open, -Long, -Overlong, -Nasalized), V(Front, Open_mid)),
        (V(Front, Close_mid, -Long, -Overlong, -Nasalized), ('j', V(Open_mid)), (C(-Palatal, -Palatalized), Pos)),
        (V(Close_mid, -Long, -Overlong, -Nasalized), V(Open_mid)),
        (V(Front, Close, -Long, -Overlong, -Nasalized), ('j', V(Central)), (C(-Palatal, -Palatalized), Pos)),
        (V(Close, -Long, -Overlong, -Nasalized), V(Central, -Rounded)),

        (V(Front, Long, -Open_mid), ('j', V), Pos, ('j', Pos)),
        (V(Front, Overlong, -Open_mid), ('j', V), Pos, ('j', Pos)),

        # Corrections
        ('j', None, (A(C(Palatal), C(Postalveolar)), Pos)),
        (C(Palatalized, Postalveolar), C(-Palatalized)),
        (C(Palatalized, Palatal), C(-Palatalized)),
    ),

    ('Voicing Assimilation',
        (C(-Voiced), C(Voiced), (Pos, C(Voiced, -Approximant, -Trill, -Nasal))), 
        (C(Voiced, -Nasal, -Approximant, -Trill), C(-Voiced), (Pos, C(-Voiced))), 
    ),

    ('Second Palatalization',
        ((C(Alveolar), 'j'), C(Palatalized)),
        ((C, 'j'), C(Palatalized)),
    ),
)