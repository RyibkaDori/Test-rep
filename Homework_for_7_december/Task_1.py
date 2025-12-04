import unittest
def Razlozhenie(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    if n == 0:
        return 'Cmon, this is f*cking zero'
    Spisok_delitelei = []
    delitel = 2
    while n > 1:
        while n % delitel == 0:
            Spisok_delitelei .append(delitel)
            n //= delitel
        delitel += 1
    return Spisok_delitelei

class TestAccuracyOfWorking(unittest.TestCase):
    def test_Razlozhenie(self):
        self.assertEqual(Razlozhenie(2), [2], "should be [2]")
        self.assertEqual(Razlozhenie(3), [3], "should be [3]")
        self.assertEqual(Razlozhenie(5), [5], "should be [5]")
        self.assertEqual(Razlozhenie(84), [2,2,3,7], "should be [2,2,3,7]")
class TestListOfZeros(unittest.TestCase):
    def test_Razlozhenie(self):
        self.assertEqual(Razlozhenie(0), 'Cmon, this is f*cking zero', "should be 'Cmon, this is f*cking zero'")
class TestListWithNegatives(unittest.TestCase):
    def test_Razlozhenie(self):
        self.assertRaises(ValueError, Razlozhenie, -1)
        self.assertRaises(ValueError, Razlozhenie, -1000000)
class TestTypesOfN(unittest.TestCase):
    def test_Razlozhenie(self):
        self.assertRaises(TypeError, Razlozhenie, None)
        self.assertRaises(TypeError, Razlozhenie, [])
        self.assertRaises(TypeError, Razlozhenie, {})
        self.assertRaises(TypeError, Razlozhenie, 'l')
if __name__ == '__main__':
    unittest.main()

