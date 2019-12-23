fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i64> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let mut x = v[0];
    let y = v[1];

    let mut ans = 0;
    while x <= y {
        ans += 1;
        x *= 2;
    }
    println!("{}", ans);
}
