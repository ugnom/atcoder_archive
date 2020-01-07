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
    let s : Vec<char> = get_one::<String>().chars().collect();
    let mut prev_c = false;
    let mut ans = true;
    for c in s {
        //println!("{}", c);
        if prev_c {
            if c != 'h' {
                ans = false;
            }
            prev_c = false;
        } else if c == 'c' {
            prev_c = true;
        } else if c != 'o' && c != 'k' && c != 'u' {
            ans = false;
        }
        if ans == false {
            break;
        }
    }
    println!("{}", if ans { "YES" } else { "NO" });
}
