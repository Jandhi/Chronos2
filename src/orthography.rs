use crate::phonology::word::Word;
mod token;
mod greedy;


pub trait Orthography {
    fn decode(&self, input : &str) -> Word;
    fn encode(&self, input : Word) -> String;
}