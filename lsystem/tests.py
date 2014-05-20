import unittest
import lsystem

class LSystemTestCase(unittest.TestCase):
    def test_simple(self):
        lsys = lsystem.LSystem(rules={'a': ['a', 'b'], 'b': ['a']}, initial=['a'])
        self.assertEqual(lsys.generate(0), ['a'])
        self.assertEqual(lsys.generate(1), ['a', 'b'])
        self.assertEqual(lsys.generate(2), ['a', 'b', 'a'])

    def test_single_chars(self):
        lsys = lsystem.LSystem(rules={'a': 'ab', 'b': 'a'}, initial='a', singlechars=True)
        self.assertEqual(lsys.generate(0), 'a')
        self.assertEqual(lsys.generate(1), 'ab')
        self.assertEqual(lsys.generate(2), 'aba')

    def test_copies_consts(self):
        lsys = lsystem.LSystem(rules={'a': 'cab', 'b': 'a'}, initial='a', singlechars=True)
        self.assertEqual(lsys.generate(0), 'a')
        self.assertEqual(lsys.generate(1), 'cab')
        self.assertEqual(lsys.generate(2), 'ccaba')

    def test_required_init_args(self):
        with self.assertRaises(Exception):
            lsystem.LSystem()
        with self.assertRaises(Exception):
            lsystem.LSystem(initial='a')
        with self.assertRaises(Exception):
            lsystem.LSystem(rules={'a': 'a'})



if __name__ == '__main__':
    unittest.main()
