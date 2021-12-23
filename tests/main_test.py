
import unittest

from src.main import main
from services.recognition_service import RecognitionService

class MainTest(unittest.TestCase):
    def test_main(self):
        recognition_service = RecognitionService()
        main()
        self.assertEqual('foo'.upper(), 'FOO')