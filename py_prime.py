import sys
sys.path.append('target/release')
import libpy_prime_number_checker as py_prime_checker

class PyPrime:

    @staticmethod
    def is_prime_by_rust(num):
        return py_prime_checker.is_prime(num)

    @staticmethod
    def is_prime_unoptimized_by_rust(num):
        return py_prime_checker.is_prime_unoptimized(num)
        
    @staticmethod
    def is_prime_by_python(num):
        """
        Same algo in python
        """
        if num == 2:
            return True
        elif num % 2 == 0 or num <= 1:
        # even or smaller then one
            return False
        else:
            res = True
            partial_num_range = int(num / 4) + 1

            for i in range(1, partial_num_range):
                if num % (2 * i + 1) == 0:
                    res = False
                    break
            return res

    @staticmethod
    def is_prime_unoptimized_by_python(num):
        if num <= 1:
            return False
        else:
            res = True
        for i in range(2, num):
            if num % i == 0:
                res = False
                break
        return res

