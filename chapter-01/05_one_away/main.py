import unittest


def one_away(str, edited):
    if not -1 <= len(str) - len(edited) <= 1:
        return False
    # edited
    if len(str) == len(edited):
        diff_count = 0
        for char1, char2 in zip(str, edited):
            if char1 != char2:
                diff_count += 1
            if diff_count > 1:
                return False
        return True
    # deleted
    elif len(str) > len(edited):
        scan_index = 0
        for i in range(len(str)):
            if len(edited) - 1 >= scan_index and str[i] == edited[scan_index]:
                scan_index += 1
        return i - scan_index == 0

    # inserted
    elif len(str) < len(edited):
        scan_index = 0
        for i in range(len(edited)):
            if len(str) - 1 >= scan_index and edited[i] == str[scan_index]:
                scan_index += 1
        return i - scan_index == 0
    return False


class Test(unittest.TestCase):
    """Test Cases"""

    data = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("paleabc", "pleabc", True),
        ("pale", "ble", False),
        ("a", "b", True),
        ("", "d", True),
        ("d", "de", True),
        ("pale", "pale", True),
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("pale", "pse", False),
        ("ples", "pales", True),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pale", "pkle", True),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(
                actual,
                expected,
                f"verifying if {test_s1} is one edit away from {test_s2}",
            )


if __name__ == "__main__":
    unittest.main()
