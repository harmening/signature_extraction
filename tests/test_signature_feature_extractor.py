from unittest import TestCase
from signature_extractor.feature import SignatureFeatureExtractor


class TestSignatureFeatureExtractor(TestCase):

    def setUp(self):
        self.feature_extractor_obj = SignatureFeatureExtractor()
        self.text = """Mark, further to our conversation...\n
         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n
         or will be settled financially, however these transactions could have been set up as physical.\n
        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n
        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n
        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n
        Please call me if there are any questions regarding this note.\n
        Barry  Tycholiz\n
        Vice President, Enron North America"""
        self.input_x = [[
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'Mark, further to our conversation...', '',
                            'Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been'],
                        [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been',
                            'Mark, further to our conversation...',
                            'or will be settled financially, however these transactions could have been set up as physical.'],
                        [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'or will be settled financially, however these transactions could have been set up as physical.',
                            'Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been',
                            'The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,'],
                        [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,',
                            'or will be settled financially, however these transactions could have been set up as physical.',
                            'and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%'],
                        [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%',
                            'The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,',
                            'load factor and settlement would be on 100% of the volume regardless as to what physically flowed.'],
                        [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'load factor and settlement would be on 100% of the volume regardless as to what physically flowed.',
                            'and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%',
                            'Please call me if there are any questions regarding this note.'], [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'Please call me if there are any questions regarding this note.',
                            'load factor and settlement would be on 100% of the volume regardless as to what physically flowed.',
                            'Barry  Tycholiz'], [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'Barry  Tycholiz', 'Please call me if there are any questions regarding this note.',
                            'Vice President, Enron North America'], [
                            'Mark, further to our conversation...\n\n         Mercado transacted with Enron North America under the terms and conditions of a financial transaction and these transactions have been\n\n         or will be settled financially, however these transactions could have been set up as physical.\n\n        The structure of the transaction changes as a result of a few variables, including the price,day of cash settlement,\n\n        and curtailment issues on San Jan deliveries which would then automatically convert the fixed price portion to 100%\n\n        load factor and settlement would be on 100% of the volume regardless as to what physically flowed.\n\n        Please call me if there are any questions regarding this note.\n\n        Barry  Tycholiz\n\n        Vice President, Enron North America',
                            'Vice President, Enron North America', 'Barry  Tycholiz', '']]

    def tearDown(self):
        pass

    def test_line_to_vec(self):
        line = "Barry Tycholiz"
        output = [0, 0, 0, 0, 0, 2, 0, 0, 0]
        self.assertEqual(self.feature_extractor_obj.line_to_vec(line, self.text), output)

    def test_transform(self):
        output = [[0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1]]

        self.assertTrue((self.feature_extractor_obj.transform(self.input_x) == output).all())
