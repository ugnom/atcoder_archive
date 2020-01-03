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
    let mut abc : Vec<Vec<char>> = Vec::new();
    let a : Vec<char> = get_one::<String>().chars().collect();
    let b : Vec<char> = get_one::<String>().chars().collect();
    let c : Vec<char> = get_one::<String>().chars().collect();
    abc.push(a);
    abc.push(b);
    abc.push(c);
    let mut inds : Vec<usize> = vec!(0;3);
    let mut cur = 0;
    let mut ans = None;
    loop {
        if inds[cur] >= abc[cur].len() {
            ans = Some(cur);
            break;
        }
        //println!("{}", cur);
        let prev = cur;
        let c = abc[cur][inds[cur]];
        if c == 'a' {
            cur = 0;
        } else if c == 'b' {
            cur = 1;
        } else if c == 'c' {
            cur = 2;
        }
        inds[prev] += 1;
    }
    if ans.unwrap() == 0 {
        println!("{}", "A");
    } else if ans.unwrap() == 1 {
        println!("{}", "B");
    } else {
        println!("{}", "C");
    }
}
