fn main(){
    let mut x = String::new();
    std::io::stdin().read_line(&mut x).ok();
    let n : usize = x.trim().parse().ok().unwrap();
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let mut v : Vec<i32> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let mut ans : i32 = 0;
    loop {
        let mut dividable = true;
        for i in 0..n {
            if v[i] % 2 != 0 {
                dividable = false;
                break;
            }
            v[i] /= 2;
        }
        if !dividable {
            break;
        }
        ans += 1;
    }
    println!("{}", ans);
}
