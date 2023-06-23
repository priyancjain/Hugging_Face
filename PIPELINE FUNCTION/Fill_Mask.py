from transformers import pipeline

unmasker=pipeline("fill-mask")

result=unmasker("This course will teach you all about <mask> models.",top_k=2)

print(result)

result1=unmasker("what is my <mask> age",top_k=3)

print(result1)