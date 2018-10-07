import nltk


def get_from_file(fname):
    with open(fname, 'r') as myfile:
        data = myfile.read()
    sent_text = '\n'.join([l for l in nltk.sent_tokenize(data)])
    return sent_text


def get_from_json():
    pass


def get_from_html():
    pass