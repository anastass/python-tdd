#This file was originally generated by PyScripter's unitest wizard

import unittest
import para


class TestPara(unittest.TestCase):

    def setUp(self):
        self._para = para.Para()

    def tearDown(self):
        pass

    def test_default_column_value(self):
        expected = 72
        actual = self._para.get_columns()
        self.assertEqual(expected, actual)

    def test_assigning_column_value(self):
        expected = 8
        self._para.set_columns(expected)
        actual = self._para.get_columns()
        self.assertEqual(expected, actual)

    def test_assigning_column_value_when_object_is_created(self):
        expected = 12
        o = para.Para(expected)
        actual = o.get_columns()
        self.assertEqual(expected, actual)

    def test_column_exception(self):
        col = -5
        with self.assertRaises(ValueError) as cm:
            self._para.set_columns(col)
        self.assertEqual("The number of columns should be a positive integer. Given: " + str(col), str(cm.exception))

    # test how formatter strips spaces
    def test_formatting(self):
        self.assertEqual("", self._para.format_text(""), "empty string is not formatted correctly")
        self.assertEqual("abc", self._para.format_text("abc"), "inputted sting was changed")
        self.assertEqual("abc", self._para.format_text(" abc"), "leading space not was stripped")
        self.assertEqual("abc", self._para.format_text(" abc    "), "trailing space was not stripped too")
        self.assertEqual("abc cde", self._para.format_text("abc  cde"), \
                         "extra internal whitespace is not handled correctly")

    def test_wrapping(self):
        o = para.Para(8)
        self.assertEqual("abc def", o.format_text("abc    def"), "short line is not formatted correctly")
        #self.assertEqual("one two\nthree", o.format_text("one two three"), "short line is not formatted correctly")


if __name__ == '__main__':
    unittest.main()