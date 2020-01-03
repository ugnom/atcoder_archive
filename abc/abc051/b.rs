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
    let k = v[0];
    let s = v[1];
    let mut ans = 0;
    for i in 0..(k+1) {
        for j in 0..(k+1) {
            if i + j + k >= s && i + j <= s {
                //println!("{} {}", i, j);
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}
