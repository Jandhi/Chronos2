

use std::iter::zip;

use super::{phone::Phone, category::Matches};

pub struct Word {
    phones : Vec<Phone>,
}

impl Word {
    pub fn new() -> Word {
        Word { phones: vec![] }
    }

    pub fn append(&mut self, mut other : Word) -> &mut Self {
        self.phones.append(&mut other.phones);
        self
    }

    pub fn len(&self) -> usize {
        self.phones.len()
    }

    pub fn pop(&mut self) -> Phone {
        self.phones.pop().expect("Should have a last element")
    }

    pub fn last(&self) -> Option<&Phone> {
        self.phones.last()
    }

    pub fn remove_start(&mut self, length : usize) {
        for _ in 0..length {
            self.phones.remove(0);
        }
    }

    pub fn slice<'a>(&'a self, start : usize, end : usize) -> &'a [Phone] {
        &self.phones[start..end]
    }
}

impl From<Vec<Phone>> for Word {
    fn from(value: Vec<Phone>) -> Self {
        Word { phones: value }
    }
}

impl From<Phone> for Word {
    fn from(value: Phone) -> Self {
        Word { phones: vec![value] }
    }
}

impl Matches<Word> for Word {
    fn matches(&self, word : &Word) -> bool {
        if word.len() != self.len() {
            false
        } else {
            self.phones.iter()
                .zip(word.phones.iter())
                .all(|(p1, p2)| p1.matches(p2))
        }
    }
}

impl Matches<Word> for &[Phone] {
    fn matches(&self, word : &Word) -> bool {
        if word.len() != self.len() {
            false
        } else {
            self.iter()
                .zip(word.phones.iter())
                .all(|(p1, p2)| p1.matches(p2))
        }
    }
}