from core.language import Language, LanguageChange
from volodnian.northeast.north_volodnian import NorthVolodnian
from core.chronos import *

OldZobrozhne = Language('Old Zobrozhne', 'OZob')
NVol_to_OZob = LanguageChange(NorthVolodnian, OldZobrozhne,
    ('A Reduction',
        (V(Open, Central, -Stressed, -Long, -Overlong, -Lengthened), V(Mid), None, (Pos, End)),
    ),

    ('Nasal Diffentiation',
        ((C(Nasal), V, C(Nasal), V), (C(Alveolar), V, C(Bilabial), V)),
    ),

    ('Length Merger',
        (V(Overlong), V(Long)),
        (V(Close_mid, -Lengthened, -Long), V(Open_mid)),
        (V(Lengthened), V(-Lengthened)),
    ),

    ('Final Lenition',
        (C(Plosive, Voiced), C(Fricative), (Pos, End)),
        (C(Bilabial, Fricative), C(Labiodental)),
    ),

    ('Zobrozhnian Back Chain Shift',
        (V(Close, Back), V(Central)),
        (V(Close_mid, Back, Long), V(Close)),
        (V(Close_mid, Back, Overlong), V(Close)),
        (V(Open_mid, Back, Long), V(Close_mid)),
        (V(Open_mid, Back, Overlong), V(Close_mid)),
    ),

    ('Palatal Simplification',
        ('l^j', 'ji', (A(C, End), Pos, C)),
        ('l^j', 'j'),
        (C(Nasal, Palatalized), C(-Palatalized), (Pos, End)),
        ('j', 'i', (V, Pos, A(C, End)),), 
    ),

    ('Cluster Simplification',
        (C(Alveolar, Plosive), None, (C(Affricate), Pos)),
    ),

    # Leave this for somewhere else? bogda bodgyka > bozza bozzka
    ('Cluster Lenition',
        (C(Voiced, Plosive), C(Fricative), (C(Voiced, Plosive), Pos), (Pos, C)),
        (C(Bilabial, Fricative), C(Labiodental)),
    ),

    ('Nasal Cluster Shift',
        (C(Nasal), C(Plosive), (Pos, C(Trill)))
    ),
)