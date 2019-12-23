fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let n : i32 = s.trim().parse().ok().unwrap();
    let mut ans : i32 = 0;
    for _i in 0..n {
        let mut t = String::new();
        std::io::stdin().read_line(&mut t).ok();
        let v : Vec<i32> = t.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
        ans += v[1] - v[0] + 1;
    }
    println!("{}", ans);
}
