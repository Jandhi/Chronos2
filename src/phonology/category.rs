pub trait Matches<T> {
    fn matches(&self, t : &T) -> bool;
}