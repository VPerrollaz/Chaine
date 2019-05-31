use super::graphe::Graphe;

#[allow(dead_code)]
fn glouton(gr: Graphe) -> Vec<u16> {
    let mut fin: bool = false;
    let mut courant: &u16 = &gr.demarrage;
    let mut chaine: Vec<u16> = Vec::new();
    chaine.push(*courant);
    while !fin {
        fin = true;
        for nombre in gr.voisinage[courant].iter() {
            if !chaine.contains(&nombre) {
                courant = &nombre;
                chaine.push(*courant);
                fin = false;
                break;
            }
        }
    }
    chaine
}

#[cfg(test)]
mod tests {
    use super::super::mouvement::Mouvement;
    use super::{glouton, Graphe};

    #[test]
    fn glouton_simple_test() {
        let gr = Graphe::new(8u16);
        let resultat = glouton(gr);
        assert_eq!(resultat, vec![1, 2, 4, 8]);
    }

    #[test]
    fn glouton_test() {
        let mut gr = Graphe::new(3u16);
        let mouv = Mouvement::Voisinage(1, 2, 3);
        gr.modification(mouv);
        assert_eq!(glouton(gr), vec![1, 3]);
    }
}
