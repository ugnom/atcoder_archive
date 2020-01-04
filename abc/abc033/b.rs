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
    let mut v : Vec<(String, i32)> = Vec::new();
    let mut sm : i32 = 0;
    for i in 0..n {
        let w : Vec<String> = get_vec();
        let s : String = w[0].to_string();
        let x : i32 = w[1].parse().ok().unwrap();
        v.push((s,x));
        sm += x;
    }
    let mut ans = "atcoder".to_string();
    for (s, x) in v {
        if x*2 > sm {
            ans = s;
            break;
        }
    }
    println!("{}", ans);
}
