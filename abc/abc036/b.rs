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
    let mut mat : Vec<Vec<char>> = Vec::new();
    for _i in 0..n {
        let s : Vec<char> = get_one::<String>().chars().collect();
        mat.push(s);
    }
    let mut t : Vec<String> = Vec::new();
    for i in 0..n {
        let mut s = String::new();
        for j in 0..n {
            s.push(mat[n-j-1][i])
        }
        t.push(s);
    }
    for s in t {
        println!("{}", s);
    }
}
