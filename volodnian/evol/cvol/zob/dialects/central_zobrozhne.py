from core.language import Language, LanguageChange
from volodnian.evol.cvol.zob.middle_zobrozhne import MiddleZobrozhne
from core.chronos import *

CentralZobrozhne = Language('Central Zobrozhne', 'CZob')

LanguageChange(MiddleZobrozhne, CentralZobrozhne,         

    ('Nasalization loss',
        (V(Nasalized), V(-Nasalized)),
    ),

    ('Y-Lowering', 
        (V(Central, Close, -Rounded), V(Mid), Pos, (Pos, 'j')),
    ),

    ('Riesta',
        (C(Palatalized, Trill), C(Postalveolar, Fricative, -Palatalized)), 
    ),

    ('Je merger', 
        (V(Central, Mid), V(Front, Open_mid), ('j', Pos), (Pos, 'j')) 
    ),

    ('Ě merger',
        (V(Central, Mid), V(Close), (Pos, 'j')),
    ),

    ('Alveopalatal Merger',
        (C(Alveopalatal), C(Postalveolar)), 
    ),

    ('Final Palatal Simplification',
        ('j', None, (C, Pos, End)), 
        (C(Palatal, Nasal), C(Alveolar), (Pos, End)),
    ),

    ('Ȝeta',
        ('g-', 'j', (Pos, V(Front))), 
        ('g-', 'j', (V(Front), Pos), (Pos, V(-Front))), 
        ('g-', 'w', Pos, (Pos, V)),
        ('g-', None, (V, Pos, V)),
    ),
)