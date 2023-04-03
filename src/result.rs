use crate::phonology::{phone::Phone, feature::Feature};

pub enum Result {
    New(Phone),
    Transformed(Transform),
}

pub struct Transform {
    pub index : u8,
    pub add : Vec<Feature>,
    pub remove : Vec<Feature>,
}
