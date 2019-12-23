fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let mut x : i32 = 0;
    for c in s.chars() {
        if c == '1' {
            x += 1;
        }
    }
    println!("{}", x);
}
