mod sound_change;
mod matchable;
mod category;
mod phone;

use sound_change::sound_change;

use crate::{category::Category, matchable::Matchable};

fn main() {
    println!("Hello, world!");

    let x = sound_change("").target(vec![]);
}
