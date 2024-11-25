use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let mut N: i64 = input.trim().parse().expect("a valid number");
    println!("{} ml gin", N * 45);
    println!("{} ml fresh lemon juice", N * 30);
    println!("{} ml simple syrup", N * 10);
    if N == 1 { println!("1 slice of lemon"); }
    else { println!("{} slices of lemon", N); }
}