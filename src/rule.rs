use std::marker::PhantomData;

use crate::matchable::Matchable;

pub struct Rule {
    target : Vec<Matchable>,
}

// States
pub struct NeedsTarget;
pub struct NeedsResult;


pub struct RuleBuilder<T> {
    phantom_state : PhantomData<T>,
    rule : Rule,
}

pub fn build_rule() -> RuleBuilder<NeedsTarget> {
    return RuleBuilder {
        phantom_state: PhantomData, 
        rule: Rule {
            target: vec![],
        } 
    }
}

impl RuleBuilder<NeedsTarget> {
    pub fn target(self : RuleBuilder<NeedsTarget>, target: &[Matchable]) -> RuleBuilder<NeedsResult> {
        let mut rule = self.rule;
        rule.target = target.to_vec();

        return RuleBuilder { 
            phantom_state: PhantomData, 
            rule: rule,
        }
    }
}
