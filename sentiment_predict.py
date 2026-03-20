def predict(text, model, vectorizer):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
