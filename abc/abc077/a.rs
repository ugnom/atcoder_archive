fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let mut t = String::new();
    std::io::stdin().read_line(&mut t).ok();

    let mut ans = true;
    for i in 0..3 {
        if s.chars().nth(i) != t.chars().nth(2-i) {
            ans = false;
            break;
        }
    }
    if ans {
        println!("YES");
    }
    else {
        println!("NO");
    }
}
