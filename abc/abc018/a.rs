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
    let a : i32 = get_one();
    let b : i32 = get_one();
    let c : i32 = get_one();
    let ra = if a > b && a > c { 1 } else { if a < b && a < c { 3 } else { 2 }};
    let rb = if b > a && b > c { 1 } else { if b < a && b < c { 3 } else { 2 }};
    let rc = if c > b && c > a { 1 } else { if c < b && c < a { 3 } else { 2 }};
    println!("{}", ra);
    println!("{}", rb);
    println!("{}", rc);
}
