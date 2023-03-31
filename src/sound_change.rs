use std::marker::PhantomData;

use crate::matchable::Matchable;

// States
pub struct NeedsTarget;
pub struct NeedsResult;

pub struct SoundChangeBuilder<T> {
    phantom : PhantomData<T>,
    data: SoundChangeBuilderData,
}

pub struct SoundChangeBuilderData {
    name : String,
    target: Vec<Matchable>,
}

pub fn sound_change(name : &str) -> SoundChangeBuilder<NeedsTarget> {
    return SoundChangeBuilder { 
        phantom: PhantomData,
        data: SoundChangeBuilderData { 
            name: String::from(name), 
            target: vec![],
        }
    }
}

impl SoundChangeBuilder<NeedsTarget> {
    pub fn target(self : &mut SoundChangeBuilder<NeedsTarget>, target: Vec<Matchable>) -> SoundChangeBuilder<NeedsResult> {
        self.data.target = target;
        return SoundChangeBuilder { 
            phantom: PhantomData, 
            data: self.data,
        }
    }
}