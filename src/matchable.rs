use crate::{category::Category, phone::Phone};

pub enum Matchable {
    Category(Category),
    Phone(Phone),
}