extern crate rand;

use rand::prelude::*;
use std::collections::HashMap;

#[allow(dead_code)]
#[derive(Copy, Clone)]
enum Mouvement {
    Demarrage(u16, u16),
    Voisinage(u16, u16, u16),
}

#[allow(dead_code)]
pub struct Graphe {
    pub demarrage: u16,
    pub voisinage: HashMap<u16, Vec<u16>>,
    admissibles: Vec<u16>,
    dernier: Option<Mouvement>,
    generateur: ThreadRng,
}

#[allow(dead_code)]
fn echange(liste: &mut Vec<u16>, b: u16, c: u16) {
    for i in 0..liste.len() {
        if liste[i] == c {
            liste[i] = b;
        } else if liste[i] == b {
            liste[i] = c;
        }
    }
}

impl Graphe {
    #[allow(dead_code)]
    pub fn new(n: u16) -> Graphe {
        let demarrage: u16 = 1;
        let mut voisinage: HashMap<u16, Vec<u16>> = HashMap::new();
        for i in 1..=n {
            let mut temp: Vec<u16> = Vec::new();
            for j in 1..=n {
                if (i != j) && ((i % j == 0) || (j % i == 0)) {
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
        let generateur: ThreadRng = thread_rng();
        Graphe {
            demarrage,
            voisinage,
            admissibles,
            dernier,
            generateur,
        }
    }

    #[allow(dead_code)]
    fn modification(&mut self, m: Mouvement) {
        match m {
            Mouvement::Demarrage(a, b) => {
                if self.demarrage == a {
                    self.demarrage = b;
                } else if self.demarrage == b {
                    self.demarrage = a;
                } else {
                    panic!("Aucun des deux entiers ne correspond au démarrage");
                }
            }
            Mouvement::Voisinage(a, b, c) => echange(self.voisinage.get_mut(&a).unwrap(), b, c),
        }
        self.dernier = Some(m);
    }
    #[allow(dead_code)]
    fn inversion(&mut self) {
        match self.dernier {
            Some(m) => {
                self.modification(m);
                self.dernier = None;
            }
            None => panic!("Pas de dernier mouvement à inverser."),
        }
    }

    #[allow(dead_code)]
    fn mutation(&mut self) {
        let mouv: Mouvement = if self.generateur.gen::<f64>() < 0.1 {
            Mouvement::Demarrage(
                self.demarrage,
                (1..101).choose(&mut self.generateur).unwrap(),
            )
        } else {
            let entier: &u16 = self.admissibles.choose(&mut self.generateur).unwrap();
            let choix = self.voisinage[entier]
                .iter()
                .choose_multiple(&mut self.generateur, 2);
            Mouvement::Voisinage(*entier, *choix[0], *choix[1])
        };
        self.modification(mouv);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn creation_mouvement_test() {
        let _d: Mouvement = Mouvement::Demarrage(1, 2);
        let _v: Mouvement = Mouvement::Voisinage(1, 2, 3);
    }

    #[test]
    fn pattern_mouvement_test() {
        let d: Mouvement = Mouvement::Demarrage(1, 2);
        let v: Mouvement = Mouvement::Voisinage(1, 2, 3);
        match d {
            Mouvement::Demarrage(a, _b) => assert_eq!(a, 1u16),
            _ => panic!("Problème"),
        }
        match v {
            Mouvement::Voisinage(a, _b, _c) => assert_eq!(a, 1u16),
            _ => panic!("Oups"),
        }
    }

    #[test]
    fn echange_test() {
        let mut liste: Vec<u16> = Vec::new();
        liste.append(&mut vec![1, 2, 3]);
        assert_eq!(liste[0], 1);
        assert_eq!(liste[1], 2);
        echange(&mut liste, 1, 2);
        assert_eq!(liste[0], 2);
        assert_eq!(liste[1], 1);
    }

    #[test]
    fn creation_graphe_test() {
        let g = Graphe::new(3u16);
        assert_eq!(g.demarrage, 1);
        assert_eq!(g.voisinage.get(&1).unwrap(), &vec![2u16, 3]);
    }

    #[test]
    fn modification_graphe_test() {
        let mut g = Graphe::new(3u16);
        let md = Mouvement::Demarrage(1, 2);
        let mv = Mouvement::Voisinage(1, 2, 3);
        g.modification(md);
        assert_eq!(g.demarrage, 2);
        g.modification(md);
        assert_eq!(g.demarrage, 1);
        g.modification(mv);
        assert_eq!(g.voisinage.get(&1).unwrap(), &vec![3, 2u16]);
    }

    #[test]
    fn inversion_graphe_test() {
        let mut g = Graphe::new(3u16);
        let md = Mouvement::Demarrage(1, 2);
        g.modification(md);
        g.inversion();
        assert_eq!(g.demarrage, 1);
    }

    #[test]
    fn mutation_graphe_test() {
        let mut g = Graphe::new(3u16);
        g.mutation();
    }
}
