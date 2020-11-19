#! /usr/bin/python3
'''\
Not number
'''
import sys
import io
import re
import pytest

def test_nan(capsys):
    original_stdin = sys.stdin

    sys.stdin = io.StringIO('Malia\nX\none\n27\n')

    import aloha_e2
    
    strRet = capsys.readouterr()

    sys.stdin = original_stdin

    assert re.search(r"OOPS!", strRet.out)
