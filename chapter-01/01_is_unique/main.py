import unittest
# O(n) time, O(1) space
def is_unique(str):
  if len(str) > 128:
    return False
  
  chars_table = [False for _ in range(128)]

  for char in str:
    if chars_table[ord(char)]:
      return False
    chars_table[ord(char)] = True

  return True

# O(n^2) time, O(1) space
def is_unique_without_data_structures(str):
  if len(str) > 128:
    return False
  for i in range(len(str)):
     for j in range(i+1, len(str)):
        if str[i] == str[j]:
          return False
  return True

class TestUnique(unittest.TestCase):
    dataT = [('nacho'), ('*)asz'), ('')]
    dataF = [('alfonsina'), ('(nacho))')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertEqual(actual, True, f"verifying if {test_string} is unique str")
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertEqual(actual, False, f"verifying if {test_string} is not unique str")

class TestUniqueWithoutExtraStructures(unittest.TestCase):
    dataT = [('nacho'), ('*)asz'), ('')]
    dataF = [('alfonsina'), ('(nacho))')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique_without_data_structures(test_string)
            self.assertEqual(actual, True, f"verifying if {test_string} is unique str")
        # false check
        for test_string in self.dataF:
            actual = is_unique_without_data_structures(test_string)
            self.assertEqual(actual, False, f"verifying if {test_string} is not unique str")

if __name__ == "__main__":
    unittest.main()
