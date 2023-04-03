from core.language import Language, LanguageChange
from volodnian.evol.cvol.central_volodnian import CentralVolodnian
from core.chronos import *

OldZobrozhne = Language('Old Zobrozhne', 'OZob')

LanguageChange(CentralVolodnian, OldZobrozhne,
    ('Length Simplification',
        (V(Overlong), V(Long)),
        (V(Lengthened), V(-Lengthened)), 
    ),

    ('Nasal Differentiation',
        ('m', 'n', (Pos, V, O(V), 'm')), 
        ('n', 'm', ('n', V, O(V), Pos)), 
    ),

    ('Back Chain Shift',
        (V(Long, Close, Back), V(Central)),
        (V(Long, Close_mid, Back), V(Close)), 
        (V(Long, Open_mid, Back), V(Close_mid)), 
    ),

    ('Ě backing',
        (V(Long, Open_mid, Front), V(Central))
    ),
    
    ('Final Frication',
        (C(Voiced, Plosive), C(Fricative), (Pos, End)), 

        # Corrections
        (C(Bilabial, Fricative), C(Labiodental)),
    )
)