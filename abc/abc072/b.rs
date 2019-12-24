use std::str::FromStr;

fn get_one<T : FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().parse().ok().unwrap();
}

fn main() {
    let s : String = get_one();
    let mut t = "".to_string();
    for (i, x) in s.chars().enumerate() {
        if i % 2 == 0 {
            t.push(x);
        }
    }
    println!("{}", t);
}
