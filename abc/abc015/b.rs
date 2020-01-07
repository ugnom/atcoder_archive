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
    let n : i32 = get_one();
    let v : Vec<i32> = get_vec();

    let sm = v.iter().fold(0 as i32, |s, x| s+x) as f64;
    let cnt = v.iter().fold(0 as i32, |c, x| if x != &(0 as i32) {c+1} else {c} ) as f64;

    println!("{}", (sm/cnt).ceil());
}
