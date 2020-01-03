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
    let v : Vec<String> = get_vec();
    let a : i32 = v[0].parse().ok().unwrap();
    let b : i32 = v[2].parse().ok().unwrap();
    println!("{}", if v[1] == "+" { a+b } else { a-b });

}
