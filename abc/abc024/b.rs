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
    let n = v[0] as usize;
    let t = v[1];
    let mut u : Vec<i32> = Vec::new();
    for _i in 0..n {
        let a : i32 = get_one();
        u.push(a);
    }
    let mut ans : i32 = 0;
    for i in 1..(n) {
        ans += std::cmp::min(t,u[i]-u[i-1]);
    }
    ans += t;
    println!("{}", ans);

}
