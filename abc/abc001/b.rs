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
    let v : Vec<f64> = get_vec();
    let n = if v[0] > 12.0 { v[0]-12.0 } else { v[0] };
    let m = v[1];
    let l = ((m / 60.0) * 360.0);
    let s = ((n / 12.0) * 360.0 + (m/60.0) * (360.0/12.0)) ;
    //println!("{} {}", l, s);
    let mut ans = (l-s).abs();
    ans = if ans > 180.0 { 360.0 - ans } else { ans };
    println!("{}", ans);
}
