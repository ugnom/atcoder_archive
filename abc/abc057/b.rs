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
    let mut stu = Vec::new();
    for _i in 0..v[0] {
        let xs : Vec<i32> = get_vec();
        stu.push((xs[0], xs[1]));
    }
    let mut cps = Vec::new();
    for _i in 0..v[1] {
        let xs : Vec<i32> = get_vec();
        cps.push((xs[0], xs[1]));
    }
    for j in 0..v[0] {
        let (sx, sy) = stu[j];
        let mut min_d = i32::max_value();
        let mut min_i = 0;
        for i in 0..v[1] {
            let (cx, cy) = cps[i];
            let d = (sx - cx).abs() + (sy - cy).abs();
            if min_d > d {
                min_d = d;
                min_i = i
            }
        }
        println!("{}", min_i+1);
    }

}
