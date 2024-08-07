from results import reverse_substrings
import unittest

class TestReverseSubstrings(unittest.TestCase):

    def test_simple_reverse(self):
        self.assertEqual(reverse_substrings("Example (string)"), "Example gnirts")

    def test_nested_parentheses(self):
        self.assertEqual(reverse_substrings("(abc(def)ghi)"), "ihgfedcba")
        self.assertEqual(reverse_substrings("a(b(c)d)e"), "a(dcb)e")

    def test_multiple_reversals(self):
        self.assertEqual(reverse_substrings("x(a) y(b) z(c)"), "x(a) y(b) z(c)")
        self.assertEqual(reverse_substrings("prefix (in) middle (out) suffix"), "prefix ni middle tuo suffix")

    def test_no_parentheses(self):
        self.assertEqual(reverse_substrings("no parentheses here"), "no parentheses here")

    def test_empty_string(self):
        self.assertEqual(reverse_substrings(""), "")

    def test_all_parentheses(self):
        self.assertEqual(reverse_substrings("(((((())))))"), "")

    def test_complex_nesting(self):
        self.assertEqual(reverse_substrings("a(bcd(efg(hij))klm)"), "amlkjihgfedcb")

if __name__ == '__main__':
    unittest.main()