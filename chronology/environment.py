from core.exception import ChronosException
from chronology.category import C, V, Category
from phonology.sound import Sound
from orthography.sipa import sipa

class SpecialItem:
    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return self.name

Pos = SpecialItem('pos')
End = SpecialItem('end')

class MatcherInterface:
    def is_match(self, other : Sound):
        pass

class InvalidEnvironmentException(ChronosException):
    def __init__(self, error_message: str):
        super().__init__(error_message)

class Environment:
    def __init__(self, items : list[MatcherInterface]) -> None:
        if items.count(Pos) != 1:
            raise InvalidEnvironmentException(f'Invalid environment {items}! You must have a single positional marker "Pos".')

        for (index, item) in enumerate(items):
            if item == End and index != 0 and index != len(items) - 1:
                raise InvalidEnvironmentException(f'Invalid environment {items}! Ends can only appear at beginning or end of sequence!')
        
        self.pre_items = items[:items.index(Pos)]
        self.post_items = items[items.index(Pos) + 1:]

    def is_match(self, preposition, postposition) -> bool:
        restrict_start = False
        restrict_end = False
        # copy cuz we popping Ends off
        pre_items = self.pre_items.copy() 
        post_items = self.post_items.copy()
        
        if len(pre_items) > 0 and pre_items[0] == End:
            restrict_start = True
            pre_items.pop(0)
        
        if len(post_items) > 0 and post_items[-1] == End:
            restrict_end = True
            post_items.pop()

        # Cannot match less than required items
        if len(preposition) < len(pre_items) or len(postposition) < len(post_items):
            return False
        
        # If we restrict ends, we are saying the length of the preposition or posposition is equal to the length of the required items
        if (restrict_start and len(pre_items) != len(preposition)) or (restrict_end and len(post_items) != len(postposition)):
            return False
        
        for i in range(len(pre_items)):
            diff = len(preposition) - len(pre_items)
            if not pre_items[i].is_match(preposition[i + diff]):
                return False
        
        for i in range(len(post_items)):
            if not post_items[i].is_match(postposition[i]):
                return False

        return True

def env(*items) -> list[Environment]:
    return generate_environments(items)

def generate_environments(items):
    return [Environment(seq) for seq in generate_sequences(*items)]

def generate_sequences(*items):
    # This is for the special case of multiple environments
    if isinstance(items[0], tuple):
        sequences = []

        for item in items:
            sequences += generate_sequences(*item)
        
        return sequences

    # Normal case
    sequences = [[]]

    for outer_item in items:
        possibilities = []
        new_sequences = []
        
        if isinstance(outer_item, Optional):
            possibilities.append([])
            
            for seq in generate_sequences(outer_item.item):
                possibilities.append(seq)
        elif isinstance(outer_item, AnyOf):
            for inner_item in outer_item.items:
                for seq in generate_sequences(inner_item):
                    possibilities.append(seq)
        # Cleanse list of uncalled functions
        elif isinstance(outer_item, str):
            possibilities.append([sipa(outer_item)])
        elif outer_item == V:
            possibilities.append([V()])
        elif outer_item == C:
            possibilities.append([C()])
        elif outer_item == A:
            possibilities.append([Category()])
        else:
            possibilities.append([outer_item])

        for p in possibilities:
            for s in sequences:
                new_sequences.append(s + p)
        
        sequences = new_sequences
    
    return sequences

class Optional:
    def __init__(self, item) -> None:
        self.item = item

def O(item):
    return Optional(item)

class AnyOf:
    def __init__(self, items) -> None:
        self.items = items

def A(*items):
    return AnyOf(list(items))