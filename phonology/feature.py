from util import default

class Feature:
    def __init__(self, name, is_negative = False, set = None) -> None:
        self.name = name
        self.set = set
        self.is_negative = is_negative

    def __neg__(self):
        return Feature(self.name, not self.is_negative, self.set)

    def __repr__(self) -> str:
        return self.name
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Feature):
            return self.name == __o.name
        else:
            return False
    
    def __hash__(self) -> int:
        return hash(('-' if self.is_negative else '') + self.name)

class FeatureSet:
    sets = []

    def __init__(self, 
        name : str,
        members : list[Feature], # Features which are a member of this set
        is_exclusive = True,     # A sound may only have one of these features
    ) -> None:
        self.name = name
        self.members = members
        self.default = None

        self.is_exclusive = is_exclusive

        for member in members:
            member.set = self
        
        FeatureSet.sets.append(self)
    
    def add(self, feature) -> None:
        self.members.add(feature)
    
    def __contains__(self, item) -> None:
        return item in self.members

    def __iter__(self):
        return self.members.__iter__()
    
    def __repr__(self) -> str:
        return f'*{self.name}*'