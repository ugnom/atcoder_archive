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
    let v : Vec<i32> = get_vec();
    let n = v[0];
    let s = v[1];
    let t = v[2];
    let mut cur = 0;
    let mut ans = 0;
    for _i in 0..n {
        let x : i32 = get_one();
        cur += x;
        if s <= cur && cur <= t {
            ans += 1;
        }
    }
    println!("{}", ans);
}
