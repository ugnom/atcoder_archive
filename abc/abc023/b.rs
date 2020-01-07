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
    let n : usize = get_one();
    let v = get_one::<String>();
    let s : Vec<char> = "abc".to_string().chars().collect();
    let mut cur = (4 - (n/2 % 3)) % 3;

    let mut ss : String = String::new();
    for _i in 0..(n) {
        ss.push(s[cur]);
        cur = (cur + 1) % 3;
    }
    if n % 2 == 1 && ss == v {
        println!("{}", n / 2);
    } else {
        println!("{}", -1);
    }

}
