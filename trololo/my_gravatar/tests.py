from django.test import TestCase
import unittest
from templatetags import gravatar_register


class MyFuncCase(unittest.TestCase):

    def test_my_gravatar(self):
        email = "dikov.yury@gmail.com"
        self.assertEqual(
            gravatar_register.gravatar_url(email),
            'http://www.gravatar.com/avatar/5740211ff155850b45157e01c360d580?s=40&d=http%3A%2F%2Fexample.com%2Fstatic%2Fimages%2Fdefaultavatar.jpg'
        )

    def test_my_gravatar_url(self):
        email = "dikov.yury@gmail.com"
        self.assertEqual(
            gravatar_register.gravatar(email),
            '<img src="http://www.gravatar.com/avatar/5740211ff155850b45157e01c360d580?s=40&d=http%3A%2F%2Fexample.com%2Fstatic%2Fimages%2Fdefaultavatar.jpg" width="40" height="40">'
        )
