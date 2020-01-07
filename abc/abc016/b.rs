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
    let v : Vec<i32> = get_vec();
    let plus = v[0] + v[1] == v[2];
    let minus = v[0] - v[1] == v[2];
    if plus && minus {
        println!("{}", "?");
    } else if plus {
        println!("{}", "+");
    } else if minus {
        println!("{}", "-");
    } else {
        println!("{}", "!");
    }
}
