import unittest
import lsystem

class LSystemTestCase(unittest.TestCase):
    def test_simple(self):
        lsys = lsystem.LSystem(alphabet=['a', 'b'], rules={'a': ['a', 'b'], 'b': ['a']}, initial=['a'])
        self.assertEqual(lsys.generate(0), ['a'])
        self.assertEqual(lsys.generate(1), ['a', 'b'])
        self.assertEqual(lsys.generate(2), ['a', 'b', 'a'])

    def test_single_chars(self):
        lsys = lsystem.LSystem(alphabet='ab', rules={'a': 'ab', 'b': 'a'}, initial='a', singlechars=True)
        self.assertEqual(lsys.generate(0), 'a')
        self.assertEqual(lsys.generate(1), 'ab')
        self.assertEqual(lsys.generate(2), 'aba')



if __name__ == '__main__':
    unittest.main()