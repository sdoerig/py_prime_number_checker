# py_prime_number_checker

Note this is just for testing purposes to show how easy it is possible to gain a speedup in Python by writing CPU intensive stuff in a language like Rust.

Note also the prime checker algorithm is silly and it's only purpose is to stress the CPU. 

## Unoptimized

The used algorithm is very simple. Its complexity is O=(n).

## Optimized

The used algorithm is very simple too. Its complexity is O=(n/4).

## Running

```bash
$ cd py_prime_prime_number_checker
$ rustup default nightly
$ cargo build --release
$ /usr/bin/python3 test_py_prime.py
Rust implementation: 274432559 is prime True time elapsed 0.5027853359997607
Rust implementation unoptimized: 274432559 is prime True time elapsed 2.0088721140000416
Python implementation: 274432559 is prime True time elapsed 7.902524029000233
Python implementation unoptimized: 274432559 is prime True time elapsed 19.413287408000542
Optimized: Rust is 15.717491070590798 times faster than Python.
Unoptimized: Rust is 9.663774648822738 times faster than Python.
..
----------------------------------------------------------------------
Ran 2 tests in 29.828s

OK
```

## Conclusion

* Python library implemented in Rust does the job much faster than the implementation in native Python - as expected.
* Algorithm is not usable to distinguish big primes.
* Implentation with [PYO3](https://pyo3.rs/) is pretty easy.
