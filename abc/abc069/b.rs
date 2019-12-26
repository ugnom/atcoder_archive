use std::str::FromStr;

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
    let n = s.len();
    let s_ind = s.chars().collect::<Vec<char>>();
    println!("{}{}{}", s_ind[0], n-2, s_ind[n-1]);
}