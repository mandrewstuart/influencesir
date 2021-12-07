import numpy as np
from spacy.lang.en import English


def find_sentence_vectors(text):
    nlp = English()
    nlp.add_pipe('sentencizer')
    nlp.add_pipe('tok2vec')
    nlp.initialize()
    doc = nlp(text)
    sentences_with_vectors = list(doc.sents)
    return sentences_with_vectors


def compute_centre_sentence(sentences_with_vectors):
    vectors = np.asarray([s.vector for s in sentences_with_vectors])
    mean = np.mean(vectors)
    distance_function = np.linalg.norm
    distances = [distance_function(mean, vector) for vector in vectors]
    index = np.argmin(distances)
    return str(sentences_with_vectors[index])
