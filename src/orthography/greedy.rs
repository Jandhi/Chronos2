use std::collections::HashMap;

use crate::phonology::{word::Word, category::Matches};

use super::{token::{Token, Modifier}, Orthography};


pub struct GreedyOrthography {
    tokens : Vec<Token>,
    modifiers : Vec<Modifier>,
}

/*
DECODING:
    The greedy orthography consumes as many characters it can at once
    If it finds any modifiers at the end, it will pop those characters off to modify the result
    If it matches any token, pop those characters and push the token

ENCODING:
    Consumes as many characters as it can, first trying to match a token to a word
    Eventually trying to match individual phones, in which case it first tries to remove all modifiers first

*/

impl Orthography for GreedyOrthography {
    fn decode(&self, input : &str) -> Word {
        todo!()
    }

    fn encode(&self, input : Word) -> String {
        let result = String::new();
        while input.len() > 0 {
            let mut length = input.len();

            while length > 1 {
                for token in self.tokens.iter() {
                    if token.word().matches(t) {
                        
                    }
                }
            }
        }

        result
    }
}