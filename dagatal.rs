use std::io;
use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let m: i64 = input.trim().parse().expect("a valid number");
    let days: HashMap<i64, i64> = HashMap::from([
        (1, 31), (2, 28), (3, 31), (4, 30),
        (5, 31), (6, 30), (7, 31), (8, 31),
        (9, 30), (10, 31), (11, 30), (12, 31)
    ]);
    println!("{}", days[&m]);
}