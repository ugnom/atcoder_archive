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
    let v : Vec<usize> = get_vec();
    let n = v[0];
    let q = v[1];

    let mut u : Vec<usize> = vec!(0;n);
    for _i in 0..q {
        let w : Vec<usize> = get_vec();
        for j in (w[0]-1)..w[1] {
            u[j] = w[2];
        }
    }
    for x in u {
        println!("{}", x);
    }
}
