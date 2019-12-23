fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let n : i32 = s.trim().parse().ok().unwrap();
    let mut t = String::new();
    std::io::stdin().read_line(&mut t).ok();
    let k : i32 = t.trim().parse().ok().unwrap();

    let mut ans = 1;
    for _i in 0..n {
        if ans < k {
            ans *= 2;
        }
        else {
            ans += k;
        }
    }
    println!("{}", ans);

}
