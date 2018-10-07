import os
from sklearn.externals import joblib


def save_model(model, filename):
    joblib.dump(model, os.path.join("signature_extractor", "models", filename))


def load_model(filename):
    loaded_model = joblib.load(os.path.join("signature_extractor", "models", filename))
    return loaded_model
