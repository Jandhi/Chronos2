from phonology.feature import Feature, FeatureSet
from core.exception import ChronosException
from typing import Union

key_type = Union[Feature, FeatureSet]
__requirements : dict[key_type, list[key_type]] = {}
__defaults : dict[key_type, list[Feature]] = {}

class FeatureRequirementException(ChronosException):
    def __init__(self, error_message: str):
        super().__init__(error_message)

def add_requirement(item : key_type, requirement : key_type):
    if item not in __requirements:
        __requirements[item] = []
    
    __requirements[item].append(requirement)

def add_default(item : key_type, default : Feature):
    if item not in __defaults:
        __defaults[item] = []
    
    __defaults[item].append(default)

def __validate_item(sound, item : key_type):
    if isinstance(item, FeatureSet):
        if item.is_exclusive:
            features_in_set = [f for f in sound.features if f in item]

            if len(features_in_set) > 1:
                raise FeatureRequirementException(f'Too many {item} features: {features_in_set}!')

    if item not in __requirements:
        return
    
    for req in __requirements[item]:
        if req not in sound:
            msg = f'Sound {sound} fails requirement: {item} requires {req}'
            raise FeatureRequirementException(msg)

def __add_default_to_sound(sound, item : key_type, to_process : set[Feature]):
    if item not in __defaults:
        return
    
    for feature in __defaults[item]:
        if feature in sound:
            continue

        sound.add_default_feature(feature)
        to_process.add(feature)

def add_defaults_to_sound(sound):
    processed = set()
    to_process = set()

    for feature in sound:
        if feature.set is not None and feature.set not in processed:
            to_process.add(feature.set)
        
        to_process.add(feature)
    
    while len(to_process) > 0:
        item = to_process.pop()

        if item in processed:
            continue

        __add_default_to_sound(sound, item, to_process)
        processed.add(item)


def validate_sound(sound):
    validated = set()
    
    for feature in sound:
        if feature.set is not None and feature.set not in validated:
            __validate_item(sound, feature.set)
            validated.add(feature.set)
        
        __validate_item(sound, feature)
        validated.add(feature)