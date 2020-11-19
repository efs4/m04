#! /usr/bin/python3
'''\
John
'''
import sys
import io
import re

def test_johnok(capsys):
    original_stdin = sys.stdin

    sys.stdin = io.StringIO('Jane\n19\n')

    import aloha_e2
    strRet = capsys.readouterr()

    sys.stdin = original_stdin

    assert re.search(r"Hello, Jane", strRet.out)
