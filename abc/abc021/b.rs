use std::str::FromStr;
use std::collections::HashSet;

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
    let ab : Vec<i32>  = get_vec();
    let a = ab[0];
    let b = ab[1];
    let k : i32 = get_one();
    let p : Vec<i32> = get_vec();
    let mut set : HashSet<i32> = HashSet::new();
    set.insert(a);
    set.insert(b);
    let mut ans = true;
    for pi in p {
        if set.contains(&pi) {
            ans = false;
            break;
        }
        set.insert(pi);
    }
    println!("{}", if ans {"YES"} else {"NO"});
}
