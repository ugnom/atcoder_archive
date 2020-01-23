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

fn get_vec_by_lines<T : FromStr>(n : usize) -> Vec<T> {
    let mut v : Vec<T> = Vec::new();
    for _i in 0..n {
        let x : T = get_one();
        v.push(x);
    }
    return v;
}

fn main() {
    let s = get_one();
    let ans = s;
    println!("{}", ans);
}
