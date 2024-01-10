

use super::{vowel::Vowel, consonant::Consonant, category::Matches};

#[derive(PartialEq, Eq)]
pub enum Phone {
    Vowel(Vowel),
    Consonant(Consonant),
}

impl Matches<Phone> for Phone {
    fn matches(&self, phone : &Phone) -> bool {
        self == phone
    }
}