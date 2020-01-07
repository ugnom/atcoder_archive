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
    let n : usize = v[0] as usize;
    let a = v[1];
    let b = v[2];

    let mut ans : i32 = 0;
    for _i in 0..n {
        let u : Vec<String> = get_vec();
        let d = &u[0];
        let x = u[1].parse().ok().unwrap();
        if d == "East" {
            ans += if x < a { a } else { if x > b { b } else { x } };
        }
        else {
            ans -= if x < a { a } else { if x > b { b } else { x } };
        }
    }
    if ans == 0 {
        println!("{}", 0);
    }
    else {
        println!("{} {}", if ans < 0 { "West" } else { "East" }, ans.abs());        
    }
}
