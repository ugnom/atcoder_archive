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
    let _n : usize = get_one();
    let s : Vec<char> = get_one::<String>().chars().collect();
    let mut ans = 0;
    let mut max_a = 0;
    for c in s {
        if c == 'I' {
            ans += 1;
        }
        else {
            ans -= 1;
        }
        max_a = std::cmp::max(max_a, ans);
    }
    println!("{}", max_a);
}
