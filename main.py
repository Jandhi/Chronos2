from volodnian.greater_volodnian import *
from volodnian.northeast.zobrozhnan.central_zobrozhne import *
from volodnian.southwest.west_volodnian import *
from speedlang.speedlang import *
from orthography.sipa import SIPA

while True: 
    word = input()
    ProtoVolodnian.derive(word, verbose=True)