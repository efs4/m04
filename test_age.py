#! /usr/bin/python3
'''\
age
'''
import sys
import io
import re

def test_nine(capsys):
    original_stdin = sys.stdin

    sys.stdin = io.StringIO('Keoki\n19\n')

    import aloha_e2
    strRet = capsys.readouterr()

    sys.stdin = original_stdin

    assert re.search(r"21", strRet.out)
