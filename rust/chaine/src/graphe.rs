use std::collections::HashMap;

#[allow(dead_code)]
pub enum Mouvement {
    Demarrage(u16, u16),
    Voisinage(u16, u16, u16),
}

#[allow(dead_code)]
pub struct Graphe {
    demarrage: Vec<u16>,
    voisinage: HashMap<u16, Vec<u16>>,
    admissibles: Vec<u16>,
    dernier: Mouvement,
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn creation_mouvement_test() {
        let d: Mouvement = Mouvement::Demarrage(1, 2);
        let v: Mouvement = Mouvement::Voisinage(1, 2, 3);
    }

    #[test]
    fn pattern_mouvement_test() {
        let d: Mouvement = Mouvement::Demarrage(1, 2);
        let v: Mouvement = Mouvement::Voisinage(1, 2, 3);
        match d {
            Mouvement::Demarrage(a, b) => assert_eq!(a, 1u16),
            _ => panic!("Problème"),
        }
        match v {
            Mouvement::Voisinage(a, b, c) => assert_eq!(a, 1u16),
            _ => panic!("Oups"),
        }
    }
}
