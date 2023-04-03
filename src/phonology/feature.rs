

#[derive(Debug, Clone)]
pub enum Feature {
    //Voicing
    Voiced,
    
    // Height
    Close,
    NearClose,
    CloseMid,
    Mid,
    OpenMid,
    Open,

    // Backness
    Front,
    Central,
    Back,

    // Length
    Ultrashort,
    Short,
    Lengthened,
    Long,
    Overlong,

    // Vowel Features
    Rounded,
    Nasalized,
    Stressed,
}


