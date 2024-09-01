
from sklearn.feature_extraction.text import TfidfVectorizer

class VectorizationPipeline:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)

