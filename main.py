import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(current_dir, 'aclImdb')

def preprocess_text(text):
    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    preprocess_text = ' '.join(tokens)

    return preprocess_text


def preprocess_files(directory):
    data = []
    labels = []
    for label in ['pos', 'neg']:
        subdir = os.path.join(directory, label)
        print("Subdirectory path:", subdir)
        for filename in os.listdir(subdir):
            file_path = os.path.join(subdir, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                preprocessed_text = preprocess_text(text)
                data.append(preprocessed_text)
                labels.append(label)

    return data, labels





train_data, train_labels = preprocess_files(os.path.join(dataset_dir, 'train'))

test_data, test_labels = preprocess_files(os.path.join(dataset_dir, 'test'))

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)
X_test  = vectorizer.fit_transform(test_data)


print("Training data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)