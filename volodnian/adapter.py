from core.language import Language, LanguageChange
from volodnian.proto_volodnian import ProtoVolodnian
from volodnian.master import *
from core.chronos import *

Adapter = Language('Adapter', 'Adp')

LanguageChange(Adapter, ProtoVolodnian, 
    ('Adapt Phonology',
        ('ts', 't+s'),
        ('c', 't+s'),
        ('h', 'x'),
        ('y', 'j', (Pos, V)),
        ('y', 'i'), 
        ('v', 'w'),
        ('f', 'p'),
    ),

    ('Syllable rules',
        (C(-Nasal), (C, 'o'), (Pos, C(-Approximant))),
        (C(-Nasal), (C, 'o'), (Pos, End)),
    ),
)