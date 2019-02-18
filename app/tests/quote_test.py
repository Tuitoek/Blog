import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Quote class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_quote = Quote(	"Sam Ewing",	33,"Computers are like bikinis. They save people a lot of guesswork.","http://quotes.stormconsultancy.co.uk/quotes/33")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
