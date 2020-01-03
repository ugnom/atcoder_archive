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
    let mut v : Vec<i32> = get_vec();
    if v[0] == 1 { v[0] = 14; }
    if v[1] == 1 { v[1] = 14; }
    let mut ans = "Draw";
    if v[0] > v[1]{
        ans = "Alice";
    }
    else if v[0] < v[1] {
        ans = "Bob";
    }
    println!("{}", ans);
}
