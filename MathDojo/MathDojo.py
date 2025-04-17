import unittest
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result+=num
        for n in nums:
            self.result += n
        return self
    def subtract(self, num, *nums):
        self.result-=num
        for n in nums:
            self.result -= n
        return self

# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)    # should print 5
# run each of the methods a few more times and check the result!

class TestMathDojo(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()
    def test_MathDojo(self):
        self.md.add(5)
        self.assertEqual(self.md.result,5)
    def test_add_subtract(self):
        self.md.add(2).add(2,5,1).subtract(3,2)
        self.assertEqual(self.md.result,5)

if __name__ == '__main__':
    unittest.main()