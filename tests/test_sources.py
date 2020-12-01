
import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Class to test the behaviour of the source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("Rain or Shine we play the best music all day long" , "https://www.capitalfm.co.ke/")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))


if __name__ == '__main__':
    unittest.main()