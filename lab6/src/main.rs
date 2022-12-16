use std::io;
use std::env;
use std::mem;
enum SquareRootResult {
    /// Unit-тип
    NoRoots,
    /// Один корень - кортежная структура
    OneRoot(f64),
    /// С-подобная структура
    TwoRoots { root1: f64, root2: f64 },

    ThreeRoots { root1: f64, root2: f64, root3:f64 },
    FourRoots { root1: f64, root2: f64, root3:f64, root4:f64 },
}
struct Equation {
    /// Коэффициент A
    a: f64,
    /// Коэффициент B
    b: f64,
    /// Коэффициент C
    c: f64,
    /// Дискриминант
    diskr: f64,
    /// Корни
    res: SquareRootResult,
}
impl Equation {
    /// Функция вычисления корней
    fn calculate_roots(&mut self) {
        self.diskr = self.b.powi(2) - 4.0 * self.a * self.c;
        self.res = {
            if self.diskr < 0.0 {
                SquareRootResult::NoRoots
            } else if self.diskr == 0.0 {
                let rt = -self.b / (2.0 * self.a);
                if rt <= 0.0 {
                    SquareRootResult::NoRoots
                } else if rt == 0.0 {
                    SquareRootResult::OneRoot(rt)
                } else {
                    SquareRootResult::TwoRoots{root1: -rt.sqrt(), root2: rt.sqrt()}
                }
            } else {
                let mut rt1 = (-self.b - self.diskr.sqrt()) / (2.0 * self.a);
                let mut rt2 = (-self.b + self.diskr.sqrt()) / (2.0 * self.a);
                if rt1 > rt2 {
                    mem::swap(&mut rt1, &mut rt2);
                }
                if rt1 * rt2 == 0.0 {
                    if rt2 > 0.0 {
                        SquareRootResult::ThreeRoots{root1: rt1, root2: -rt2.sqrt(), root3: rt2.sqrt()}
                    } else {
                        SquareRootResult::OneRoot(rt2)
                    }
                }
                else if rt1 * rt2 < 0.0 {
                    SquareRootResult::TwoRoots{root1: -rt2.sqrt(), root2: rt2.sqrt()}
                }
                else {
                    if rt1 > 0.0 {
                        SquareRootResult::FourRoots{root1: -rt1.sqrt(), root2: rt1.sqrt(), root3: -rt2.sqrt(), root4: rt2.sqrt()}
                    } else {
                        SquareRootResult::NoRoots
                    }
                }
            }
        };
    }

    /// Ввод одного коэффициента
    fn set_coef(&mut self) {
        let factors = read_factors();
        self.a = factors[0];
        self.b = factors[1];
        self.c = factors[2];
    }
}

fn read_factors() -> [f64; 3] {
    let mut factors:[f64; 3] = [0.0, 0.0, 0.0];
    let name_factors = ["a", "b", "c"];
    let mut curr_index = 0;
    let args: Vec<String> = env::args().collect();
    for i in args[2..].iter() {
        let row = String::from(i);
        match row.trim().parse() {
            Ok(val) => {
            factors[curr_index] = val;
            curr_index += 1;
            }
            Err(_) => {
                continue;
            }
        };
    }
    if curr_index > 2 {
        return factors;
    }
    while curr_index <= 2 {
        println!("введите коэффициент {}: ", name_factors[curr_index]);
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Неверно введена строка");
        match input.trim().parse() {
            Ok(val) => {
                factors[curr_index] = val;
                curr_index += 1;
            }
            Err(_) => {
                continue;
            }
        }
    }
    return factors;
}
macro_rules! root_derivation {
    ($e:expr) => {{
        {
            use SquareRootResult::*;
            let eq: Equation = $e;
            let text_res = match eq.res {
                NoRoots => format!("Корней нет"),
                OneRoot(rt) => format!("Один корень => {}", rt),
                TwoRoots { root1, root2 } => format!("Два корня => {} и {}", root1, root2),
                ThreeRoots { root1, root2, root3 } => format!("Три корня => {}, {} и {}", root1, root2, root3),
                FourRoots { root1, root2, root3, root4 } => format!("Четыре корня => {}, {}, {} и {}", root1, root2, root3, root4),
            };
            println!("{}", text_res);
        }
    }};
}
fn main() {
    let mut eq = Equation {
        a: 0.0,
        b: 0.0,
        c: 0.0,
        diskr: 0.0,
        res: SquareRootResult::NoRoots,
    };
    eq.set_coef();
    eq.calculate_roots();
    root_derivation!(eq);
}
