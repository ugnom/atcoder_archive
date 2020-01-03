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
    let _n : usize = get_one();
    let t : Vec<i32> = get_vec();
    let sm = t.iter().fold(0, |s, a| s + a);
    let m : usize = get_one();
    let mut pxs = Vec::new();
    for _i in 0..m {
        let px = get_vec::<i32>();
        let p = px[0] as usize;
        let x = px[1];
        pxs.push((p,x));
    }
    for (p,x) in pxs {
        println!("{}", sm - t[p-1] + x);
    }
}
