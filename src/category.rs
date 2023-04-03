use crate::phonology::{feature::Feature};
use std::{ops, vec};

#[derive(Debug, Clone)]
pub struct Category {
    has_features : Vec<Feature>,
    has_not_features : Vec<Feature>,
}

impl ops::Add<Feature> for Category {
    type Output = Category;

    fn add(self, rhs: Feature) -> Self::Output {
        let mut clone = self.clone();
        clone.has_features.push(rhs);
        return clone
    }
}

impl ops::Sub<Feature> for Category {
    type Output = Category;

    fn sub(self, rhs: Feature) -> Self::Output {
        let mut clone = self.clone();
        clone.has_not_features.push(rhs);
        return clone;
    }
}