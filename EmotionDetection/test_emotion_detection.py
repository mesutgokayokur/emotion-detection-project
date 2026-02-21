import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test Case 1: Joy (Mutluluk)
        statement_1 = "I am glad this happened"
        response_1 = emotion_detector(statement_1)
        self.assertEqual(response_1['dominant_emotion'], 'joy')

        # Test Case 2: Anger (Öfke)
        statement_2 = "I am really mad about this"
        response_2 = emotion_detector(statement_2)
        self.assertEqual(response_2['dominant_emotion'], 'anger')

        # Test Case 3: Disgust (İğrenme)
        statement_3 = "I feel disgusted just hearing about this"
        response_3 = emotion_detector(statement_3)
        self.assertEqual(response_3['dominant_emotion'], 'disgust')

        # Test Case 4: Sadness (Üzüntü)
        statement_4 = "I am so sad about this"
        response_4 = emotion_detector(statement_4)
        self.assertEqual(response_4['dominant_emotion'], 'sadness')

        # Test Case 5: Fear (Korku)
        statement_5 = "I am really afraid that this will happen"
        response_5 = emotion_detector(statement_5)
        self.assertEqual(response_5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
