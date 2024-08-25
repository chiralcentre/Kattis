use std::io;

const HOUR_THRESHOLD: i64 = 3600;
const MIN_THRESHOLD: i64 = 60;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let mut s: i64 = input.trim().parse().expect("a valid number");
    let h: i64 = s / HOUR_THRESHOLD;
    s %= HOUR_THRESHOLD;
    let m: i64 = s / MIN_THRESHOLD;
    s %= MIN_THRESHOLD;
    println!("{} : {} : {}", h, m, s);
}