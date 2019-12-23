fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let n = v[0];
    let a = v[1];
    let b = v[2];
    //println!("{} {} {}", n, a, b);
    let mut ans = 0;
    for x in 0..(n+1) {
        let mut y = x;
        let mut k = 0;
        while y > 0 {
            k += y % 10;
            y /= 10;
        }
        if a <= k && k <= b {
            ans += x;
        }
    }
    println!("{}", ans);
}
