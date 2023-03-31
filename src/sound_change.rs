use std::marker::PhantomData;

pub struct NeedsTarget;
pub struct NeedsResult;

pub struct SoundChangeBuilder<T> {
    phantom : PhantomData<T>
}

pub fn SoundChange() -> SoundChangeBuilder<NeedsTarget> {
    return SoundChangeBuilder { phantom: PhantomData }
}

impl SoundChangeBuilder<NeedsTarget> {
    pub fn AddTarget(self : &SoundChangeBuilder<NeedsTarget>) -> SoundChangeBuilder<NeedsResult> {
        return SoundChangeBuilder { phantom: PhantomData }
    }
}