
import nltk
import spacy
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

nlp = spacy.load("en_core_web_sm")

patterns = [
    (r"hi|hello|hey", ["Hello, how can I help you today?", "Hi! How can I assist you?"]),
    (r"what is your name?", ["I am a chatbot created using NLP.", "You can call me ChatBot."]),
    (r"how are you?", ["I'm just a program, but I'm doing well, thanks for asking!", "I'm fine, how about you?"]),
    (r"quit", ["Goodbye! Have a great day!"]),
    (r"your (favorite|best) (color|food|movie)", ["I don't have preferences, but I can help you with some recommendations."]),
    (r"(.*) (weather|forecast) (.*)", ["I don't have access to live weather data, but I can help you find weather sites!"]),
    (r"(.*)", ["I'm sorry, I don't understand that. Could you clarify?"]),
]

chatbot = Chat(patterns, reflections)

def process_with_nltk(query):
    tokens = word_tokenize(query)
    print("NLTK Tokenized Words:", tokens)
    return tokens

def process_with_spacy(query):
    doc = nlp(query)
    print("spaCy Tokens and POS Tags:")
    for token in doc:
        print(f"Text: {token.text}, POS: {token.pos_}")
    return doc

def chatbot_interface():
    print("Hello! I'm your chatbot. Type 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")

        #Tokenization
        nltk_tokens = process_with_nltk(user_input)

        # Part of speech tagging
        process_with_spacy(user_input)

        # Get response from the chatbot
        if user_input.lower() == "quit":
            print("Goodbye! Have a great day!")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)

if __name__ == "__main__":
    chatbot_interface()
