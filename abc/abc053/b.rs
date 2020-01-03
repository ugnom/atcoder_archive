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
    let s : Vec<char> = get_one::<String>().chars().collect();
    let mut pos_a = None;
    let mut pos_z = None;
    for (i,c) in s.iter().enumerate() {
        if c == &'A' && pos_a == None {
            pos_a = Some(i);
        }
        else if pos_a != None && c == &'Z' {
            pos_z = Some(i);
        }
    }
    println!("{}", pos_z.unwrap() - pos_a.unwrap() + 1);
}
