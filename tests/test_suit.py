import unittest
from .test_feature_parser import TestFeatureParser
from .test_signature_feature_extractor import TestSignatureFeatureExtractor
from .test_segmentation import TestEmailSegmenter


def create_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestEmailSegmenter())
    test_suite.addTest(TestFeatureParser())
    test_suite.addTest(TestSignatureFeatureExtractor())
    return test_suite

if __name__ == '__main__':
   suite = create_suite()

   runner=unittest.TextTestRunner()
   runner.run(suite)
