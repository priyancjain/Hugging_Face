from transformers import pipeline

classifier =pipeline("zero-shot-classification")

result=classifier("This is a course about the Transformers library",candidate_labels=["eduction","politics","business"])

print(result)

result1=classifier("This is a manufacturing company I want to sell it",candidate_labels=["eduction","politics","business"])

print(result1)

result2=classifier("Hey this is my country I am the president",candidate_labels=["eduction","politics","business"])

print(result2)