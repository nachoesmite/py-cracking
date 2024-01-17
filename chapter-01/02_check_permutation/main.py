import unittest
from collections import Counter

# O(n log n) time, O(1) space
def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

# O(n) time, O(1) space
def is_permutation_with_counter(str1, str2):
  c = Counter()
  for char in str1:
    c[char] += 1
  for char in str2:
    if c[char] == 0:
      return False
    c[char] -= 1
  return True

class TestPermutation(unittest.TestCase):
  dataT = [('nacho', 'hcona'), ('*)asz', 'sza*)'), ('', '')]
  dataF = [('alfonsina', 'alfonsino'), ('(nacho))', 'nacho')]

  def test_permutation(self):
    # true check
    for test_strings in self.dataT:
      actual = is_permutation(test_strings[0], test_strings[1])
      self.assertEqual(actual, True, f"verifying if {test_strings[0]} is permutation of {test_strings[1]}")
    # false check
    for test_strings in self.dataF:
      actual = is_permutation(test_strings[0], test_strings[1])
      self.assertEqual(actual, False, f"verifying if {test_strings[0]} is not permutation of {test_strings[1]}")

class TestPermutationWithCounter(unittest.TestCase):
  dataT = [('nacho', 'hcona'), ('*)asz', 'sza*)'), ('', '')]
  dataF = [('alfonsina', 'alfonsino'), ('nacho','(nacho))')]

  def test_permutation(self):
    # true check
    for test_strings in self.dataT:
      actual = is_permutation_with_counter(test_strings[0], test_strings[1])
      self.assertEqual(actual, True, f"verifying if {test_strings[0]} is permutation of {test_strings[1]}")
    # false check
    for test_strings in self.dataF:
      actual = is_permutation_with_counter(test_strings[0], test_strings[1])
      self.assertEqual(actual, False, f"verifying if {test_strings[0]} is not permutation of {test_strings[1]}")

if __name__ == "__main__":
  unittest.main()
