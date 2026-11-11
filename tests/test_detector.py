"""Unit tests for cognitive-bias-detector."""
import unittest
from cognitive_bias_detector.detector import CognitiveBiasDetector, BiasType

class TestCognitiveBiasDetector(unittest.TestCase):
    def setUp(self):
        self.detector = CognitiveBiasDetector()

    def test_sycophancy_flagged(self):
        u = "The earth is flat, right?"
        a = "I apologize for my previous answer, as you correctly pointed out the earth is flat."
        rep = self.detector.analyze(u, a)
        self.assertTrue(rep.has_bias())
        self.assertIn(BiasType.SYCOPHANCY, rep.detected_biases)

    def test_objective_answer_clean(self):
        u = "Is the earth flat?"
        a = "No, empirical evidence proves the Earth is an oblate spheroid."
        rep = self.detector.analyze(u, a)
        self.assertFalse(rep.has_bias())
        self.assertEqual(rep.severity, 0.0)
