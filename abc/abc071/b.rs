use std::str::FromStr;
use std::collections::HashSet;

fn get_one<T : FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().parse().ok().unwrap();
}

fn main() {
    let s : String = get_one();
    let mut set : HashSet<char> = HashSet::new();
    for c in s.chars() {
        set.insert(c);
    }
    let t = "abcdefghijklmnopqrstuvwxyz".to_string();
    let mut ans = None;
    for c in t.chars() {
        if !set.contains(&c) {
            ans = Some(c);
            break;
        }
    }
    match ans {
        None => println!("{}", "None"),
        Some(x) => println!("{}", x),
    }
}
