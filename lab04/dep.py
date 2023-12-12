import os
import math


def get_spam_list():
    return os.listdir("./spam_data/train/spam")


def get_ham_list():
    return os.listdir("./spam_data/train/ham")


class Container:
    def __init__(self):
        self.count = 0
        self.words = {}


def init():
    data_spam = Container()
    data_ham = Container()
    spam_directory = "./spam_data/train/spam/"
    ham_directory = "./spam_data/train/ham/"
    count = 0

    files = get_spam_list()
    for filename in files:
        f = spam_directory + filename

        f = open(f, 'rb')
        try:
            text = f.read().decode('utf-8', errors='replace').split()
            count += 1
            for word in text:
                word = word.lower()
                if data_spam.words.get(word) is None:
                    data_spam.words.update({word: 1})
                else:
                    data_spam.words[word] += 1
            data_spam.count += len(text)
        except Exception as e:
            print(f"An unexpected error occurred in init: {e}")

        f.close()
    files = get_ham_list()
    for filename in files:
        f = ham_directory + filename

        f = open(f, 'rb')
        try:
            text = f.read().decode('utf-8', errors='replace').split()
            count += 1
            for word in text:
                word = word.lower()
                if data_ham.words.get(word) is None:
                    data_ham.words.update({word: 1})
                else:
                    data_ham.words[word] += 1

            data_ham.count += len(text)
        except Exception as e:
            print(f"An unexpected error occurred in init: {e}")

        f.close()

    for word, c in data_spam.words.items():
        data_spam.words[word] = c / data_spam.count
    for word, c in data_ham.words.items():
        data_ham.words[word] = c / data_ham.count
    return [data_spam, data_ham]


def classify(spam, ham, path):
    files = os.listdir(path)
    total_count = 0
    detected_count = 0

    for filename in files:
        f = path + filename
        f = open(f, 'rb')

        try:
            text = f.read().decode('utf-8', errors='replace').split()
            total_count += 1
            prob_spam = sum(math.log(spam.words.get(word, 1 / spam.count)) for word in text)
            prob_ham = sum(math.log(ham.words.get(word, 1 / ham.count)) for word in text)

            if prob_spam > prob_ham:
                detected_count += 1
        except Exception as e:
            print(f"An unexpected error occurred in classify: {e}")

        f.close()
    return [total_count, detected_count]
