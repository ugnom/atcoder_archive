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

use std::cmp::max;
use std::cmp::min;
fn main() {
    let v : Vec<i32> = get_vec();
    println!("{}", max(0, max(v[1],v[2]) - (min(v[1],v[2]) + v[0])))
}
