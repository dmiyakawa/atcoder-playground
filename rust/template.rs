
use std::io::Read;

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

    println!("{:?}", values);
}

