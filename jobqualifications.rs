use std::io::{self, Read, Write};
use std::collections::HashSet;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();

    let n: i64 = it.next().unwrap().parse().unwrap();
    let m: i64 = it.next().unwrap().parse().unwrap();
    let mut q: HashSet<String> = HashSet::new();
    for _ in 0..n {
        q.insert(it.next().unwrap().to_string());
    }

    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for _ in 0..m {
        let k: i64 = it.next().unwrap().parse().unwrap();
        let mut found: bool = true;
        for _ in 0..k {
            let s: &str = it.next().unwrap();
            if !found { continue; }
            if !q.contains(s) { found = false; }
        }
        if found {
            writeln!(out, "apply").unwrap();
        } else {
            writeln!(out, "why bother?").unwrap();
        }

    }
}