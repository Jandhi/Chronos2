from core.language import Language, LanguageChange
from volodnian.northeast.zobrozhnan.middle_zobrozhne import MiddleZobrozhne
from core.chronos import *


CentralZobrozhne = Language('Central Zobrozhne', 'CZob')
MZob_to_CZob = LanguageChange(MiddleZobrozhne, CentralZobrozhne,
    ('Palatal Merger',
        (C(Alveopalatal), C(Postalveolar)),
        (C(Palatalized, Velar), C(-Palatalized, Palatal)),
    ),

    ('Riesta',
        (C(Palatalized, Trill), C(Postalveolar, Fricative, -Palatalized))
    ),

    ('Vowel Reduction',
        (V(Mid), None, A((Pos, C(-Plosive)), (C(-Plosive), Pos),)),
        (V(Mid), None, (V, C, Pos, C, V)),
        (V(Open, Central, -Stressed), V(Mid), (Pos, End)),
        ('j', 'i', (A(C, End), Pos, A(C, End))),
    ),

    ('Haȝta',
        (C(Velar, Voiced, Fricative), 'u', (Pos, A(C, End))),
        ('uu', 'u^_'),
    ),

    ('Nasalization Loss',
        (V(Nasalized), V(-Nasalized)),
    ),

    ('Postalveolar Cluster Simplification',
        ((C(Postalveolar, Fricative), C(Fricative, Palatal, Voiced)), (I(0, Voiced), I(0, Voiced))),
        ((C(Postalveolar, Fricative), C(Fricative, Palatal, -Voiced)), (I(0, -Voiced), I(0, -Voiced))),
    ),
)