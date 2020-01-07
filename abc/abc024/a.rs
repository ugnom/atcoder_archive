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
    let v : Vec<i32> = get_vec();
    let u : Vec<i32> = get_vec();
    println!("{}", if u[0] + u[1] >= v[3] { (v[0]-v[2]) * u[0] + (v[1] - v[2]) * u[1] } else { v[0]*u[0] + v[1]*u[1] } );
}
