import numpy as np

from signature_extractor.persister import save_model
from signature_extractor.datasets import dataset_loader as d_loader
from signature_extractor.feature import SignatureFeatureExtractor

from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


def build_pipeline():
    output_pipeline = Pipeline([
        ('features', SignatureFeatureExtractor()),
        ('clf', KNeighborsClassifier(weights='distance'))
    ])

    return output_pipeline


def get_gridsearch_params():
    n_neighbors = [2, 3, 5, 7, 10]
    param_grid = {'clf__n_neighbors': n_neighbors}
    return param_grid


def train_model(data, pipeline, parameters):
    X_train, y_train_bin = data
    grid_search = GridSearchCV(pipeline, parameters, scoring='f1', verbose=1, n_jobs=-1)
    grid_search.fit(X_train, y_train_bin)

    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))
    return grid_search.best_estimator_


def evaluate_model(model, data):
    X_test, y_test = data
    y_pred = model.predict(X_test)
    score = classification_report(y_test, y_pred)
    print("-" * 25)
    print("Model Evaluation:")
    print("Accuracy Score:", score)
    print("-" * 25)
    return score


def downsample_majority_class(X, y):
    mask_sig = y == "sig"
    X_sig, y_sig = X[mask_sig], y[mask_sig]

    mask_oth = y == "other"
    X_oth, y_oth = X[mask_oth], y[mask_oth]
    X_oth, y_oth = shuffle(X_oth, y_oth)
    X_oth, y_oth = X_oth[:len(X_sig)], y_oth[:len(y_sig)]

    X_new = np.concatenate([X_sig, X_oth], axis=0)
    y_new = np.concatenate([y_sig, y_oth], axis=0)

    return shuffle(X_new, y_new)


if __name__ == '__main__':
    print("Loading signatures dataset")
    X, y = d_loader.load_signatures_dataset()

    print("Downsampling majority class")
    X, y = downsample_majority_class(X, y)

    print("Preparing data for training")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=124)
    label_binarizer = LabelBinarizer().fit(y)
    print("X_train size:", len(X_train), "X_test size:", len(X_test))

    print("Binarizing target label")
    y_train_bin = label_binarizer.transform(y_train)
    y_test_bin = label_binarizer.transform(y_test)
    print(y_train[0], y_train_bin[0])

    print("Building pipeline")
    pipeline = build_pipeline()

    print("Training classification model")
    model = train_model((X_train, y_train_bin), pipeline, get_gridsearch_params())

    print("Evaluating trained model")
    _ = evaluate_model(model, (X_test, y_test_bin))

    print("Saving model")
    _ = save_model(model, "signature_model")
