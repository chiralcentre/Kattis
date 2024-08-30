use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("a string");
    let a: i64 = input.trim().parse().expect("a valid number");
    input.clear();
    io::stdin().read_line(&mut input).expect("a string");
    let b: i64 = input.trim().parse().expect("a valid number");
    if a < b  { println!("FAKE NEWS!"); }
    else if a > b { println!("MAGA!"); }
    else { println!("WORLD WAR 3!"); }
}