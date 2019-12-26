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
    let x : i32 = get_one();
    let mut ans = 1;
    let v = [2,4,8,16,32,64];
    for p in v.iter() {
        if x < *p {
            break;
        }
        ans = *p;
    }
    println!("{}", ans);
}
