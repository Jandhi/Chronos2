from volodnian.greater_volodnian import *
from volodnian.northeast.zobrozhnan.central_zobrozhne import *
from volodnian.southwest.west_volodnian import *
from speedlang.speedlang import *
from core.exception import ChronosException
from orthography.sipa import SIPA
from word_generator import generate

while True: 
    word = input()

    if word == '':
        word = generate()

    try:
        ProtoVolodnian.derive(word, verbose=True)
    except ChronosException as err:
        print(err.message)