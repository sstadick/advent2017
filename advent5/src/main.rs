use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;


fn cal_jumps(jmplist: &mut Vec<isize>) -> isize {
    let mut i : isize = 0;
    let mut count: isize = 0;

    while i < jmplist.len() as isize{
        let j = jmplist[i as usize];
        if j > 2 { // for part two
            jmplist[i as usize] = j - 1;
        } else {
            jmplist[i as usize] = j + 1;
        }
        i = i + j;
        count = count + 1; // just use this for part one
    }
    count
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    let f = File::open(filename).expect("File can't be opened");
    let file = BufReader::new(&f);

    let mut positions: Vec<isize> = Vec::new();

    for line in file.lines() {
        positions.push(line.unwrap().trim().parse().unwrap());
    }

    let jumps = cal_jumps(&mut positions);

    println!("Positions: {:?}", jumps);

}
