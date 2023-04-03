pub mod sound_change;
pub mod matchable;
pub mod phonology {
    pub mod feature;
    pub mod phone;
    pub mod vowel;
}
pub mod category;
pub mod rule;
pub mod result;

use category::MakeVowel as V;

use crate::phonology::{
    vowel::Height::*, 
    vowel::Backness::*,

    feature::Feature::*,
};

fn main() {
    println!("Hello, world!");
}
