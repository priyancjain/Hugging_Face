from transformers import pipeline

q_a= pipeline("question-answering")

result=q_a(question="Where do I work ?",context="My name is Priyanshi and I work at 31 vijay nagar Extension")

print(result)

result1=q_a(question='What is my pet name?',context="Hey this is my pet his name is Ruby")

print(result1)