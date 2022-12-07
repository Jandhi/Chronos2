from core.language import Language, LanguageChange
from core.chronos import *

ProtoLang = Language('Proto-Lang', 'Proto')
SpeedLang = Language('Speed-Lang', 'Lang')

ProtoToSpeed = LanguageChange(ProtoLang, SpeedLang, 
    ('Tonogenisis',
        (V, V(Low_tone), (Pos, C(Voiced, Fricative))),
        (V, V(Low_tone), (Pos, C(Voiced, Plosive))),
        (V, V(High_tone), (Pos, C(-Voiced))),
    ),

    ('Coda restriction',
        (C(Plosive, -Voiced), '?', (Pos, A(End, C))),
        (C(Fricative), None, (V, Pos)),
        (C(Lateral, Approximant), C(Labiovelar, -Lateral), (Pos, A(End, C))),
        (C(Plosive), None, (A(C(Nasal), C(Voiced, Plosive)), Pos)),
    ),

    ('Vowel Shift',
        ((V(Open, Central), 'w'), V(Open, Back, Rounded).sound()),
        ((V(Open, Central), V(Back)), V(Open, Back, Rounded).sound()),
        ((V(Open, Central), 'j'), V(Open, Front).sound()),
        ((V(Open, Central), V(Front)), V(Open, Front).sound()),
    ),

    ('Nasal Merger',
        (C(Nasal), C(Plosive), (End, Pos)),
        (C(Plosive, Voiced), C(Nasal), (V, Pos)),
    ),

    ('Approximant Merger',
        (C(Labiodental, Fricative), C(Labiovelar, Approximant)),
        ((C(Approximant, -Voiced), V(-Low_tone)), (C(Voiced), V(High_tone))),
        (C(Approximant, -Voiced), C(Voiced)),
    ),

    ('Lateral Allophony',
        (C(Lateral, Approximant), C(Tap, -Lateral), (V, Pos, V)),
    ),
)