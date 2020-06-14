import unittest
from timeit import default_timer as timer
from py_prime import PyPrime

class TestPrimeImplementations(unittest.TestCase):

    primes = [274432559]

    def test_small_primes(self):
        test_tuples = [[2, True], 
                       [3, True],
                       [5, True],
                       [11, True],
                       [4, False],
                       [6, False],
                       [8, False],
                       [49, False],
                       [21, False]
                    ]
        for method in [PyPrime.is_prime_by_python, 
                       PyPrime.is_prime_unoptimized_by_python]:
            for test_tupel in test_tuples:
                num, expected_res = test_tupel
                self.assertEqual(method(num), 
                                 expected_res, 
                                 "Should be {} -> {}".format(num, expected_res))
    
    def test_prime_crunching_time(self):
        rs_time_elapesed, rs_is_prime = \
            self._executor(PyPrime.is_prime_by_rust, 
                           TestPrimeImplementations.primes[0],
                           "Rust implementation: {} is prime {} time elapsed {}")

        rs_unoptimized_time_elapesed, rs_unoptimized_is_prime = \
            self._executor(PyPrime.is_prime_unoptimized_by_rust, 
                           TestPrimeImplementations.primes[0],
                           "Rust implementation unoptimized: {} is prime {} time elapsed {}")

        py_time_elapesed, py_is_prime = \
            self._executor(PyPrime.is_prime_by_python, 
                           TestPrimeImplementations.primes[0],
                           "Python implementation: {} is prime {} time elapsed {}")

        py_unoptimized_time_elapesed, py_unoptimized_is_prime = \
            self._executor(PyPrime.is_prime_unoptimized_by_python, 
                           TestPrimeImplementations.primes[0],
                           "Python implementation unoptimized: {} is prime {} time elapsed {}")

        print("Optimized: Rust is {} times faster than Python."
        .format(py_time_elapesed / rs_time_elapesed))
        print("Unoptimized: Rust is {} times faster than Python."
        .format(py_unoptimized_time_elapesed / rs_unoptimized_time_elapesed))

    def _executor(self, method, prime_cadidate, message):
        start_time = timer()
        is_prime = method(prime_cadidate)
        time_elapesed = timer() - start_time
        print(message.format(prime_cadidate, is_prime, time_elapesed))
        return [time_elapesed, is_prime]


if __name__ == '__main__':
    unittest.main()