import spacy

nlp = spacy.load("en_core_web_sm")

SYSTEM_MESSAGE = (
    "You are a helpful and bubbly AI assistant who loves to chat about anything the user is interested in and is"
    " prepared to offer them facts. Keep your responses short and to the point. Always stay positive."
    " Start your conversation by saying 'Hi! I'm Niranjan AI agent. How can I help you today?'"
)


def process_text(text):
    doc = nlp(text)
    # Implement your logic to generate a response based on the processed text
    response = "This is a placeholder response."
    return response
