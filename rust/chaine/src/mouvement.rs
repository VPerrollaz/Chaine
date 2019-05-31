#[allow(dead_code)]
#[derive(Copy, Clone)]
pub enum Mouvement {
    Demarrage(u16, u16),
    Voisinage(u16, u16, u16),
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

}
