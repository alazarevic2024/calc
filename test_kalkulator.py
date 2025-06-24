import kalkulator
import pytest

def test_sabiranje():
    ocekivano = 5
    dobijeno = kalkulator.saberi(2, 3)
    assert ocekivano == dobijeno 