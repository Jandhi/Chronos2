use crate::{category::Category, phonology::phone::Phone};

#[derive(Debug, Clone)]
pub enum Matchable {
    Category(Category),
    Phone(Phone),
}