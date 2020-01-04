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
    let mut s : String = get_one();
    let x = s.chars().nth(0).unwrap();
    let mut ans = true;
    for c in s.chars() {
        if x != c {
            ans = false;
        }
    }
    println!("{}", if ans { "SAME" } else { "DIFFERENT" });
}
