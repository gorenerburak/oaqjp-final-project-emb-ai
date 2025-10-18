from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test joy as dominant emotion
        result = emotion_detector('I am so happy I am doing this')
        self.assertEqual(result['dominant_emotion'], 'joy')

unittest.main()