use std::default;

use super::{consonant::Voicing, phone::Phone};

#[derive(PartialEq, Eq)]
pub struct Vowel {
    pub(super) voicing : Voicing,
    pub(super) roundness : Roundness,
    pub(super) height : Height,
    pub(super) length : Length,
    pub(super) backness : Backness,
    pub(super) features : Vec<VowelFeature>,
}

impl Vowel {

    //CONSTRUCTORS

    pub fn new(height : Height, backness : Backness) -> Phone {
        Phone::Vowel(Vowel { 
            voicing: Voicing::Voiced, 
            roundness: Default::default(), 
            height, 
            length: Default::default(), 
            backness, 
            features: vec![] 
        })
    }

    // GETTERS

    pub fn voicing(&self) -> Voicing {
        self.voicing
    }

    pub fn roundness(&self) -> Roundness {
        self.roundness
    }

    pub fn height(&self) -> Height {
        self.height
    }

    pub fn length(&self) -> Length {
        self.length
    }

    pub fn backness(&self) -> Backness {
        self.backness
    }

    pub fn features(&self) -> &Vec<VowelFeature> {
        &self.features
    }

    // MUTATORS

    pub fn rounded(&mut self) -> &mut Self {
        self.roundness = Roundness::Rounded;
        self
    }
}

#[derive(Default, Clone, Copy, PartialEq, Eq)]
pub enum Roundness {
    #[default]
    Unrounded,
    Rounded
}

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Height {
    High,
    NearHigh,
    Mid,
    NearLow,
    Low
}

#[derive(Clone, Copy, PartialEq, Eq)]
pub enum Backness {
    Front,
    NearFront,
    Central,
    NearBack,
    Back
}

#[derive(Default, Clone, Copy, PartialEq, Eq)]
pub enum Length {
    Extrashort,
    #[default]
    Short,
    Long,
    Overlong,
}

#[derive(Clone, PartialEq, Eq)]
pub enum VowelFeature {
    Nasalized,
    Custom(String),
}