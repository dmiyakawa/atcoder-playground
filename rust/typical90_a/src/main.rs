/*
 * https://atcoder.jp/contests/typical90/tasks/typical90_a
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


/*
 * M+1個の score_cand 以上のピースに分割可能であれば true
 */
fn bisectional_check(score_cand: i32, k: i32, l: i32, a_s: &Vec<i32>) -> bool {
    // println!("bisectional_check(score_cand: {}, k: {}, l: {})", score_cand, k, l);
    let mut prev_pos = 0;
    let mut i = 0;
    let mut vec1: Vec<i32> = Vec::new();
    let mut vec2: Vec<i32> = Vec::new();
    for _ in 0..k {
        while a_s[i] - prev_pos < score_cand {
            // println!("cur_k: {}, i: {}, prev_pos: {}, score: {}", cur_k, i, prev_pos, a_s[i] - prev_pos);
            i += 1;
            if i >= a_s.len() {
                return false;
            }
        }
        // println!("setting cur_k {} to As[{}] = {}", cur_k, i, a_s[i]);

        vec1.push(i as i32);
        vec2.push(a_s[i]);

        prev_pos = a_s[i];
    }
    vec2.push(l);
    // println!("k: {:?} ({:?})", vec1, vec2);
    l - prev_pos >= score_cand
}

#[warn(non_snake_case)]
fn main() {
    let values: Vec<Vec<i32>> = read_from_stdin();
    let n = values[0][0] as usize;
    let l = values[0][1];
    let k = values[1][0];
    let a_s = &values[2];
    assert_eq!(a_s.len(), n);

    // これよりスコアが大きくなることはない
    let theoretical_min: i32 = (l as f64 / (k + 1) as f64).ceil() as i32;

    // println!("N: {}, L: {}, K: {}", n, l, k);
    // println!("As: {:?}", a_s);
    // println!("Theoretical min: {}", theoretical_min);

    let mut min_value = 0;  // ありえる
    let mut max_value = theoretical_min + 1;  // ありえない
    let mut score_cand = theoretical_min / 2;
    loop {
        // println!("Looking for {} ({} < {} < {})", score_cand, min_value, score_cand, max_value);

        if bisectional_check(score_cand, k, l, &a_s) {
            // println!("Score {} is feasible", score_cand);
            min_value = score_cand;
        } else {
            // println!("Score {} is not feasible", score_cand);
            max_value = score_cand;
        }
        score_cand = (min_value + max_value) / 2;
        if score_cand == min_value {
            break;
        }
    }
    print!("{}", score_cand);
    // let mut score_cand = theoretical_min / 2;
    // bisectional_check(score_cand: i32, a_s: &Vec<i32>)
}
