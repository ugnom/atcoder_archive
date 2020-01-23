fn primes(to : i32) -> Vec<i32> {
    let mut primes : Vec<i32> = Vec::new();
    for i in 2..(to+1) {
        let x = i as f64;
        let xx = x.sqrt().floor() as i32;
        println!("{} {}", i,xx);
        let mut is_prime = true;
        for j in 2..(xx+1) {
            if i % j == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(i);
        }
    }
    return primes;
}

fn prime_factors(n : u64) -> Vec<u64> {
    let mut x = n;
    let mut v = Vec::new();
    let mut i : u64= 2;
    while i.pow(2) <= n {
        while x % i == 0 {
            v.push(i);
            x = x / i;
        }
        i+=1;
    }
    if x != 1 {
        v.push(x);
    }
    return v;
}

fn mod_pow(a : i64, b : i64, mod : i64) -> i64 {
    if b == 0 { return 1; }
    if b % 2 == 0 {
        h = mod_pow(a, b/2, mod);
        return (h * h) % mod;
    }
    else {
        return (a * modpow(a, b-1, mod)) % mod;
    }
}

fn mod_comb(a : i64,b : i64,mod : i64) -> i64 {
    if a-b < b { return mod_comb(a,a-b,mod); }
    let mut ans_mul = 1
    let mut ans_div = 1
    for i in 0..b {
        ans_mul *= a-i;
        ans_div *= i+1;
        ans_mul %= mod;
        ans_div %= mod;
    }
    return (ans_mul * modpow(ans_div, mod-2, mod)) % mod;
}

fn gcd(mut x : u64, mut y : u64) -> u64 {
    while y != 0 {
        let tmp = y;
        y = x % y;
        x = tmp;
    }
    return x;
}

fn lcm(x : u64, y : u64) -> u64 {
    return (x / gcd(x,y)) * y
}
