use std::iter;

fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).ok();
    let v : Vec<usize> = s.trim().split_whitespace().map(|e| e.parse().ok().unwrap()).collect();
    let mut mat : Vec<String> = Vec::new();
    let mut ans : Vec<Vec<i32>> = Vec::new();
    let mut ans2 : Vec<String> = Vec::new();
    let h = v[0];
    let w = v[1];

    mat.push(std::iter::repeat(".").take(w+2).collect());
    ans.push(vec![0; w+2]);
    for _i in 0..h {
        let mut t = String::new();
        std::io::stdin().read_line(&mut t).ok();
        let mut pstr = ".".to_string();
        pstr.push_str(&t.trim());
        pstr.push('.');
        //println!("{}", pstr);
        mat.push(pstr);
        ans.push(vec![0; w+2]);
    }
    mat.push(iter::repeat(".").take(w+2).collect());
    ans.push(vec![0; w+2]);

    for i in 1..(h+1) {
        for j in 1..(w+1) {
            if mat[i].chars().nth(j).unwrap() == '#' {
                for k in 0..3 {
                    for l in 0..3 {
                        //println!("{} {} {} {}", k,l,i-1+k, j-1+l);
                        ans[i-1+k][j-1+l] += 1;
                    }
                }
            }
        }
    }
    for i in 1..(h+1) {
        let mut u = String::new();
        for j in 1..(w+1) {
            if mat[i].chars().nth(j).unwrap() == '#' {
                u.push('#');
            }
            else {
                u.push_str(&ans[i][j].to_string());
            }
        }
        ans2.push(u);
    }

    for i in 0..(h) {
        println!("{}", ans2[i]);
    }
}
