use std::str::FromStr;
use std::cmp::max;
use std::cmp::min;

fn get_vec<T : FromStr>() -> Vec<T> {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
}

fn main() {
    let v : Vec<i32> = get_vec();
    println!("{}", max(0,min(v[1],v[3]) - max(v[0],v[2])));

}