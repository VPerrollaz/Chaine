mod mouvement;

use genre::Genre;
use std::collections::HashMap;

pub struct Graphe {
    demarrage: Vec<u16>,
    voisinage: HashMap<u16, Vec<u16>>,
    admissibles: Vec<u16>,
    dernier: Genre,
}

#[cfg(test)]
mod tests {
    #[test]
    fn verification_test() {
        ()
    }
}
