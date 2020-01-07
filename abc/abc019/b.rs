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
    let s : String = get_one();
    let mut ans = String::new();
    let mut cur = s.chars().nth(0).unwrap();
    let mut cnt = 0;
    for c in s.chars() {
        if c == cur {
            cnt += 1;
        } else {
            ans = format!("{}{}{}", ans, cur, cnt);
            cur = c;
            cnt = 1;
        }
    }
    ans = format!("{}{}{}", ans, cur, cnt);
    println!("{}", ans);
}
