import unittest
from timeit import default_timer as timer
from py_prime import PyPrime

class TestPrimeImplementations(unittest.TestCase):

    primes = [274432559]

    def test_small_primes(self):
        
        self.assertEqual(PyPrime.is_prime_by_python(2), True)
        self.assertEqual(PyPrime.is_prime_by_python(3), True)
        self.assertEqual(PyPrime.is_prime_by_python(5), True)
        self.assertEqual(PyPrime.is_prime_by_python(11), True)
        self.assertEqual(PyPrime.is_prime_by_python(3), True)
    
    def test_small_non_primes(self):
        self.assertEqual(PyPrime.is_prime_by_python(4), False)
        self.assertEqual(PyPrime.is_prime_by_python(6), False)
        self.assertEqual(PyPrime.is_prime_by_python(8), False)
        self.assertEqual(PyPrime.is_prime_by_python(49), False)
        self.assertEqual(PyPrime.is_prime_by_python(21), False)
    
    def test_prime_crunching_time(self):
        rs_start_time = timer()
        rs_is_prime = PyPrime.is_prime_by_rust(TestPrimeImplementations.primes[0])
        rs_time_elapesed = timer() - rs_start_time
        print("Rust implementation: {} is prime {} time elapsed {}"
        .format( TestPrimeImplementations.primes[0], rs_is_prime, rs_time_elapesed))

        py_start_time = timer()
        py_is_prime = PyPrime.is_prime_by_python(TestPrimeImplementations.primes[0])
        py_time_elapesed = timer() - py_start_time
        print("Python implementation: {} is prime {} time elapsed {}"
        .format( TestPrimeImplementations.primes[0], py_is_prime, py_time_elapesed))

        print("Rust is {} times faster".format(py_time_elapesed / rs_time_elapesed))


if __name__ == '__main__':
    unittest.main()