from phonology.sound import Sound
from phonology.feature import Feature
from phonology.features import Vowel, Consonant
from chronology.category import Category, V, C
from core.word import Word
from orthography.sipa import SIPA
from util import wrap

class GeneratorInterface:
    def generate(self, word : Word, sounds: list[Sound]) -> None:
        pass

Ø = GeneratorInterface()

class Transformer:
    def __init__(self, index, add_features : set[Feature], remove_features : set[Feature]) -> None:
        self.index = index
        self.add_features = add_features
        self.remove_features = remove_features
    
    def generate(self, word : Word, sounds: list[Sound]) -> None:
        sound = word[self.index].copy()

        for ft in self.add_features:
            sound.add(ft)

        for ft in self.remove_features:
            sound.remove(-ft)
        
        sounds.append(sound)

def X(*features : Feature):
    add_features = set()
    remove_features = set()

    for ft in features:
        if ft.is_negative:
            remove_features.add(ft)
        else:
            add_features.add(ft)
    
    return Transformer(None, add_features, remove_features)

def I(index, *features : Feature):
    add_features = set()
    remove_features = set()

    for ft in features:
        if ft.is_negative:
            remove_features.add(ft)
        else:
            add_features.add(ft)
    
    return Transformer(index, add_features, remove_features)

class Conditional:
    def __init__(self, index : int, category : Category, generators : list[GeneratorInterface], else_generators : list[GeneratorInterface]) -> None:
        self.index = index
        self.category : Category = category
        self.generators = generators
        self.else_generators = else_generators

    def generate(self, word : Word, sounds: list[Sound]) -> None:
        snd = word[self.index]

        if self.category.is_match(snd):
            for tr in self.generators:
                tr.generate(word, sounds)
        else:
            for tr in self.else_generators:
                tr.generate(word, sounds)

def IF(index, category : Category, transformers):
    
    return Conditional(index, category, make_generator_list(wrap(transformers)), [])

def IF_ELSE(index, category, transformers, else_transformers):
    return Conditional(index, category, make_generator_list(wrap(transformers)), make_generator_list(wrap(else_transformers)))

class Result:
    def __init__(self, generators : list[GeneratorInterface]) -> None:
        self.generators = generators

        for i in range(len(generators)):
            if generators[i] == X:
                generators[i] = X()

    def transform(self, word : Word) -> Word:
        sounds = []

        for gen in self.generators:
            gen.generate(word, sounds)
        
        return Word(sounds)

def res(*generators : GeneratorInterface) -> Result:
    gens = make_generator_list(generators)
    return Result(gens)

def make_generator_list(items) -> list[GeneratorInterface]:
    list = []

    for item in items:
        if isinstance(item, str):
            list += SIPA.word(item).sounds
        elif item is None:
            list.append(Ø)
        elif item == V or item == C:
            item = item()
            features = []

            for ft in item.include_features:
                features.append(ft)

            for ft in item.exclude_features:
                features.append(-ft)

            list.append(X(*features))
        elif isinstance(item, Category):
            features = []

            for ft in item.include_features:
                features.append(ft)

            for ft in item.exclude_features:
                features.append(-ft)

            list.append(X(*features))
        elif item == X:
            list.append(X())
        else:
            list.append(item)


    # Adds indices to non indexed elements
    counter = 0
    for gen in list:
        if isinstance(gen, Transformer) or isinstance(gen, Conditional):
            if gen.index is None:
                gen.index = counter
            
            counter += 1
        
    return list