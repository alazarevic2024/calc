import kalkulator
import pytest

def test_sabiranje():
    ocekivano = 6
    dobijeno = kalkulator.saberi(2, 3)
    assert ocekivano == dobijeno 