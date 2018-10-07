from unittest import TestCase
from signature_extractor.segmentation import EmailSegmenter


class TestEmailSegmenter(TestCase):

    def setUp(self):
        self.segmenter_obj = EmailSegmenter()

    def tearDown(self):
        pass

    def test_get_longest_signature_segment(self):
        tests = ["11001110", "11111", "101", "000000", "00110101110"]
        output = ["111", "11111", "1", "", "111"]
        for _idx, t in enumerate(tests):
            extracted = self.segmenter_obj.get_longest_signature_segment(t)
            self.assertEqual(t[extracted[0]:extracted[1]], output[_idx])

    def test_prepare_text_for_classification(self):
        text = "This is first line.\n This is second line.\n This one is third line.\n And this one is fourth line."
        expected = [['This is first line.', '', 'This is second line.'],
                    ['This is second line.', 'This is first line.', 'This one is third line.'],
                    ['This one is third line.', 'This is second line.', 'And this one is fourth line.'],
                    ['And this one is fourth line.', 'This one is third line.', '']]

        output = self.segmenter_obj.prepare_text_for_classification(text)
        self.assertTrue(expected == output)


if __name__ == '__main__':
    unittest.main()
