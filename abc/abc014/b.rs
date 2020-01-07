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
    let mut x = v[1];
    let a : Vec<i32> = get_vec();
    let mut i = 0;
    let mut ans = 0;
    while x > 0 {
        //println!("{} {} {} ", i, x, x&1);
        if x & 1 == 1 {
            ans += a[i]
        }
        i += 1;
        x >>= 1;
    }
    println!("{}", ans);
}
