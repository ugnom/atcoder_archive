fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let ans = std::cmp::min(v[0] * v[1], v[2]);
    println!("{}", ans);
}
