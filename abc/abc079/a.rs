fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    if  s.chars().nth(0) == s.chars().nth(1) && s.chars().nth(1) == s.chars().nth(2) ||
        s.chars().nth(1) == s.chars().nth(2) && s.chars().nth(2) == s.chars().nth(3) {
        println!("Yes");
    }
    else {
        println!("No");
    }

}
