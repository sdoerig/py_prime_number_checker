use pyo3::prelude::*;


fn is_prime(num: u64) -> bool {
    // Checks it a positive integer is prime and returns true
    // if it is. 
    // The algorithm is little optimized and just inteded for demonstrations.
    if num == 2 || num == 3 {
        true
    } else if num % 2 == 0 || num <= 1 {
        // even or smaller then one
        false
    } else {
        let mut res = true;
        let partial_num_range = num / 4 + 1;
        
        for i in 1..partial_num_range {
            if num % (2 * i + 1) == 0 {
                res = false;
                break;
            }
        }
        res
    }
}



/// py_prime_checker implemented in rust
/// Functions:
/// - is_prime 
#[pymodule]
fn py_prime_checker(_py: Python, m: &PyModule) -> PyResult<()> {
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
    // For primes see https://bigprimes.org - thanks, great job. 
    use super::is_prime;
    #[test]
    fn test_small_primes() {
        assert_eq!(is_prime(2), true);
        assert_eq!(is_prime(3), true);
        assert_eq!(is_prime(5), true);
        assert_eq!(is_prime(11), true);
        assert_eq!(is_prime(3), true);
    }
    #[test]
    fn test_small_non_primes() {
        assert_eq!(is_prime(4), false);
        assert_eq!(is_prime(6), false);
        assert_eq!(is_prime(8), false);
        assert_eq!(is_prime(49), false);
        assert_eq!(is_prime(21), false);
    }

    #[test]
    fn test_medium_primes() {
        assert_eq!(is_prime(839323), true);
        assert_eq!(is_prime(179689), true);
        assert_eq!(is_prime(413081), true);
        assert_eq!(is_prime(799801), true);
    }

    #[test]
    fn test_medium_non_primes() {
        // combined by two primes multiplied - will be crunced at 
        // the smallest prime factor.
        assert_eq!(is_prime(317701 * 895313), false);
        assert_eq!(is_prime(658979 * 852457), false);
        assert_eq!(is_prime(200273 * 877469), false);
        assert_eq!(is_prime(738851 * 384547), false);
    }

    
}
