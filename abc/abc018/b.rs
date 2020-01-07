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
    let mut w : Vec<char> = get_one::<String>().chars().collect();
    let n : i32 = get_one();

    for i in 0..n {
        let v : Vec<usize> = get_vec();
        let l = v[0]-1;
        let r = v[1]-1;
        let mut tmp = vec!(' ' ;r-l+1);
        tmp.copy_from_slice(&w[l..r+1]);
        tmp.reverse();
        for j in 0..tmp.len() {
            w[l+j] = tmp[j];
        }
    }

    let ans = w.iter().collect::<String>();
    println!("{}", ans);
}
