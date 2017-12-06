use std::env;

struct Square {
    side: i32,
    largest_corner: i32,
}

impl Square {
    fn get_corners(&self) -> Vec<i32> {
        let mut c: Vec<i32> = Vec::new();
        c.push(self.largest_corner);
        for i in 1..4 {
            c.push(self.largest_corner - i * (self.side - 1));
        }
        return c;
    }

    fn closest_corner(value: &i32, corners: &Vec<i32>) -> i32 {
        let mut distance: i32 = *value;
        for (i, _corner) in corners.iter().enumerate() {
            let possible_diff: i32 = value - corners[i];
            if distance > possible_diff.abs() {
                distance = possible_diff.abs();
            }
        }
        return distance;
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let input = &args[1];
    let part = &args[2];
    let part: i32 = part.trim().parse().unwrap();
    let input: i32 = input.trim().parse().unwrap();
    if part == 1 {
        let mut start = 1;
        let mut largest = start;
        while largest < input {
            largest = start * start;
            start = start + 2;
        }
        let level = start - 2;
        let sq = Square {
            side: level,
            largest_corner: largest,
        };
        let corners = sq.get_corners();
        let distance = (level - 1) - Square::closest_corner(&input, &corners);
        println!("Distance: {}", distance);
    } else {
        println!("Part two looks hard");
    }
}

