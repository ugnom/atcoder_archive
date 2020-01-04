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
    let l = v[0];
    let h = v[1];
    let n : usize = get_one();
    let mut v : Vec<i32> = Vec::new();
    for _i in 0..n {
        let x : i32 = get_one();
        v.push(x);
    }
    for x in v {
        println!("{}", if x > h { -1 } else { std::cmp::max(0, l - x) });
    }
}
