fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let n : i32 = s.trim().parse().ok().unwrap();

    let mut k = 0;
    let mut ans = 1;
    while k*k <= n {
        ans = k*k;
        k += 1;
    }
    println!("{}", ans);
}
