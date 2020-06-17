use pyo3::prelude::*;
pub mod math;
use math::*;



/// py_prime_checker implemented in rust
/// Functions:
/// - is_prime 
#[pymodule]
fn libpy_prime_number_checker(_py: Python, m: &PyModule) -> PyResult<()> {
    // PyO3 aware function. All of our Python interfaces could be declared in a separate module.
    // Note that the `#[pyfn()]` annotation automatically converts the arguments from
    // Python objects to Rust values, and the Rust return value back into a Python object.
    // The `_py` argument represents that we're holding the GIL.
    #[pyfn(m, "is_prime")]
    fn is_prime_py(_py: Python, a: u64) -> PyResult<bool> {
        let out = is_prime(a);
        Ok(out)
    }

    #[pyfn(m, "is_prime_unoptimized")]
    fn is_prime_py_unoptimized(_py: Python, a: u64) -> PyResult<bool> {
        let out = is_prime_unoptimized(a);
        Ok(out)
    }

    Ok(())
}


