import csv
import nltk
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.util import ngrams

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]
    # Get n-grams
    ngrams_list = list(ngrams(tokens, 2))
    # Flatten n-grams to single tokens
    tokens += [token1 + " " + token2 for token1, token2 in ngrams_list]
    return tokens

# Load CSV file
input_file = "questions.csv"  # Replace with your input file path
output_file = "output.csv"  # Replace with your output file path
questions = []
with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        questions.extend(preprocess_text(row[0]))

# Find repeated questions
question_freq_dist = FreqDist(questions)
repeated_questions = [question for question, count in question_freq_dist.items() if count > 1]

# Save unique questions to separate CSV file
unique_questions = list(set(questions))
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for question in unique_questions:
        if question not in repeated_questions:
            writer.writerow([question])
