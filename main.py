import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump, load

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


if os.path.exists('tfidf_model.joblib') and os.path.exists('classifier.joblib'):
    print("Loading pre-trained model...")
    vectorizer = load('tfidf_model.joblib')
    classifier = load('classifier.joblib')
else:
    print("Training and saving the model...")
    train_data, train_labels = preprocess_files(os.path.join(dataset_dir, 'train'))

    vectorizer = TfidfVectorizer()
    x_train = vectorizer.fit_transform(train_data)

    # Train your classifier here (for example, using Logistic Regression)
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression()
    classifier.fit(x_train, train_labels)

    # Save the trained models
    dump(vectorizer, 'tfidf_model.joblib')
    dump(classifier, 'classifier.joblib')


new_comment = "This was such a funny episode. genuinely was laughing through the whole thing"

preprocessed_comment = preprocess_text(new_comment)

X_new = vectorizer.transform([preprocessed_comment])

predicted_label = classifier.predict(X_new)

if predicted_label[0] == 'pos':
    print("The sentiment of the new comment is positive.")
else:
    print("The sentiment of the new comment is negative.")



# train_data, train_labels = preprocess_files(os.path.join(dataset_dir, 'train'))

# test_data, test_labels = preprocess_files(os.path.join(dataset_dir, 'test'))

# vectorizer = TfidfVectorizer()
# X_train = vectorizer.fit_transform(train_data)
# X_test  = vectorizer.fit_transform(test_data)


# print("Training data shape:", X_train.shape)
# print("Testing data shape:", X_test.shape)