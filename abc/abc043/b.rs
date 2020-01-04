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
    let s : Vec<char> = get_one::<String>().chars().collect();
    let mut t = String::new();
    for c in s {
        if c == 'B' {
            t.pop();
        }
        else {
            t.push(c);
        }
    }
    println!("{}", t);

}
