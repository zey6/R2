import pytest
import random
from crypto import *
from string import ascii_letters as printable

ord_value = {ch: i for i, ch in enumerate(printable)}


def read_file(file) -> str:
    with open(file) as fh:
        s = fh.read()
    return s


def write_to_file(file, s) -> None:
    with open(file, 'w') as fh:
        fh.write(s)


def test_file_output_1():
    expected = ''.join([printable[random.randint(0, len(printable) - 1)] for _ in range(40)])
    write_to_file('atestfile.txt',expected)
    crypto('atestfile.txt', lambda x: printable[(ord_value[x] + 5) % len(printable)])
    assert expected != read_file('atestfile.txt')
    crypto('atestfile.txt', lambda x: printable[(ord_value[x] - 5) % len(printable)])
    assert expected == read_file('atestfile.txt')


def test_file_output_2():
    expected = ''.join([printable[random.randint(0, len(printable) - 1)] for _ in range(20)])
    write_to_file('atestfile.txt', expected)
    crypto('atestfile.txt', lambda x: printable[(ord_value[x] + 5) % len(printable)])
    assert expected != read_file('atestfile.txt')
    crypto('atestfile.txt', lambda x: printable[(ord_value[x] - 5) % len(printable)])
    assert expected == read_file('atestfile.txt')