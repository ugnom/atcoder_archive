use std::str::FromStr;
use std::cmp::max;
use std::cmp::min;

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
    let n : i32 = get_one();
    let k : i32 = get_one();
    let x : i32 = get_one();
    let y : i32 = get_one();
    println!("{}", min(k, n) * x + max(0, n-k) * y);
}
