import os
import nltk
import numpy as np
from os import listdir
from os.path import isfile, join


signatures_dataset_path = os.path.join("signature_extractor", "datasets", "signatures")
data_files = [f for f in listdir(signatures_dataset_path) if isfile(join(signatures_dataset_path, f)) if f != '.DS_Store']


def label_email_text(fname):
    # add line position in message
    X, y = [], []
    with open(fname, 'r') as myfile:
        data = myfile.read()
        lines = nltk.sent_tokenize(data)
        text = '\n'.join([txt for txt in lines])
        for l_idx in range(len(lines)):
            prev_line = "" if l_idx == 0 else lines[l_idx - 1]
            next_line = "" if l_idx+1 > len(lines)-1 else lines[l_idx+1]
            if lines[l_idx].find('#sig#') == -1:
                y.append('other')
            else:
                y.append('sig')
            X.append((text.replace("#sig#", ""), lines[l_idx].replace("#sig#", ""), prev_line, next_line))
    return X, y


def load_signatures_dataset():
    x, y = [], []
    for f in data_files:
        file = os.path.join(signatures_dataset_path, f)
        loc_x, loc_y = label_email_text(file)
        x += loc_x
        y += loc_y
    return np.array(x), np.array(y)

