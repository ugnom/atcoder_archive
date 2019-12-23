fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let n : usize = s.trim().parse().ok().unwrap();
    let mut v : Vec<i64> = Vec::new();

    v.push(2);
    v.push(1);
    for i in 2..(n+1) {
        let x = v[i-1] + v[i-2];
        v.push(x);
    }
    println!("{}", v[n]);
}
