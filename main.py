import summarize
import trendspottr
import twitter


def main(TOPIC_KEYWORDS):
    link = trendspottr.get_trending(TOPIC_KEYWORDS)
    text = trendspottr.retrieve_text_from(link)
    sentence_vectors = summarize.find_sentence_vectors(text)
    key_sentence = summarize.compute_centre_sentence(sentence_vectors)
    message = '"' + key_sentence + '"' + ' from ' + link
    twitter.tweet(message)


if __name__ == '__main__':
    TOPIC_KEYWORDS = 'job interview'
    main(TOPIC_KEYWORDS)