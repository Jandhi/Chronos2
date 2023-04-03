from core.language import Language, LanguageChange
from volodnian.evol.cvol.zob.old_zobrozhne import OldZobrozhne
from core.chronos import *

MiddleZobrozhne = Language('Middle Zobrozhne', 'MZob')

LanguageChange(OldZobrozhne, MiddleZobrozhne, 
    
    ('U-I Merger',
        (V(Central, Rounded), V(Front, -Rounded)),
    ),
               
    ('Ě Diphthongization',
        (V(Long, Central, Open_mid), ('əj')),
    ),

    ('Vowel Length Loss',
        (V, V(-Long, -Overlong, -Lengthened)), 
    ),

    ('Depalatalization',
        (C(Palatalized, -Alveolar), (C(-Palatalized), 'j')), 
        (C(Nasal, Palatalized), C(Palatal, -Palatalized)),
        (C(Lateral, Palatalized), C(Palatal, -Palatalized)),
        (C(Alveolar, Palatalized, Plosive), C(-Palatalized, Alveopalatal, Affricate)),
        (C(Alveolar, Palatalized, -Trill), C(-Palatalized, Alveopalatal)),
    ),

    ('ljetta',
        (C(Lateral, Palatal), C(-Lateral, Approximant)),
    ),

    ('velar palatalization',
        ((C(Velar), 'j'), C(Palatal)),
    ),
)