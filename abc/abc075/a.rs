fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let mut ans = 0;
    if v[0] == v[1] {
        ans = v[2];
    }
    else if v[1] == v[2] {
        ans = v[0];
    }
    else {
        ans = v[1];
    }
    println!("{}", ans);
}
