import string

# Define a simple list of stopwords
stopwords = [
    "the", "is", "in", "and", "to", "of", "a", "an", "on", "for", "with", 
    "that", "this", "it", "as", "at", "by", "from"
]

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove stopwords
    words = text.split()
    cleaned_words = [word for word in words if word not in stopwords]
    
    # Join back to string
    return " ".join(cleaned_words)

# Test the cleaner
print("Enter a sentence:")
input_text = input()

cleaned_text = clean_text(input_text)

print("\nOriginal Text:")
print(input_text)

print("\nCleaned Text:")
print(cleaned_text)