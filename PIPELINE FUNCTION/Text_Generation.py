from transformers import pipeline

generator=pipeline("text-generation",model="distilgpt2")

result=generator("In this course,we will teach you how to",max_length=30,num_return_sequences=2)


print(result)

result1=generator("Today we are going to learn",max_length=20,num_return_sequences=3)

print(result1)