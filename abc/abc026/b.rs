use std::str::FromStr;
use std::f64::consts::PI;

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
    let n : usize = get_one();
    let mut v : Vec<i32> = Vec::new();
    for _i in 0..n {
        let x : i32 = get_one();
        v.push(x);
    }
    v.sort();
    v.reverse();
    let mut ans = 0;
    for (i,x) in v.iter().enumerate() {
        if i % 2 == 0 {
            ans += x.pow(2);
        }
        else {
            ans -= x.pow(2);
        }
    }
    println!("{}", (ans as f64) * PI );
}
