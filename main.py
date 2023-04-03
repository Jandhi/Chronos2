from volodnian.adapter import Adapter
from speedlang.speedlang import *
from core.exception import ChronosException
from orthography.sipa import SIPA
from word_generator import generate

while True: 
    word = input()

    if word == '':
        word = generate()

    try:
        Adapter.derive(word.split(' '), verbose=True)
    except ChronosException as err:
        print(err.message)