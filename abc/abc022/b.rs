use std::str::FromStr;
use std::collections::HashSet;

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
    let mut set : HashSet<i32> = HashSet::new();
    let ans = 0;
    for _i in 0..n {
        let x : i32 = get_one();
        if set.contains(&x) {
            ans += 1;
        }
        else {
            set.insert(x);
        }
    }
    println!("{}", ans);
}
