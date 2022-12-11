from random import randrange

def pick_weighted(items : dict):
    total = sum(items.values())
    index = randrange(0, total)
    count = 0
    for item, weight in items.items():
        count += weight
        if index < count:
            return item


def pick(list):
    return list[randrange(len(list))]

def generate():
    short_vowels = ['a', 'e', 'i', 'o', 'u']
    long_vowels = [f'{v}^_' for v in short_vowels]
    diphthongs = ['ai', 'au', 'ou', 'oi', 'eu', 'ei']
    vowels = short_vowels + long_vowels + diphthongs

    nasals = ['m', 'n', 'N']
    plosives = ['p', 'b', 't', 'd', 'k', 'g']
    liquids = ['w', 'l', 'j', 'r']
    fricatives = ['s', 'z', 'x', 'g-', 't+s']
    consonants = nasals + plosives + liquids + fricatives

    word = ''

    syllable_count_weight = {
        1 : 2,
        2 : 5,
        3 : 2,
        4 : 1,
    }
    syllable_count = pick_weighted(syllable_count_weight)
    
    for _ in range(syllable_count):
        # CV
        # CVN
        # CRV
        # CRVN
        
        syllable_type_weights = {
            'CV' : 15,
            'CVN' : 2,
            'CRV' : 2,
            'CRVN' : 1,
        }
        syllable_type = pick_weighted(syllable_type_weights)

        

        if 'R' in syllable_type:
            word += pick(plosives + fricatives + nasals)
            word += pick(liquids)
        else:
            word += pick(consonants)
        
        vowel_weights = {
            0 : 5, # short vowels
            1 : 1, # long vowels
            2 : 1, # diphthongs
        }
        word += pick((short_vowels, long_vowels, diphthongs)[pick_weighted(vowel_weights)])

        if 'N' in syllable_type:
            word += pick(nasals)
    
    return word

