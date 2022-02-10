import unittest

from app.models import User, Post, Comment


class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='alex', email='alexndegwa46@gmail.com', password='0711693062')
        self.new_post = Post()
        self.new_comment = Comment()

    def test_user_instance(self):
        pass

    def test_post_instance(self):
        pass

    def test_comment_instance(self):
        pass
