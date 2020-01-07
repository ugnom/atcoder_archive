use std::str::FromStr;
use std::collections::HashMap;

fn get_one<T : FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().parse().ok().unwrap();
}

fn get_vec<T : FromStr>() -> Vec<T> {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
}

fn main() {
    let s : String = get_one();
    let t : String = "ABCDEF".to_string();
    let mut hmap : HashMap<char, i32> = HashMap::new();
    for c in t.chars() {
        hmap.entry(c).or_insert(0);
    }
    for c in s.chars() {
        let e = hmap.entry(c).or_insert(0);
        *e += 1;
    }

    println!("{} {} {} {} {} {}",
        hmap.get(&'A').unwrap(),
        hmap.get(&'B').unwrap(),
        hmap.get(&'C').unwrap(),
        hmap.get(&'D').unwrap(),
        hmap.get(&'E').unwrap(),
        hmap.get(&'F').unwrap());
}
