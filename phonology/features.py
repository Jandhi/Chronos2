from phonology.feature import Feature, FeatureSet
from phonology.constraints import add_requirement, add_default


Vowel = Feature('vowel')
Consonant = Feature('consonant')
Type = FeatureSet('type', members=[
    Vowel, Consonant
])

# Voicing
Voiced = Feature('voiced')
Voicing = FeatureSet('voicing', members=[
    Voiced
])
add_default(Vowel, Voiced)

# VOWELS

# Height
Close = Feature('close')
Near_close = Feature('near-close')
Close_mid = Feature('close-mid')
Mid = Feature('mid')
Open_mid = Feature('open-mid')
Open = Feature('open')

Height = FeatureSet('height', members=[
    Close, Near_close, Close_mid, Mid, Open_mid, Open
])
add_requirement(Height, Vowel)
add_requirement(Vowel, Height)


# Backness
Front = Feature('front')
Central = Feature('central')
Back = Feature('back')

Backness = FeatureSet('backness', members=[
    Front, Central, Back
])
add_requirement(Backness, Vowel)
add_requirement(Vowel, Backness)

# Tone
Extra_high_tone = Feature('extra-high-tone')
High_tone = Feature('high-tone')
Mid_tone = Feature('mid-tone')
Low_tone = Feature('low-tone')
Extra_low_tone = Feature('extra-low-tone')
Rising_tone = Feature('rising-tone')
Falling_tone = Feature('falling-tone')

Tone = FeatureSet('tone', members=[
    Extra_high_tone, High_tone, Mid_tone, Low_tone, Extra_low_tone,
    Rising_tone, Falling_tone,
])
add_requirement(Tone, Vowel)

# Length
Ultrashort = Feature('ultrashort')
Lengthened = Feature('lengthened')
Long = Feature('long')
Overlong = Feature('overlong')
Length = FeatureSet('length', members=[
    Ultrashort, Lengthened, Long, Overlong
])
add_requirement(Length, Vowel)

# Vowel Features
Rounded = Feature('rounded')
Nasalized = Feature('nasalized')
Stressed = Feature('stressed')
VowelFeatures = FeatureSet('vowel feature', members=[
    Rounded, Nasalized, Stressed
], is_exclusive=False)
add_requirement(VowelFeatures, Vowel)

# CONSONANTS

# Place of Articulation
Bilabial = Feature('bilabial')
Labiovelar = Feature('labiovelar')
Labiodental = Feature('labiodental')
Dental = Feature('dental')
Alveolar = Feature('alveolar')
Alveopalatal = Feature('alveopalatal')
Alveovelar = Feature('alveovelar')
Postalveolar = Feature('postalveolar')
Retroflex = Feature('retroflex')
Palatal = Feature('palatal')
Velar = Feature('velar')
Uvular = Feature('uvular')
Pharyngeal = Feature('pharyngeal')
Glottal = Feature('glottal')
PlaceOfArticulation = FeatureSet('place of articulation', members=[
    Bilabial, Labiovelar, Labiodental, Dental, Alveolar, Alveopalatal, Alveovelar, 
    Postalveolar, Retroflex, Palatal, Velar, Uvular, Pharyngeal, Glottal
])
add_requirement(PlaceOfArticulation, Consonant)
add_requirement(Consonant, PlaceOfArticulation)

# Manner of Articulation
Plosive = Feature('plosive')
Affricate = Feature('affricate')
Fricative = Feature('fricative')
Nasal = Feature('nasal')
Trill = Feature('trill')
Tap = Feature('tap')
Approximant = Feature('approximant')
Ejective = Feature('ejective')
Implosive = Feature('implosive')
MannerOfArticulation = FeatureSet('manner of articulation', members=[
    Plosive, Affricate, Fricative, Nasal, Trill, Tap, Approximant, Ejective, Implosive
])
add_requirement(MannerOfArticulation, Consonant)
add_requirement(Consonant, MannerOfArticulation)
add_default(Approximant, Voiced)
add_default(Nasal, Voiced)
add_default(Trill, Voiced)
add_default(Tap, Voiced)

# Consonant Features
Vocalic = Feature('vocalic')
Lateral = Feature('lateral')
Palatalized = Feature('palatalized')
Aspirated = Feature('aspirated')
ConsonantFeatures = FeatureSet('consonant features', members=[
    Vocalic, Lateral, Palatalized, Aspirated
], is_exclusive=False)
add_requirement(ConsonantFeatures, Consonant)