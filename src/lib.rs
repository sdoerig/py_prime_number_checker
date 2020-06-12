
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;


fn is_prime(num: u64) -> bool {
    if num <= 1 {
        false
    } else {
        let mut res = true;
        for i in 2..num {
            if num % i == 0 {
                res = false;
                break;
            }
        }
        res
    }
}



/// This module is implemented in Rust.
#[pymodule]
fn rust2py(py: Python, m: &PyModule) -> PyResult<()> {
    // PyO3 aware function. All of our Python interfaces could be declared in a separate module.
    // Note that the `#[pyfn()]` annotation automatically converts the arguments from
    // Python objects to Rust values, and the Rust return value back into a Python object.
    // The `_py` argument represents that we're holding the GIL.
    #[pyfn(m, "is_prime")]
    fn is_prime_py(_py: Python, a: u64) -> PyResult<bool> {
        let out = is_prime(a);
        Ok(out)
    }

    Ok(())
}



#[cfg(test)]
mod tests {
    use super::is_prime;
    #[test]
    fn it_works() {
        assert_eq!(is_prime(5), true);
    }
}
