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
    let h : usize = v[0];
    let _w : usize = v[1];
    let mut im : Vec<String> = Vec::new();
    for _i in 0..h {
        let s : String = get_one();
        im.push(s);
    }

    for s in im {
        println!("{}", s);
        println!("{}", s);
    }
}
