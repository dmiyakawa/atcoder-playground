/*
 * https://atcoder.jp/contests/typical90/tasks/typical90_bi
 */

use std::{io::Read, collections::VecDeque};

fn read_from_stdin() -> Vec<Vec<i32>> {
    let mut buffer = String::new();
    match std::io::stdin().read_to_string(&mut buffer) {
        Ok(_) => {}
        Err(msg) => {
            eprintln!("{:?}", msg);
            std::process::exit(1);
        }
    }
    let mut vec: Vec<Vec<i32>> = Vec::new();
    for s in buffer.lines() {
        let s = String::from(s);
        vec.push(s.split(' ').map(|s| s.parse::<i32>().unwrap()).collect());
    }
    vec
}

fn main() {
    let values: Vec<Vec<i32>> = read_from_stdin();
    let q = values[0][0];
    let mut deque: VecDeque<i32> = VecDeque::new();
    for i in 0..q {
        let t = values[(1 + i) as usize][0];
        let x = values[(1 + i) as usize][1];
        match t {
            1 => {
                deque.push_back(x);
            },
            2 => {
                deque.push_front(x);
            },
            _ => {
                println!("{}", deque[deque.len() - (x as usize)]);
            }
        }
    }
}
