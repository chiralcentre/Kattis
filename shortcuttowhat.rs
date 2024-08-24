use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let mut n: i64 = input.trim().parse().expect("a valid number");
    n = (n + 5) * 3 - 10;
    println!("{}", n);
}