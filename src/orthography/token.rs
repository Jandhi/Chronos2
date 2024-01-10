use crate::phonology::{phone::Phone, feature::Feature, word::Word};

pub struct Token {
    string : String,
    word : Word,
}

impl Token {
    pub fn string<'a>(&'a self) -> &'a String {
        &self.string
    }

    pub fn word<'a>(&'a self) -> &'a Word {
        &self.word
    }
}

pub struct Modifier {
    string : String,
    feature : Feature,
}

impl Modifier {
    fn new(string : &str, feature : impl Into<Feature>) -> Modifier {
        Modifier { string: string.to_string(), feature: feature.into() }
    }
}

