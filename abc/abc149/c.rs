fn find_prime(frm : i32) -> i32 {
    let mut prime = 0;
    let mut i = frm;
    loop {
        let x = i as f64;
        let xx = x.sqrt().floor() as i32;
        //println!("{} {}", i,xx);
        let mut is_prime = true;
        for j in 2..(xx+1) {
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            prime = i;
            break;
        }
        i += 1;
    }
    return prime;
}

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
    let p = find_prime(n);
    println!("{}", p);
}
