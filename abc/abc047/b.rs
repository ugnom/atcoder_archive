use std::str::FromStr;
use std::cmp::max;
use std::cmp::min;

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
    let w : i32 = v[0];
    let h : i32 = v[1];
    let n = v[2] as usize;

    let mut l : i32 = 0;
    let mut r : i32 = w;
    let mut u : i32 = h;
    let mut d : i32 = 0;
    for _i in 0..n {
        let v2 : Vec<i32> = get_vec();
        if v2[2] == 1 {
            l = max(l, v2[0]);
        }
        else if v2[2] == 2 {
            r = min(r, v2[0]);
        }
        else if v2[2] == 3 {
            d = max(d, v2[1]);
        }
        else if v2[2] == 4 {
            u = min(u, v2[1]);
        }
    }

    //println!("{} {} {} {}", u, d, r, l);
    if l >= r || u <= d {
        println!("{}", 0);
    }
    else {
        println!("{}", (u-d) * (r-l))
    }
}
