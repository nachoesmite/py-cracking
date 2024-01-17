import unittest

def string_compression(str_to_compress):
    str_to_compress_list = list(str_to_compress)
    latest = str_to_compress[0]
    counter = 0
    result = ''
    for x in str_to_compress_list:
        if x == latest:
            counter += 1
        else:
            result += latest + str(counter)
            counter = 1
            latest = x
    result += latest + str(counter)
    return result if len(str_to_compress) > len(result) else str_to_compress 
class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected, test_string)

if __name__ == "__main__":
    unittest.main()
