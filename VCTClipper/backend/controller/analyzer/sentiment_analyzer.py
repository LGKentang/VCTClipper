from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_excitement(messages):
    analyzer = SentimentIntensityAnalyzer()
    excitement_scores = []
    
    specific_terms = ["wtf", "no way"]

    for message in messages:
        lower_message = message.lower()
        
        if any(term in lower_message for term in specific_terms):
            excitement_scores.append(0.6)
        else:
            sentiment_score = analyzer.polarity_scores(message)
            excitement_scores.append(sentiment_score['compound'])
    
    print(excitement_scores)
    return calculate_average_score(excitement_scores)

def calculate_average_score(scores):
    if scores:
        return sum(scores) / len(scores)
    return 0
