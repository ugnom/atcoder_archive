use std::str::FromStr;
use std::collections::HashMap;

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
    let mut m : HashMap<char, i32>= HashMap::new();
    for c in s {
        let cnt = m.entry(c).or_insert(0);
        *cnt += 1;
    }
    let mut ans = true;
    for (_k,v) in &m {
        if v % 2 != 0 {
            ans = false;
            break;
        }
    }
    println!("{}", if ans {"Yes"} else {"No"});

}
