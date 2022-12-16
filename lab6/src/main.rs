//use std::io;
use std::env;
fn read_factors() -> [f64; 3] {
    let name_factors = ["a", "b", "c"];
    let mut curr_index = 0;
    let args: Vec<String> = env::args().collect();
    for i in args[2..].iter() {
        println!("{}", i);
    }
    return [5.5, 4.1, 5.6];
}
fn main() {// -> io::Result<()>{
    // println!("Hello, world!");
    // let mut input = String::new();
    // io::stdin().read_line(&mut input)?;
    // println!("{}", input);
    // Ok(())
    let args: Vec<String> = env::args().collect();
    for i in args[2..].iter() {
        println!("{}", i);
    }
}
