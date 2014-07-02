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

    def test_non_neg_gen(self):
        lsys = lsystem.LSystem(rules={'a': 'ab', 'b': 'a'}, initial='a', singlechars=True)
        self.assertRaises(TypeError, lsys.generate, -1)

    def test_copies_consts(self):
        lsys = lsystem.LSystem(rules={'a': 'cab', 'b': 'a'}, initial='a', singlechars=True)
        self.assertEqual(lsys.generate(0), 'a')
        self.assertEqual(lsys.generate(1), 'cab')
        self.assertEqual(lsys.generate(2), 'ccaba')

    def test_required_init_args(self):
        self.assertRaises(Exception, lsystem.LSystem)
        self.assertRaises(Exception, lsystem.LSystem, None, {'initial': 'a'})
        self.assertRaises(Exception, lsystem.LSystem, None, {'rules': {'a': 'a'}})

    def test_random_seed(self):
        lsys = lsystem.LSystem(initial='0', singlechars=True, rules={'0': [(1, '0'), (1, '1[0]0')], '1': '11'})
        lsys.seed = 12
        results_12 = [lsys.generate(x) for x in [0, 1, 2, 3, 4]]
        lsys.seed = 30
        results_30 = [lsys.generate(x) for x in [0, 1, 2, 3, 4]]
        self.assertNotEqual(results_12, results_30)

        lsys.seed = 12
        self.assertEqual([lsys.generate(x) for x in [0, 1, 2, 3, 4]], results_12)
        lsys.seed = 12
        self.assertEqual([lsys.generate(x) for x in [0, 1, 2, 3, 4]], results_12)
        lsys.seed = 30
        self.assertEqual([lsys.generate(x) for x in [0, 1, 2, 3, 4]], results_30)


class WeightedRowTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(lsystem.expand_weighted([(1, 'a'), (1, 'b')]), ['a', 'b'])
        self.assertEqual(lsystem.expand_weighted([(1, 'a'), (2, 'b')]), ['a', 'b', 'b'])


class RuleParsingTestCase(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(lsystem.convert_rules({'a': ['b']}, singlechars=False), {'a': [['b']]})
        self.assertEqual(lsystem.convert_rules({'a': ['b'], 'b': ['a', 'b']}, singlechars=False), {'a': [['b']], 'b': [['a', 'b']]})
        self.assertEqual(lsystem.convert_rules({'a': 'b'}, singlechars=True), {'a': [['b']]})
        self.assertEqual(lsystem.convert_rules({'a': 'b', 'b': 'ab'}, singlechars=True), {'a': [['b']], 'b': [['a', 'b']]})

    def test_single_char_weighted(self):
        self.assertEqual(lsystem.convert_rules({'a': 'b', 'b': [(1, 'a'), (2, 'b')]}, singlechars=True), {'a': [['b']], 'b': [['a'], ['b'], ['b']]})
        self.assertEqual(lsystem.convert_rules({'a': 'b', 'b': [(1, 'a'), (2, 'ab')]}, singlechars=True), {'a': [['b']], 'b': [['a'], ['a', 'b'], ['a', 'b']]})

    def test_nonsingle_weighted(self):
        self.assertEqual(
            lsystem.convert_rules({'a': ['ab'], 'ab': [(1, ['a', 'ab']), (2, ['a'])]}, singlechars=False),
            {'a': [['ab']], 'ab': [['a', 'ab'], ['a'], ['a']]})

if __name__ == '__main__':
    unittest.main()
