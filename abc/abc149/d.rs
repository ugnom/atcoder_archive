use std::str::FromStr;
use std::collections::HashMap;

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
    let k = v[1];
    let w : Vec<i32> = get_vec();
    let mut score : HashMap<char,i32> = HashMap::new();
    score.insert('s', w[0]);
    score.insert('p', w[1]);
    score.insert('r', w[2]);
    let rsp : String = get_one();
    let rsp_i : Vec<char> = rsp.chars().collect();
    let mut ans = 0;
    for i in 0..k {
        let mut j = 0;
        let mut prev = rsp_i[i];
        let mut same_cnt = 0;
        while j*k+i < n {
            //println!("{} {} {}", i, j, j*k+i);
            let cur = rsp_i[j*k+i];
            //println!("{} {} {} {}", prev, cur, same_cnt, ans);
            if cur == prev {
                same_cnt += 1;
            }
            else {
                ans += ((same_cnt+1) / 2) * score[&prev];
                same_cnt = 1;
            }
            prev = cur;
            j+=1;
        }
        ans += ((same_cnt + 1) / 2) * score[&prev];
    }
    println!("{}", ans);
}
