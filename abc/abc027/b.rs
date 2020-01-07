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
    let v : Vec<i32> = get_vec();
    let sm = v.iter().fold(0, |sum, e| sum + e);
    if sm % (v.len() as i32) != 0 {
        println!("{}", -1);
    }
    else {
        let ave = sm / (n as i32);
        let mut ans = 0;
        let mut sum_so_far = 0;
        let mut i = 1;
        for x in v {
            sum_so_far += x;
            if sum_so_far == ave * i {
                sum_so_far = 0;
                i = 1;
            }
            else {
                i += 1;
                ans += 1;
            }
        }
        println!("{}", ans);
    }
}
