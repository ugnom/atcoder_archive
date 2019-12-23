fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    if s.chars().nth(0).unwrap() == '9' || s.chars().nth(1).unwrap() == '9' {
        println!("Yes");
    }
    else {
        println!("No");
    }
}
