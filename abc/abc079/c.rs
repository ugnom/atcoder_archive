fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let mut v : Vec<i32> = Vec::new();
    for i in 0..4 {
        v.push(s.chars().nth(i).unwrap().to_digit(10).unwrap_or(0) as i32);
    }
    let mut end = false;
    for f1 in 0..2 {
        for f2 in 0..2 {
            for f3 in 0..2 {
                let mut ans = v[0];
                if f1 == 0 {
                    ans += v[1];
                }
                else {
                    ans -= v[1];
                }
                if f2 == 0 {
                    ans += v[2];
                }
                else {
                    ans -= v[2];
                }
                if f3 == 0 {
                    ans += v[3];
                }
                else {
                    ans -= v[3];
                }
                if ans == 7 {
                    println!("{}{}{}{}{}{}{}=7", v[0], if f1==0 {'+'} else {'-'}, v[1], if f2==0 {"+"} else {"-"}, v[2], if f3==0 {"+"}  else {"-"}, v[3]);
                    end = true;
                    break;
                }
            }
            if end {
                break;
            }
        }
        if end {
            break;
        }
    }
}
