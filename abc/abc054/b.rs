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
    let n = v[0];
    let m = v[1];

    let mut im_n : Vec<Vec<char>> = Vec::new();
    for _i in 0..n {
        let l_n : Vec<char> = get_one::<String>().chars().collect();
        im_n.push(l_n);
    }
    let mut im_m : Vec<Vec<char>> = Vec::new();
    for _i in 0..m {
        let l_m : Vec<char> = get_one::<String>().chars().collect();
        im_m.push(l_m);
    }
    let mut ans = false;
    for i in 0..(n-m+1) {
        for j in 0..(n-m+1) {
            let mut is_matched = true;
            for k in 0..m {
                for l in 0..m {
                    if im_n[i+k][j+l] != im_m[k][l] {
                        is_matched = false;
                        break;
                    }
                }
                if !is_matched {break;}
            }
            if is_matched {
                ans = true;
                break;
            }
        }
        if ans {break;}
    }

    println!("{}", if ans {"Yes"} else {"No"});
}
