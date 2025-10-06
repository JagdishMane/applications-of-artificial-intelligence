### Sentiment Analysis
from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
result=sentiment("I like Hugging Face")
print(result)

### Classifier
classifier = pipeline("text-classification")
result = classifier("The moview was Fantastic !!")
print(result)


### Question Answering
qa = pipeline("question-answering")
result = qa({
    "question": "Where was Barack Obama born ?"
    "context": "Barak Oboama was bo....."
})
print(result)
