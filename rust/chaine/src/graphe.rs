enum Genre {
    Demarrage(u16, u16),
    Voisinage(u16, u16, u16),
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_genre() {
        let d: Genre = Genre::Demarrage(1, 2);
        let v: Genre = Genre::Voisinage(1, 2, 3);
    }
