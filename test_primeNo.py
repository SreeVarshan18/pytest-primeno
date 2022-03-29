import pytest

import primeNo

@pytest.mark.parametrize("a, b", [(3, True), (4, False), (1, False), (20, False), (11, True)])
def test_prime(a,b):
    result = primeNo.checkPrime(a)
    assert result == b

