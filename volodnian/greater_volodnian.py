from volodnian.proto_volodnian import ProtoVolodnian
from core.language import Language, LanguageChange
from core.chronos import *

GreaterVolodnian = Language('Greater Volodnian', 'GVol')

PVol_to_GVol = LanguageChange(ProtoVolodnian, GreaterVolodnian,
    ('U-Umlaut',
        ('a', 'o', (Pos, C, V(Close, Rounded))),
        ('a^_', 'o^_', (Pos, C, V(Close, Rounded))),
        ('e', 'o', (Pos, C, V(Close, Rounded))),
        ('e^_', 'o^_', (Pos, C, V(Close, Rounded))),
        ('i', 'u', (Pos, C, V(Close, Rounded))),
        ('i^_', 'u^_', (Pos, C, V(Close, Rounded))),
    ),

    ('Nasal Merger',
        ('N', 'n')
    ),

    ('Nasalization',
        ((V, C(Nasal)), V(Nasalized), Pos, (Pos, V))
    ),

    ('Glide Prosthesis',
        (V(Front), ('j', V), (End, Pos)),
        (V, ('w', V), (End, Pos)),
    ),

    ('Short Vowel Merger',
        # Short vowels merge unless they are the first syllable (stressed) or in a diphthong (next to another vowel)
        (V(Close_mid, -Long), V(Close), Pos, [(End, O(C), O(C), Pos), (Pos, V), (V, Pos)])
    ),

    ('W Hardening',
        ('w', 'v')
    ),

    ('First Palatalization',
        ('x', 'S', (Pos, V(Front))),
        ('g-', 'Z', (Pos, V(Front))),
        ('k', 't+S', (Pos, V(Front))),
        ('g', 'd+Z', (Pos, V(Front))),
    )
)