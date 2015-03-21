# -*- coding: utf-8 -*-
import unittest

from spino import spin_text, BracketUnbalanced


class SpinoTest(unittest.TestCase):
    def test_spin(self):
        choices = ['8', 'Crazy, Stupid, Love.', 'Elephant White',
            'Apollo 13', 'Mystic River']
        text = 'I like {{{0}}}'.format('|'.join(choices))
        text = spin_text(text)

        self.assertNotIn('{', text)
        self.assertNotIn('}', text)
        self.assertIn(text.replace('I like ', ''), choices)

    def test_spin_unbalanced(self):
        choices = ['8', 'Crazy, Stupid, Love.', 'Elephant White',
            'Apollo 13', 'Mystic River']
        text = 'I like {{{0}'.format('|'.join(choices))
        self.assertRaises(BracketUnbalanced, spin_text, text)

    def test_spin_multiple_levels(self):
        choices = ['Elephant White', 'Apollo 13', 'Mystic River']
        choices2 = ['8', 'Crazy, Stupid, Love.']
        text = 'I like {{{0}|{1}}}'.format('|'.join(choices),
            '|'.join(choices2))
        text = spin_text(text)

        self.assertNotIn('{', text)
        self.assertNotIn('}', text)
        self.assertIn(text.replace('I like ', ''), choices + choices2)

if __name__ == '__main__':
    unittest.main()
