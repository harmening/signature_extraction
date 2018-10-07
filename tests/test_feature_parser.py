from unittest import TestCase
from signature_extractor.preprocessing import feature_parser as f_parser


class TestFeatureParser(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_contains_phone(self):
        phone_text_tests = ["Matches +4917612345678 test first", "No phone number here",
                            "My name is Fabienne", "This is phone 333.444.5555", "My mobile num 123-444-5555",
                            "T.: 333 601 5435"]
        phone_text_tests_output = [True, False, False, True, True, True]

        for _idx, test in enumerate(phone_text_tests):
            self.assertEqual(f_parser.contains_phone(test), phone_text_tests_output[_idx])

    def test_contains_email(self):
        email_tests = ["E.: butch@gmail.com", "Our email is yolanda@becool.eu", "no email here", "this is a string"]
        email_tests_output = [True, True, False, False]

        for _idx, test in enumerate(email_tests):
            self.assertEqual(f_parser.contains_email(test), email_tests_output[_idx])

    def test_contains_signature_word(self):
        signature_words_tests = ["Manager Vincent Vega", "Quarter Pounder with Cheese in Paris", "President Marcellus Wallace",
                                 "Director Q. Tarantino", "A Royale with cheese"]
        signature_words_tests_output = [True, False, True, True, False]

        for _idx, test in enumerate(signature_words_tests):
            self.assertEqual(f_parser.contains_signature_word(test), signature_words_tests_output[_idx])

    def test_has_only_quotes(self):
        quotes_tests = ["---", "-----", "", "this is just a line"]
        quotes_tests_output = [True, True, False, False]

        for _idx, test in enumerate(quotes_tests):
            self.assertEqual(f_parser.has_only_quotes(test), quotes_tests_output[_idx])

    def test_has_url(self):
        url_tests = ["WEB.: mail.com", "Our url is http://www.mia-wallace.com", "no email here",
                     "My webpage is www.ringo.com"]
        url_tests_output = [True, True, False, True]

        for _idx, test in enumerate(url_tests):
            self.assertEqual(f_parser.has_url(test), url_tests_output[_idx])

    def test_count_named_entities(self):
        named_entity_count_tests = ["My name is Winston the Wolf", "no email or names here",
                                    "I think fast, I talk fast and I need you guys to act fast if you wanna get out of this. My name is Winston.",
                                    "I solve problems"]
        named_entity_count_tests_output = [2, 0, 1, 0]

        for _idx, test in enumerate(named_entity_count_tests):
            self.assertEqual(f_parser.count_named_entities(test), named_entity_count_tests_output[_idx])

    def test_is_under_closing_phrase(self):
        closing_phrase_tests = ["Hello friend, thanks here, One more time Thanks, Jules",
                                "Hello Jules! Thanks here, One more time Thanks"
                                "Hello friend Thanks Jules, One more time Thanks"]
        closing_phrase_tests_output = [True, False, False]
        for _idx, test in enumerate(closing_phrase_tests):
            self.assertEqual(f_parser.is_under_closing_phrase(test, 'Jules'), closing_phrase_tests_output[_idx])

    def test_is_in_second_part(self):
        text = """Mmmm Goddamn, Jimmie! This is some serious gourmet shit!\n
        Usually, me and Vince would be happy with some freeze-dried Taster's
        Choice right, but he springs this serious GOURMET shit on us! What
        flavor is this?\n Thanks Jimmie, Jules."""
        line_tests = ["Jimmie", "serious gourmet shit"]
        line_tests_output = [True, False]

        for _idx, test in enumerate(line_tests):
            self.assertEqual(f_parser.is_in_second_part(text, test), line_tests_output[_idx])

    def test_is_in_last_five_lines(self):
        text = """
	I ain't saying it's right. But you're saying a foot massage don't mean nothing, and I'm saying it does.\n
        Now look, I've given a million ladies a million foot massages, and they all meant something. We act like they don't, but they do, and that's what's so fucking cool about them.\n
        There's a sensuous thing going on where you don't talk about it, but
        you know it, she knows it, fucking Marsellus knew it, and Antwone
        should have fucking better known better.\n
        I mean, that's his fucking wife, man.\n
        He can't be expected to have a sense of humor about that shit.\n
        You know what I'm saying?\n
        That's an interesting point.\n
        """

        line_tests = ["sense of humor", "wife", "foot massage", 0]
        line_tests_output = [True, True, False, False]

        for test, result in zip(line_tests, line_tests_output):
            self.assertEqual(f_parser.is_in_last_five_lines(text, test), result)


if __name__ == '__main__':
    unittest.main()
