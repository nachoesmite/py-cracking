from collections import Counter
import unittest
import re
def is_palindrome_perm(str):
  char_dict = {}
  odd_count = 0
  pattern = r"[a-zA-Z]"
  for s in str:
    x = s.lower()
    if re.match(pattern, x) is None:
      continue
    if char_dict.get(x):
      char_dict[x] += 1
    else:
      char_dict[x] = 1
    if char_dict[x] % 2 == 0:
      odd_count -= 1
    else:
      odd_count += 1
  return odd_count <= 1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_is_palindrome_perm(self):
        for [test_string, expected] in self.data:
            actual = is_palindrome_perm(test_string)
            self.assertEqual(actual, expected, test_string)

if __name__ == "__main__":
    unittest.main()    