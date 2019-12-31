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
