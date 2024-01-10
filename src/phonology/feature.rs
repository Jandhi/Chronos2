use super::{phone::Phone, consonant::{Voicing, PlaceOfArticulation, MannerOfArticulation, ConsonantFeature}, vowel::{Roundness, Height, Backness, Length, VowelFeature}};


pub enum Feature {
    Voicing(Voicing),
    Place(PlaceOfArticulation),
    Manner(MannerOfArticulation),
    ConsonantFeature(ConsonantFeature),
    Roundness(Roundness),
    Height(Height),
    Backness(Backness),
    Length(Length),
    VowelFeature(VowelFeature),
}

pub struct FeatureError {
    pub description : String,
}

impl Phone {
    pub fn has(&self, feature : impl Into<Feature>) -> bool {
        let generalized_feature : Feature = feature.into();
        match (generalized_feature, self) {
            (Feature::Voicing(voicing), Phone::Vowel(vowel)) => {
                vowel.voicing() == voicing
            }
            (Feature::Voicing(voicing), Phone::Consonant(cons)) => {
                cons.voicing() == voicing
            }
            (Feature::Place(_) 
                | Feature::Manner(_) 
                | Feature::ConsonantFeature(_), Phone::Vowel(_)) => {
                false
            }
            (Feature::Place(place), Phone::Consonant(cons)) => {
                cons.place() == place
            }
            (Feature::Manner(manner), Phone::Consonant(cons)) => {
                cons.manner() == manner
            }
            (Feature::ConsonantFeature(feature), Phone::Consonant(cons)) => {
                cons.features().contains(&feature)
            }
            (Feature::Roundness(roundness), Phone::Vowel(vowel)) => {
                vowel.roundness() == roundness
            },
            (Feature::Roundness(_) 
                | Feature::Height(_)
                | Feature::Backness(_)
                | Feature::Length(_)
                | Feature::VowelFeature(_), Phone::Consonant(_)) => false,
            (Feature::Height(height), Phone::Vowel(vowel)) => {
                vowel.height() == height
            },
            (Feature::Backness(backness), Phone::Vowel(vowel)) => {
                vowel.backness() == backness
            },
            (Feature::Length(length), Phone::Vowel(vowel)) => {
                vowel.length() == length
            },
            (Feature::VowelFeature(feature), Phone::Vowel(vowel)) => {
                vowel.features().contains(&feature)
            },
        }
    }

    pub fn add(&mut self, feature : impl Into<Feature>) -> Option<FeatureError> {
        let generalized_feature : Feature = feature.into();
        match (generalized_feature, self) {
            (Feature::Voicing(voicing), Phone::Vowel(vowel)) => {
                vowel.voicing = voicing
            }
            (Feature::Voicing(voicing), Phone::Consonant(cons)) => {
                cons.voicing = voicing
            }
            (Feature::Place(_), Phone::Vowel(_)) => {
                return Some(FeatureError{
                    description: "A vowel cannot have a place of articulation".to_string(),
                })
            },
            (Feature::Manner(_), Phone::Vowel(_)) => {
                return Some(FeatureError{
                    description: "A vowel cannot have a manner of articulation".to_string(),
                })
            },
            (Feature::ConsonantFeature(_), Phone::Vowel(_)) => {
                return Some(FeatureError{
                    description: "A vowel cannot have a consonant feature".to_string(),
                })
            },
            (Feature::Place(place), Phone::Consonant(cons)) => {
                cons.place = place
            }
            (Feature::Manner(manner), Phone::Consonant(cons)) => {
                cons.manner = manner
            }
            (Feature::ConsonantFeature(feature), Phone::Consonant(cons)) => {
                if !cons.features().contains(&feature) {
                    cons.features.push(feature)
                }   
            }
            (Feature::Roundness(roundness), Phone::Vowel(vowel)) => {
                vowel.roundness  = roundness
            },
            (Feature::Roundness(_), Phone::Consonant(_)) => {
                return Some(FeatureError { 
                    description: "A consonant cannot have a roundness (You may want labialization instead)".to_string()
                })
            }
            (Feature::Height(_), Phone::Consonant(_)) => {
                return Some(FeatureError { 
                    description: "A consonant cannot have a height".to_string()
                })
            }
            (Feature::Backness(_), Phone::Consonant(_)) => {
                return Some(FeatureError { 
                    description: "A consonant cannot have a backness".to_string()
                })
            }
            (Feature::Length(_), Phone::Consonant(_)) => {
                return Some(FeatureError { 
                    description: "A consonant cannot have a length (For gemination, duplicate the phone or add a custom consonant feature)".to_string()
                })
            }
            (Feature::VowelFeature(_), Phone::Consonant(_)) => {
                return Some(FeatureError { 
                    description: "A consonant cannot have a vowel feature".to_string()
                })
            }
            (Feature::Backness(backness), Phone::Vowel(vowel)) => {
                vowel.backness = backness
            },
            (Feature::Length(length), Phone::Vowel(vowel)) => {
                vowel.length = length
            },
            (Feature::VowelFeature(feature), Phone::Vowel(vowel)) => {
                vowel.features.push(feature)
            },
            (Feature::Height(height), Phone::Vowel(vowel)) => {
                vowel.height = height
            },
        };

        None
    }

    pub fn remove(&mut self, feature : impl Into<Feature> + Clone) {
        if self.has(feature.clone()) {
            return;
        }

        let generalized_feature : Feature = feature.into();
        
        match (generalized_feature, self) {
            (Feature::Voicing(_), Phone::Vowel(vowel)) => {
                vowel.voicing = Default::default()
            }
            (Feature::Voicing(_), Phone::Consonant(cons)) => {
                cons.voicing  = Default::default()
            }
            (Feature::Place(_) 
                | Feature::Manner(_) 
                | Feature::ConsonantFeature(_), Phone::Vowel(_)) => {
                return;
            }
            (Feature::Place(_), Phone::Consonant(cons)) => {
                cons.place = PlaceOfArticulation::Alveolar
            }
            (Feature::Manner(_), Phone::Consonant(cons)) => {
                cons.manner = MannerOfArticulation::Plosive
            }
            (Feature::ConsonantFeature(feature), Phone::Consonant(cons)) => {
                cons.features.retain(|ft| *ft != feature);
            }
            (Feature::Roundness(_), Phone::Vowel(vowel)) => {
                vowel.roundness = Default::default()
            },
            (Feature::Roundness(_) 
                | Feature::Height(_)
                | Feature::Backness(_)
                | Feature::Length(_)
                | Feature::VowelFeature(_), Phone::Consonant(_)) => return,
            (Feature::Height(_), Phone::Vowel(vowel)) => {
                vowel.height = Height::Low
            },
            (Feature::Backness(_), Phone::Vowel(vowel)) => {
                vowel.backness = Backness::Central
            },
            (Feature::Length(_), Phone::Vowel(vowel)) => {
                vowel.length = Default::default()
            },
            (Feature::VowelFeature(feature), Phone::Vowel(vowel)) => {
                vowel.features.retain(|ft| *ft != feature)
            },
        };
    }
}

impl From<Voicing> for Feature {
    fn from(value: Voicing) -> Self {
        Self::Voicing(value)
    }
}

impl From<PlaceOfArticulation> for Feature {
    fn from(place: PlaceOfArticulation) -> Self {
        Self::Place(place)
    }
}

impl From<MannerOfArticulation> for Feature {
    fn from(manner: MannerOfArticulation) -> Self {
        Self::Manner(manner)
    }
}

impl From<ConsonantFeature> for Feature {
    fn from(feature: ConsonantFeature) -> Self {
        Self::ConsonantFeature(feature)
    }
}

impl From<Roundness> for Feature {
    fn from(roundness: Roundness) -> Self {
        Self::Roundness(roundness)
    }
}

impl From<Height> for Feature {
    fn from(height: Height) -> Self {
        Self::Height(height)
    }
}

impl From<Backness> for Feature {
    fn from(backness: Backness) -> Self {
        Self::Backness(backness)
    }
}

impl From<Length> for Feature {
    fn from(length: Length) -> Self {
        Self::Length(length)
    }
}

impl From<VowelFeature> for Feature {
    fn from(feature: VowelFeature) -> Self {
        Self::VowelFeature(feature)
    }
}

