
use std::{io::Read, collections::HashMap, cmp::max};

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
    let n = values[0][0];
    let m = values[0][1];

    let mut hash: HashMap<i32, i32> = HashMap::with_capacity(n as usize);
    for i in 0..m as usize {
        // let node_a = min(value:s[i+1][0], values[i+1][1]);
        let node_b = max(values[i+1][0], values[i+1][1]);
        let val = match hash.get(&node_b) {
            Some(val) => *val,
            _ => 0,
        };
        hash.insert(node_b, val + 1);
    }
    let mut count = 0;
    for (_node_i, value) in hash {
        // println!("{}, {}", _node_i, value);
        if value == 1 {
            count += 1;
        }
    }
    print!("{}", count);
}
