fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let _n : i32 = s.trim().parse().ok().unwrap();
    let mut t = String::new();
    std::io::stdin().read_line(&mut t).ok();
    let k : i32 = t.trim().parse().ok().unwrap();
    let mut u = String::new();
    std::io::stdin().read_line(&mut u).ok();
    let xs : Vec<i32> = u.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();

    let mut ans = 0;
    for x in xs {
        //println!("{}", x);
        ans += std::cmp::min(x,(k-x).abs()) * 2;
    }
    println!("{}", ans);

}
