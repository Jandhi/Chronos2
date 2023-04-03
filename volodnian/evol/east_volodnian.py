from core.language import Language, LanguageChange
from volodnian.greater_volodnian import GreaterVolodnian
from core.chronos import *

EastVolodnian = Language('East Volodnian', 'EVol')

LanguageChange(GreaterVolodnian, EastVolodnian, 
    ('Nasal Merger',
        ('N', 'n'),
    ),

    ('Nasalization',
        ((V, C(Nasal)), (V(Nasalized)), Pos, (Pos, V)), 
    ),

    ('W Hardening',
        ('w', 'v')
    ),

    ('Diphthong Smoothing',
        ('ai', 'E^_'),
        ('au', 'O^_'),
    ),
)