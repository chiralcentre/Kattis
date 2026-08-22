use std::io::{self, Read};
use std::cmp;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();

    let a: i64 = it.next().unwrap().parse().unwrap();
    let b: i64 = it.next().unwrap().parse().unwrap();

    let mut ans: i64 = 0;
    let (mut i,c,d) = (0,cmp::min(a,b),cmp::max(a,b));
    while i < c {
        ans += d;
        i += 1;
    }
    println!("{}", ans);
}