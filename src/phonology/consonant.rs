use std::default;

use super::{feature::Feature, phone::Phone::{Vowel, Consonant as Cons, self}};

#[derive(PartialEq, Eq)]
pub struct Consonant {
    pub(super) voicing : Voicing,
    pub(super) place : PlaceOfArticulation,
    pub(super) manner : MannerOfArticulation,
    pub(super) features : Vec<ConsonantFeature>,
}

impl Consonant {
    // CONSTRUCTORS

    pub fn new(place : PlaceOfArticulation, manner : MannerOfArticulation) -> Phone {
        Cons(Consonant {
            voicing: Default::default(),
            place,
            manner,
            features: vec![],
        })
    }

    pub fn voiced(place : PlaceOfArticulation, manner : MannerOfArticulation) -> Phone {
        Cons(Consonant { voicing: Voicing::Voiced, place, manner, features: vec![] })
    }

    // GETTERS

    pub fn voicing(&self) -> Voicing {
        self.voicing
    }

    pub fn place(&self) -> PlaceOfArticulation {
        self.place
    }

    pub fn manner(&self) -> MannerOfArticulation {
        self.manner
    }

    pub fn features(&self) -> &Vec<ConsonantFeature> {
        &self.features
    }

    // MUTATORS

    pub fn with_feature(&mut self, feature : ConsonantFeature) -> &mut Self {
        self.features.push(feature);
        self
    }

    pub fn with_features(&mut self, mut features : Vec<ConsonantFeature>) -> &mut Self {
        self.features.append(&mut features);
        self
    }
}

#[derive(Default, PartialEq, Eq, Clone, Copy)]
pub enum Voicing {
    Voiced,
    #[default]
    Unvoiced
}

#[derive(PartialEq, Eq, Clone, Copy)]
pub enum PlaceOfArticulation {
    Dental,
    Labiodental,
    Bilabial,
    Alveolar,
    Alveopalatal,
    Postalveolar,
    Retroflex,
    Palatal,
    Velar,
    Uvular,
    Pharyngeal,
    Glottal,
}

#[derive(PartialEq, Eq, Clone, Copy)]
pub enum MannerOfArticulation {
    Nasal,
    Plosive,
    Affricate,
    Fricative,
    Approximant,
    Trill,
    Tap,
}

#[derive(PartialEq, Eq, Clone)]
pub enum ConsonantFeature {
    Labialized,
    Palatalized,
    Custom(String),
}