from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test joy as dominant emotion
        result = emotion_detector('I love this new technology.')
        self.assertEqual(result['dominant_emotion'], 'joy')

        # Test joy as dominant emotion
        result = emotion_detector('I hate working long hours')
        self.assertEqual(result['dominant_emotion'], 'anger')

unittest.main()