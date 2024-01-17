import unittest

def string_rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle','erbottlewat',True),
        ('foo','bar',False),
        ('foo','foofoo',False)
    ]

    def test_string_rotation(self):
        for (s1,s2,expected) in self.data:
            actual = string_rotation(s1,s2)
            self.assertEqual(actual,expected,f"Failed for {s1} and {s2}")

if __name__ == "__main__":
    unittest.main()
