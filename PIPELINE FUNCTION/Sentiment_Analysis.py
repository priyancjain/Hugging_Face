from transformers import pipeline

classifier=pipeline("sentiment-analysis")

res=classifier("I'have been waiting for a HuggingFace course my whole life")

print(res)

p=classifier("keep shut your mouth")

print(p)

expression=classifier("How are you?")
print(expression)

expression1=classifier("How are you!")
print(expression1)