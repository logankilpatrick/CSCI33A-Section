from regex import *
import unittest

class Tests(unittest.TestCase):
    # Tests for remove_e
    def test_e_empty(self):
        self.assertEqual(remove_e(""), "")

    def test_e_hello(self):
        self.assertEqual(remove_e("Hello"), "Hllo")

    def test_e_none(self):
        self.assertEqual(remove_e("Howdy, Y'all!"), "Howdy, Y'all!")

    def test_e_multiple(self):
        self.assertEqual(remove_e("There are a few e's here"), "Thr ar a fw 's hr")

    # Tests for replace_digits
    def test_digits_empty(self):
        self.assertEqual(replace_digits(""), "")

    def test_digits_one(self):
        self.assertEqual(replace_digits("They are 7 years old."), "They are (DIGIT) years old.")

    def test_digits_none(self):
        self.assertEqual(replace_digits("Howdy, Y'all!"), "Howdy, Y'all!")

    def test_digits_multiple(self):
        self.assertEqual(replace_digits("1 and 4 are not prime, but 2 and 3 are."), "(DIGIT) and (DIGIT) are not prime, but (DIGIT) and (DIGIT) are.")

    # Tests for keep_e
    def test_keep_e_empty(self):
        self.assertEqual(keep_e(""), "")

    def test_keep_e_hello(self):
        self.assertEqual(keep_e("Hello"), "(NOT_E)e(NOT_E)(NOT_E)(NOT_E)")

    def test_keep_e_none(self):
        self.assertEqual(keep_e("Yay!"), "(NOT_E)(NOT_E)(NOT_E)!")

    def test_keep_e_multiple(self):
        self.assertEqual(keep_e("Here!"), "(NOT_E)e(NOT_E)e!")

    # Tests for censor_phone
    def test_censor_empty(self):
        self.assertEqual(censor_phone(""), "")

    def test_censor_one(self):
        self.assertEqual(censor_phone("My number is (670)-867-5309"), "My number is (DDD)-DDD-D309")

    def test_censor_none(self):
        self.assertEqual(replace_digits("Howdy, Y'all!"), "Howdy, Y'all!")

    def test_censor_multiple(self):
        self.assertEqual(censor_phone("My number is (670)-867-5309, not (657)-243-6545"), "My number is (DDD)-DDD-D309, not (DDD)-DDD-D545")

    # Tests for IDE_highlight
    def test_ide_empty(self):
        self.assertEqual(IDE_highlight(""), "")

    def test_ide_one(self):
        self.assertEqual(IDE_highlight("# This is a line of code:\nx = 4"), "(COMMENT)# This is a line of code:(COMMENT)\nx = 4")

    def test_ide_none(self):
        self.assertEqual(IDE_highlight("x = 4\nprint(x)"), "x = 4\nprint(x)")

    def test_ide_multipe(self):
        self.assertEqual(IDE_highlight("# Setting a variable\nx = 4\n# Printing a variable\nprint(x)"),
                         "(COMMENT)# Setting a variable(COMMENT)\nx = 4\n(COMMENT)# Printing a variable(COMMENT)\nprint(x)")

    # Tests for piglatinify
    def test_pig_empty(self):
        self.assertEqual(piglatinify(""), "")

    def test_pig_con(self):
        self.assertEqual(piglatinify("connor"), "onnor-cay")

    def test_pig_vow(self):
        self.assertEqual(piglatinify("elephant"), "elephant-way")

    def test_pig_two_con(self):
        self.assertEqual(piglatinify("crunchy"), "unchy-cray")

    def test_pig_multiple(self):
        self.assertEqual(piglatinify("they ate granola and yogurt"), "ey-thay ate-way anola-gray and-way ogurt-yay")




if __name__ == "__main__":
    unittest.main()