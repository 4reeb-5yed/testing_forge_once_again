import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Define the intents and responses
intents = {
    'greeting': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'goodbye', 'see you later'],
    'thanks': ['thank you', 'thanks', 'appreciate it']
}

responses = {
    'greeting': "Hey there!",
    'goodbye': "Bye, have a great day!",
    'thanks': "You're welcome!"
}

# Define the chatbot class
class Chatbot:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
        self.model = LogisticRegression()

    def train(self, intents, responses):
        # Prepare the training data
        X = []
        y = []
        for intent, phrases in intents.items():
            for phrase in phrases:
                X.append(phrase)
                y.append(intent)

        # Fit the model
        X_vectorized = self.vectorizer.fit_transform(X)
        self.model.fit(X_vectorized, y)

    def respond(self, user_input):
        # Preprocess the user input
        user_input_vectorized = self.vectorizer.transform([user_input])

        # Predict the intent
        intent = self.model.predict(user_input_vectorized)[0]

        # Generate the response
        return responses[intent]

# Example usage
chatbot = Chatbot()
chatbot.train(intents, responses)

user_input = "Hello"
response = chatbot.respond(user_input)
print(response)  # Output: "Hey there!"
