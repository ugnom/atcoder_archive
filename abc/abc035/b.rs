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
    let x : i32 = get_one();
    let mut v : i32 = 0;
    let mut h : i32 = 0;
    let mut q : i32 = 0;
    for c in s.chars() {
        match c {
            'L' => h -= 1,
            'R' => h += 1,
            'U' => v += 1,
            'D' => v -= 1,
            _ => q += 1,
        }
    }
    let ans1 = v.abs() + h.abs();
    if x == 1 {
        println!("{}", ans1 + q);
    }
    else {
        println!("{}", if ans1 >= q {ans1 - q} else {(q-ans1) % 2})
    }

}
