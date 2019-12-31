use std::str::FromStr;

fn get_one<T : FromStr>() -> T {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().parse().ok().unwrap();
}

fn get_vec<T : FromStr>() -> Vec<T> {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    return s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
}

fn main() {
    let s : String = get_one();
    let si : Vec<char> = s.chars().collect();
    let mut ans = 0;
    for i in 1..(s.len() / 2) {
        let mut is_even = true;
        for j in 0..i {
            if si[j] != si[i+j] {
                is_even = false;
                break;
            }
        }
        if is_even {
            ans = i;
        }
    }
    println!("{}", ans*2);
}
