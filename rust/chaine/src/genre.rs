pub enum Genre {
    Demarrage(u16, u16),
    Voisinage(u16, u16, u16),
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn creation_genre_test() {
        let d: Genre = Genre::Demarrage(1, 2);
        let v: Genre = Genre::Voisinage(1, 2, 3);
    }

    #[test]
    fn pattern_test() {
        let d: Genre = Genre::Demarrage(1, 2);
        let v: Genre = Genre::Voisinage(1, 2, 3);
        match d {
            Genre::Demarrage(a, b) => assert_eq!(a, 1u16),
            _ => panic!("Problème"),
        }
        match v {
            Genre::Voisinage(a, b, c) => assert_eq!(a, 1u16),
            _ => panic!("Oups"),
        }
    }
}
