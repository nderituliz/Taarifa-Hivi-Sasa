import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    """
    class to test the behaviour of the articles class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_article = Articles("FOX NEWS", "Trump Loses but refuses to leave office")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


if __name__ == '__main__':
    unittest.main()