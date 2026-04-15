from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
messages = [
    "Win a free lottery now",
    "Congratulations you won a prize",
    "Call me when you are free",
    "Let's meet for lunch",
    "Urgent! claim your reward",
    "Are you coming today?"
]

labels = ["spam", "spam", "ham", "ham", "spam", "ham"]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test)

# Test with new message
new_msg = ["Free entry in a contest"]
new_X = vectorizer.transform(new_msg)

prediction = model.predict(new_X)
print("\nNew Message Prediction:", prediction[0])