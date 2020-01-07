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
    let n : i32 = get_one();
    let mut ans = "";
    if n <= 59 {
        ans = "Bad";
    } else if n <= 89 {
        ans = "Good";
    } else if n <= 99 {
        ans = "Great";
    } else {
        ans = "Perfect";
    }
    println!("{}", ans);
}
