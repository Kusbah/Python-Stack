import unittest

def reverseList(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

class TestReverseList(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])

    def test_empty_list(self):
        self.assertEqual(reverseList([]), [])

    def test_single_element(self):
        self.assertEqual(reverseList([42]), [42])

# if __name__ == '__main__':
#     unittest.main()

def isPalindrome(word):
    return word == word[::-1]


class TestisPalindrome(unittest.TestCase):
    def test_racecar(self):
        self.assertEqual(isPalindrome("racecar"),True)
    def test_not_palindrome(self):
        self.assertFalse(isPalindrome("rabcr"))
    def test_single_letter(self):
        self.assertTrue(isPalindrome("a"))
    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))
    def test_two_letter_palindrome(self):
        self.assertTrue(isPalindrome("aa"))

# if __name__ == '__main__':
#     unittest.main()

def coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return [quarters, dimes, nickels, pennies]

class TestCoins(unittest.TestCase):

    def test_example(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])

    def test_exact_quarters(self):
        self.assertEqual(coins(75), [3, 0, 0, 0])

    def test_single_each(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])

    def test_only_pennies(self):
        self.assertEqual(coins(4), [0, 0, 0, 4])

    def test_zero(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])

    def test_all_coin_types(self):
        self.assertEqual(coins(99), [3, 2, 0, 4])
        
if __name__ == '__main__':
    unittest.main()