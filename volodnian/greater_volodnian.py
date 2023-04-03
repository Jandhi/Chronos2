from core.language import Language, LanguageChange
from volodnian.proto_volodnian import ProtoVolodnian
from core.chronos import *

GreaterVolodnian = Language('Greater Volodnian', 'GVol')

LanguageChange(ProtoVolodnian, GreaterVolodnian, 
    ('U-umlaut',
        ('a', 'o', (Pos, C, V(Close, Rounded))),
        ('e', 'o', (Pos, C, V(Close, Rounded))),
        ('i', 'u', (Pos, C, V(Close, Rounded))),
        
        ('a^_', 'o^_', (Pos, C, V(Close, Rounded))),
        ('e^_', 'o^_', (Pos, C, V(Close, Rounded))),
        ('i^_', 'u^_', (Pos, C, V(Close, Rounded))),
    ),

    ('Glide Prosthesis',
        (V(Front), ('j', V), (End, Pos)),
        (V, ('w', V), (End, Pos)),
    ),

    ('First Palatalization',
        ('x', 'S', (Pos, V(Front))), 
        ('g-', 'Z', (Pos, V(Front))), 
        ('k', 't+S', (Pos, V(Front))), 
        ('g', 'd+Z', (Pos, V(Front))), 
    ),
)