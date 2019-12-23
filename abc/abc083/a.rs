fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let x = v[0] + v[1];
    let y = v[2] + v[3];
    if x > y {
        println!("Left");
    }
    else if x == y {
        println!("Balanced");
    }
    else {
        println!("Right");
    }
}
