fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();

    let x = v[0];
    let a = v[1];
    let b = v[2];

    if (a-x).abs() > (b-x).abs() {
        println!("B");
    }
    else {
        println!("A");
    }

}