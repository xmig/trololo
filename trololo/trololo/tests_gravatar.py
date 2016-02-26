from django.test import TestCase

import unittest
import gravatarintegration


class MyFuncCase(unittest.TestCase):

    def test_my_gravatar(self):
        email = "dikov.yury@gmail.com"
        self.assertEqual(
            gravatarintegration.get_avatavr_url(email),
            'http://www.gravatar.com/avatar/5740211ff155850b45157e01c360d580?s=50&d=http%3A%2F%2Fwww.example.com%2Fdefault.jpg'
        )
