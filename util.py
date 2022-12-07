# returns first object that is not none
def default(*args) -> any:
    for arg in args:
        if arg is not None:
            return arg

def wrap(item) -> tuple:
    if isinstance(item, tuple):
        return item
    elif isinstance(item, list):
        return item
    else:
        return [item]