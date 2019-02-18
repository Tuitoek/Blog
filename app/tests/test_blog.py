import unittest
from app.models import Blog

class BlogTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Blog class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_blog = Blog(1,"Syfa Akinyi","Three boys","One is born in his father’s house. His mother sighs in relief when his frail new voice finally clashes with the air. Outside, his father airs his frustration. This is yet another mouth to feed. He’s the last of twelve. His name will be Tumaini. Hope. As in, the parents really hope this is it, this is the last child.","https://confessions341.files.wordpress.com/2019/02/1550218968947-745459549.jpg","https://confessions341.wordpress.com/2019/02/15/three-boys/")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
