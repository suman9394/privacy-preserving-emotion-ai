from textblob import TextBlob

def extract_metadata(text):

    blob = TextBlob(text)

    sentiment = blob.sentiment.polarity

    metadata = {
        "length": len(text),
        "word_count": len(text.split()),
        "sentiment_score": sentiment,
        "exclamation_marks": text.count("!"),
        "question_marks": text.count("?")
    }

    return metadata