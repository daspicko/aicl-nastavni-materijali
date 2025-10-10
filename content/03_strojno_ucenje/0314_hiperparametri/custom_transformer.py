import numpy as np
from sklearn.base import TransformerMixin

class Median_Big_Small(TransformerMixin):
    def __init__(self):
        pass

    def fit(self, features, target=None):
        self.medians = np.median(features)
        return self

    def transform(self, features, target=None):
        return  features > self.medians
