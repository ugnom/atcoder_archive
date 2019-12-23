fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<String> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    if v[0] < v[1] {
        println!("<");
    }
    else if v[0] > v[1] {
        println!(">");
    }
    else {
        println!("=");
    }
}
