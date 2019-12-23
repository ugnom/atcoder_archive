fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let x = v[0];
    let y = v[1];
    let z = v[2];

    let ans = (x - z) / (y + z);
    println!("{}", ans);
}
