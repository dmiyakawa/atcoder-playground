
/*
 * https://atcoder.jp/contests/typical90/tasks/typical90_d
 * 004 - Cross Sum（★2）
 *
 * AC
 * https://atcoder.jp/contests/typical90/submissions/29736597
 *
 */

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
    let num_rows = &values[0][0];
    let num_cols = &values[0][1];
    let mut sum_rows: Vec<i32> = Vec::with_capacity(*num_rows as usize);
    let mut sum_cols: Vec<i32> = Vec::with_capacity(*num_cols as usize);
    let mat= &values[1..];


    for row_i in 0..*num_rows as usize{
         let lst = &mat[row_i];
         sum_rows.push(lst.iter().sum());
     }

    for col_i in  0..*num_cols as usize {
        let mut total = 0;
        for row_i in 0..*num_rows as usize {
            total += &mat[row_i][col_i];
        }
        sum_cols.push(total);
    }

    /*
    for row_i in 0..*num_rows as usize {
        let lst: Vec<String> = mat[row_i].iter().map( |&val| val.to_string()).collect();
        println!("{}", lst.join(", "))
    }
    println!("sum_rows: {:?}", sum_rows);
    println!("sum_cols: {:?}", sum_cols);
    */
    for row_i in 0..*num_rows as usize {
        let lst: Vec<String> = mat[row_i].iter().enumerate().map( |(col_i, &_)| {
            let val = sum_rows[row_i] + sum_cols[col_i] - mat[row_i][col_i];
            val.to_string()
        }).collect();
        println!("{}", lst.join(" "))
    }
}
