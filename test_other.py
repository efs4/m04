#! /usr/bin/python3
'''\
Other
'''
import sys
import io
import re

def test_keokiok(capsys):
    original_stdin = sys.stdin

    sys.stdin = io.StringIO('Malia\n8\n')

    import aloha_e2
    strRet = capsys.readouterr()

    sys.stdin = original_stdin

    assert re.search(r"Aloha [Ee]'* Malia", strRet.out)
