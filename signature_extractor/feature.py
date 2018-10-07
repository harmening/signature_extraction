import numpy as np
from sklearn.base import TransformerMixin

from .preprocessing import feature_parser as txt_prep


class SignatureFeatureExtractor(TransformerMixin):

    def line_to_vec(self, l, t):
        curr_res = list()
        curr_res.append(txt_prep.contains_phone(l))
        curr_res.append(txt_prep.contains_signature_word(l))
        curr_res.append(txt_prep.has_only_quotes(l))
        curr_res.append(txt_prep.contains_email(l))
        curr_res.append(txt_prep.has_url(l))
        curr_res.append(txt_prep.count_named_entities(l))
        curr_res.append(txt_prep.is_under_closing_phrase(t, l))
        curr_res.append(txt_prep.is_in_second_part(t, l))
        curr_res.append(txt_prep.is_in_last_five_lines(t, l))

        curr_res = [int(elem) for elem in curr_res]
        return curr_res

    def transform(self, X, **kwargs):
        result = []

        for (t, l, prevLine, nextLine) in X:
            curr_line_vec = self.line_to_vec(l, t)
            prev_line_vec = self.line_to_vec(prevLine, t)
            next_line_vec = self.line_to_vec(nextLine, t)
            curr_res = next_line_vec + prev_line_vec + curr_line_vec
            result.append(curr_res)
        return np.array(result)

    def fit(self, X, y=None, **kwargs):
        return self

    def get_params(self, **kwargs):
        return {}
