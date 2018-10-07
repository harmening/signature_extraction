from .configs import configs
from .persister import load_model


class EmailSegmenter:

    def __init__(self):
        self.model = load_model(configs.ACTIVE_MODEL)

    def prepare_text_for_classification(self, text):
        lines = text.split('\n')
        lines = [l.strip() for l in lines if len(l.strip()) > 0]
        output = []

        for idx in range(len(lines)):
            curr = lines[idx]
            next = "" if idx == len(lines) - 1 else lines[idx + 1]
            prev = "" if idx == 0 else lines[idx - 1]
            output.append([curr, prev, next])
        return output

    def classify_lines(self, text):
        output, pred_sequence = [], ""
        lines = self.prepare_text_for_classification(text)

        for curr_line in lines:
            an_input = (text, curr_line[0], curr_line[1], curr_line[2])
            sig_pred = self.model.predict([an_input])
            pred_sequence += str(sig_pred[0])
            output.append((sig_pred, curr_line[0]))
        return output, pred_sequence

    def get_longest_signature_segment(self, seq):
        count, prev_count = 0, 0
        _range = -1, -1
        for i in range(len(seq)-1, -1, -1):
            if seq[i] == '1':
                count += 1
                if count > prev_count:
                    _range = i, i + count
            else:
                if count > prev_count:
                    _range = i+1, i+count+1
                    prev_count = count
                count = 0
        return _range

    def segment_mail(self, text):
        lines, seq = self.classify_lines(text)
        signature_ranges = self.get_longest_signature_segment(seq)

        signature_segment = lines[signature_ranges[0]:signature_ranges[1]]
        email_body = lines[:signature_ranges[0]:] + lines[signature_ranges[1]:]

        signature_segment = '\n'.join([l[1] for l in signature_segment])
        email_body = '\n'.join([l[1] for l in email_body])
        return email_body, signature_segment
