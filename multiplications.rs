use std::io;

const MOD: i64 = i64::pow(10, 9) + 7;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let N: i64 = input.trim().parse().expect("a valid number");
    let mut prod: i64 = 1;
    for i in 0..N {
        input.clear();
        io::stdin().read_line(&mut input).expect("a string");
        let mut a: i64 = input.trim().parse().expect("a valid number");
        a %= MOD;
        prod *= a;
        prod %= MOD;
    }
    println!("{}", prod);
}