use std::str::FromStr;
use std::collections::BinaryHeap;

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

    let mut w : Vec<i32> = get_vec();
    w.sort();
    w.reverse();
    let mut heap = BinaryHeap::new();
    for i in 0..n {
        heap.push((w[i] + w[i], i, i));
    }
    let mut ans = 0;
    let mut i = 0;
    while i < m {
        let (v, x, y) = heap.pop().unwrap();
        //println!("{} {} {}",v,x,y);
        if x == y {
            ans += v;
            i += 1;
        }
        else if i + 1 == m {
            ans += v;
            break;
        }
        else {
            ans += 2 * v;
            i += 2;
        }
        if y+1 != n {
            heap.push((w[x] + w[y+1], x, y+1));１２
        }

    }
    println!("{}", ans);
}
