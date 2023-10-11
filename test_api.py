import unittest
from api import getRepos


class TestAPI(unittest.TestCase):
    def testStatus200(self): 
        # Test expected 200 status code
        self.assertEqual(getRepos("OmarAbdelmotaleb"), 200)
        self.assertEqual(getRepos("richkempinski"), 200)
    
    def testStatusFailed(self):
        # Test that the API doesn't get back stuff for invalid names
        self.assertNotEqual(getRepos("-"), 200)


if __name__ == '__main__':
    unittest.main()
