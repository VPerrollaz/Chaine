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
    dernier: Option<Mouvement>,
}

impl Graphe {
    #[allow(dead_code)]
    fn new(n: u16) -> Graphe {
        let mut demarrage: Vec<u16> = Vec::new();
        for i in 1..=n {
            demarrage.push(i);
        }
        let mut voisinage: HashMap<u16, Vec<u16>> = HashMap::new();
        for i in 1..=n {
            let mut temp: Vec<u16> = Vec::new();
            for j in 1..=n {
                if (i % j == 0) || (j % i == 0) {
                    temp.push(j);
                }
            }
            voisinage.insert(i, temp);
        }
        let mut admissibles: Vec<u16> = Vec::new();
        for (i, voisins) in &voisinage {
            if voisins.len() > 1 {
                admissibles.push(i.clone());
            }
        }
        let dernier: Option<Mouvement> = None;
        Graphe {
            demarrage,
            voisinage,
            admissibles,
            dernier,
        }
    }
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

    #[test]
    fn creation_graphe_test() {
        let g = Graphe::new(5u16);
    }
}
