# Movie Review Analyzer

# Predefined positive and negative words
positive_words = ["good", "great", "amazing", "excellent", "awesome", "love", "fantastic", "nice", "super"]
negative_words = ["bad", "terrible", "awful", "worst", "boring", "hate", "poor", "disappointing"]

# Function to analyze sentiment
def analyze_sentiment(review):
    review = review.lower()
    pos_count = sum(word in review for word in positive_words)
    neg_count = sum(word in review for word in negative_words)
    
    if pos_count > neg_count:
        return "Positive 😊"
    elif neg_count > pos_count:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Store reviews
reviews = []

# Input 5 reviews
for i in range(5):
    review = input(f"Enter review {i+1}: ")
    reviews.append(review)

# Analyze and print results
print("\n--- Sentiment Analysis Results ---")
for i, review in enumerate(reviews):
    sentiment = analyze_sentiment(review)
    print(f"Review {i+1}: {sentiment}")