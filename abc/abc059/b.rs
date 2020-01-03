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
    let t : String = get_one();

    let ss : Vec<char> = s.chars().rev().collect();
    let tt : Vec<char> = t.chars().rev().collect();

    if ss.len() > tt.len() {
        println!("{}", "GREATER");
    }
    else if ss.len() < tt.len() {
        println!("{}", "LESS");
    }
    else {
        let n = std::cmp::min(ss.len(), tt.len());
        let mut prev_greater = 0;
        for i in 0..n {
            if ss[i] > tt[i] {
                prev_greater = 1;
            }
            else if ss[i] < tt[i] {
                prev_greater = -1;
            }
        }
        if prev_greater == 0 {
            println!("{}", "EQUAL");
        }
        else if prev_greater == 1 {
            println!("{}", "GREATER");
        }
        else {
            println!("{}", "LESS");
        }
    }
}
