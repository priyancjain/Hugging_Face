from transformers import pipeline

ner=pipeline("ner",grouped_entities=True)

result=ner("My name is priyanshi and I work at Hugging Face in Brooklyn")

print(result)
