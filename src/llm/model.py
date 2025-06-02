from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch


class AutismModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def predict_autism_level(self, messages):
        inputs = self.tokenizer(messages, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.softmax(outputs.logits, dim=-1)
        return predictions.numpy().mean()

    def measure_autism(self, user_messages):
        autism_levels = self.predict_autism_level(user_messages)
        return autism_levels.mean(axis=0)  # Average autism level across messages
