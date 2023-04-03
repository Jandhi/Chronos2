from core.language import Language, LanguageChange
from volodnian.southwest.south_volodnian import SouthVolodnian
from core.chronos import *

OldKarosan = Language('Old Karosan', 'OKar')
SVol_to_OKar = LanguageChange(SouthVolodnian, OldKarosan,
    ('Initial V Lost',
        (C(Bilabial, Fricative), None, (End, Pos))
    ),

    ('Karosan Consonant Shift',
        (C(Plosive, -Voiced), C(Aspirated), Pos, (Pos, C(Fricative))),
        (C(Plosive, Voiced), C(-Voiced)),
        (C(Fricative, Voiced, -Postalveolar), C(Plosive)),
    ),

    ('Karosan Spirant Shift',
        (C(Alveolar, Fricative), None, (V, Pos, V)),
        (C(Alveolar, Fricative), C(Glottal), Pos, (C(Plosive), Pos)),
        (C(Postalveolar), C(Alveolar)),
        (C(Velar, Fricative), C(Postalveolar)),
    ),

    ('Denasalization',
        (V(Nasalized), (V(-Nasalized), 'm'), (Pos, A(C(Bilabial), C(Labiodental)))),
        (V(Nasalized), (V(-Nasalized), 'N'), (Pos, C(Velar))),
        (V(Nasalized), (V(-Nasalized), 'n'), (Pos, C)),
        (V(Nasalized), V(-Nasalized)),
    ),

    ('Grassmann\'s Law?',
        (C(Aspirated), C(-Aspirated), (Pos, V, C(Aspirated))),
        (C(Glottal, Fricative), None, (Pos, V, C(Aspirated))),
    ),
    
    ('J Changes',
        (C(Palatal, Approximant), None, (V, Pos, V)),
        (C(Palatal, Approximant), 'i', (Pos, V))
    ),
    
    ('Cluster Shift',
        ((C(Alveolar, Plosive), C(Bilabial, Plosive)), 'pt', (End, Pos))
    )

    #('Weak High Vowel Loss',
    #    (V(Close, -Long), None, (End, C, Pos, C, A(V(-Close), V(Long)))),
    #    (V(Close, -Long), None, (V, C, Pos, C, A(C, End))),
    #    (V(Close, -Long), None, (V, C, A(V(-Close), V(Long)), C, Pos)),
    #)
)