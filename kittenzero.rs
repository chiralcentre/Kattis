use std::io;

fn main() {
    let mut input = String::new();
    let _ = io::stdin().read_line(&mut input);
    let r: f64 = input.trim().parse().unwrap();
    // answer is (r^4 - 1) / (r - 1)
    println!("{}",((r.powi(4) - 1.0) / (r - 1.0)).round());
}