from orthography.orthography import orth
from phonology.features import *
from phonology.sound import Sound
from chronology.category import C, V
from core.word import Word

SIPA = orth(
    'Simplified IPA',
    [
        ('\u0301', Lengthened),
        ('^/', Lengthened),
        ('\u0304', Long),
        ('^_', Long),
        ('\u0302', Overlong),
        ('^^', Overlong),
        ('\u0303', Nasalized),
        ('^n', Nasalized),

        ('ʲ', Palatalized),
        ('^j', Palatalized),
        ('\u0331', Stressed),
        ('\'', Ejective),
        ('ʰ', Aspirated),
        ('^h', Aspirated),
        ('̥', -Voiced, V),
        ('̥', -Voiced, C(Nasal)),
        ('̥', -Voiced, C(Approximant)),
        ('.o', -Voiced, V),
        ('.o', -Voiced, C(Nasal)),
        ('.o', -Voiced, C(Approximant)),

        ('̪', (Dental, -Alveolar), C(-Fricative)),
        ('.[', (Dental, -Alveolar), C(-Fricative)),

        ('˥', Extra_high_tone),
        ('˦', High_tone),
        ('˧', Mid_tone),
        ('˨', Low_tone),
        ('˩', Extra_low_tone),
    ],
    [
        # ------
        # VOWELS

        # Front
        ('i', V(Close, Front)),
        ('y', V(Close, Front, Rounded)),
        ('ɪ', V(Near_close, Front)),
        ('I', V(Near_close, Front)),
        ('ʏ', V(Near_close, Front, Rounded)),
        ('Y', V(Near_close, Front, Rounded)),
        ('e', V(Close_mid, Front)),
        ('ø', V(Close_mid, Front, Rounded)),
        ('ɛ', V(Open_mid, Front)),
        ('E', V(Open_mid, Front)),
        ('œ', V(Open_mid, Front, Rounded)),
        ('æ', V(Open, Front)),

        # Central
        ('ɨ', V(Close, Central)),
        ('ʉ', V(Close, Central, Rounded)),
        ('ə', V(Mid, Central)),
        ('a', V(Open, Central)),

        # Back
        ('ɯ', V(Close, Back)),
        ('u', V(Close, Back, Rounded)),
        ('ʊ', V(Near_close, Back, Rounded)),
        ('U', V(Near_close, Back, Rounded)),
        ('ɤ', V(Close_mid, Back)),
        ('o', V(Close_mid, Back, Rounded)),
        ('ʌ', V(Open_mid, Back)),
        ('ɔ', V(Open_mid, Back, Rounded)),
        ('O', V(Open_mid, Back, Rounded)),
        ('ɑ', V(Open, Back)),
        ('ɒ', V(Open, Back, Rounded)),

        # ------
        # CONSONANTS

        # Nasals (voiced by default)
        ('m', C(Bilabial, Nasal)),
        ('n', C(Alveolar, Nasal)),
        ('ɳ', C(Retroflex, Nasal)),
        ('n,', C(Retroflex, Nasal)),
        ('ɲ', C(Palatal, Nasal)),
        ('ŋ', C(Velar, Nasal)),
        ('N', C(Velar, Nasal)),

        # Plosives
        ('p', C(Bilabial, Plosive)),
        ('b', C(Bilabial, Plosive, Voiced)),
        ('t', C(Alveolar, Plosive)),
        ('d', C(Alveolar, Plosive, Voiced)),
        ('c', C(Palatal, Plosive)),
        ('ɟ', C(Palatal, Plosive, Voiced)),
        ('j-', C(Palatal, Plosive, Voiced)),
        ('k', C(Velar, Plosive)),
        ('g', C(Velar, Plosive, Voiced)),
        ('q', C(Uvular, Plosive)),
        ('ɢ', C(Uvular, Plosive, Voiced)),
        ('G', C(Uvular, Plosive, Voiced)),
        ('ʔ', C(Glottal, Plosive)),
        ('?', C(Glottal, Plosive)),

        # Fricatives
        ('ɸ', C(Bilabial, Fricative)),
        ('β', C(Bilabial, Fricative, Voiced)),
        ('F', C(Bilabial, Fricative)),
        ('V', C(Bilabial, Fricative, Voiced)),
        ('f', C(Labiodental, Fricative)),
        ('v', C(Labiodental, Fricative, Voiced)),
        ('θ', C(Dental, Fricative)),
        ('ð', C(Dental, Fricative, Voiced)),
        ('T', C(Dental, Fricative)),
        ('D', C(Dental, Fricative, Voiced)),
        ('s', C(Alveolar, Fricative)),
        ('z', C(Alveolar, Fricative, Voiced)),
        ('ɕ', C(Alveopalatal, Fricative)),
        ('ʑ', C(Alveopalatal, Fricative, Voiced)),
        ('c&', C(Alveopalatal, Fricative)),
        ('z&', C(Alveopalatal, Fricative, Voiced)),
        ('ʃ', C(Postalveolar, Fricative)),
        ('ʒ', C(Postalveolar, Fricative, Voiced)),
        ('S', C(Postalveolar, Fricative)),
        ('Z', C(Postalveolar, Fricative, Voiced)),
        ('ʂ', C(Retroflex, Fricative)),
        ('ʐ', C(Retroflex, Fricative, Voiced)),
        ('s,', C(Retroflex, Fricative)),
        ('z,', C(Retroflex, Fricative, Voiced)),
        ('ç', C(Palatal, Fricative)),
        ('C', C(Palatal, Fricative)),
        ('ʝ', C(Palatal, Fricative, Voiced)),
        ('j&', C(Palatal, Fricative, Voiced)),
        ('x', C(Velar, Fricative)),
        ('ɣ', C(Velar, Fricative, Voiced)),
        ('g-', C(Velar, Fricative, Voiced)),
        ('χ', C(Velar, Fricative)),
        ('ʁ', C(Velar, Fricative, Voiced)),
        ('X', C(Velar, Fricative)),
        ('G-', C(Velar, Fricative, Voiced)),
        ('h', C(Glottal, Fricative)),
        ('ɦ', C(Glottal, Fricative, Voiced)),
        ('H', C(Glottal, Fricative, Voiced)),

        # Lateral Fricatives
        ('ɬ', C(Alveolar, Fricative, Lateral)),
        ('l-', C(Alveolar, Fricative, Lateral)),
        ('ɮ', C(Alveolar, Fricative, Lateral, Voiced)),
        ('L-', C(Alveolar, Fricative, Lateral, Voiced)),

        # Affricates
        ('t͡s', C(Alveolar, Affricate)),
        ('d͡z', C(Alveolar, Affricate, Voiced)),
        ('t+s', C(Alveolar, Affricate)),
        ('d+z', C(Alveolar, Affricate, Voiced)),
        ('t͡ɕ', C(Alveopalatal, Affricate)),
        ('d͡ʑ', C(Alveopalatal, Affricate, Voiced)),
        ('t+c&', C(Alveopalatal, Affricate)),
        ('d+z&', C(Alveopalatal, Affricate, Voiced)),
        ('t͡ʃ', C(Postalveolar, Affricate)),
        ('d͡ʒ', C(Postalveolar, Affricate, Voiced)),
        ('t+S', C(Postalveolar, Affricate)),
        ('d+Z', C(Postalveolar, Affricate, Voiced)),
        ('t͡ʂ', C(Postalveolar, Affricate)),
        ('d͡ʐ', C(Postalveolar, Affricate, Voiced)),
        ('t+s,', C(Postalveolar, Affricate)),
        ('d+z,', C(Postalveolar, Affricate, Voiced)),

        # Approximants and trills

        ('ʍ', C(Labiovelar, Approximant, -Voiced)),
        ('w', C(Labiovelar, Approximant)),
        ('ɹ', C(Alveolar, Approximant)),
        ('r/', C(Alveolar, Approximant)),
        ('r', C(Alveolar, Trill)),
        ('ɾ', C(Alveolar, Tap)),
        ('r-', C(Alveolar, Tap)),
        ('l', C(Alveolar, Approximant, Lateral)),
        ('ʎ', C(Palatal, Approximant, Lateral)),
        ('L', C(Palatal, Approximant, Lateral)),
        ('j', C(Palatal, Approximant)),
        ('ɰ', C(Velar, Approximant)),
    ]
)

Word.word_to_string = SIPA.transcribe # sets default word-to-string to sipa

def sipa(input : str) -> Sound:
    return SIPA.sound(input)