import getopt
import random
import sys


class BracketUnbalanced(Exception):
    pass


def spin_text(text):
    opening_b = text.find('{')

    if opening_b == -1:
        return text

    opening_b2 = text.find('{', opening_b+1)
    closing_b = text.find('}', opening_b+1)

    if closing_b == -1:
        raise BracketUnbalanced()

    if opening_b2 != -1 and opening_b2 < closing_b:
        # brackets inside
        text = text[:opening_b2] + spin_text(text[opening_b2:])
        return spin_text(text)

    content = text[opening_b+1:closing_b]
    choice = random.choice(content.split('|'))
    text = text[:opening_b] + choice + text[closing_b+1:]
    return spin_text(text)


def main():
    opts, args = getopt.getopt(sys.argv[1:], "n:p:")
    opts = dict(opts)

    with open(opts['-p']) as f:
        text = f.read()

    for i in range(int(opts['-n'])):
        print(spin_text(text))
