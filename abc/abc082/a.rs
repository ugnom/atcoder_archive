
fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<f32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let ans = f32::ceil((v[0] + v[1]) / 2.0 );

    println!("{}", ans);
}
