from transformers import pipeline

summarizer=pipeline("summarization")

result=summarizer('''State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX.

🤗 Transformers provides APIs and tools to easily download and train state-of-the-art pretrained models. Using pretrained models can reduce your compute costs, carbon footprint, and save you the time and resources required to train a model from scratch. These models support common tasks in different modalities, such as:

📝 Natural Language Processing: text classification, named entity recognition, question answering, language modeling, summarization, translation, multiple choice, and text generation.
🖼️ Computer Vision: image classification, object detection, and segmentation.
🗣️ Audio: automatic speech recognition and audio classification.
🐙 Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, and visual question answering.

🤗 Transformers support framework interoperability between PyTorch, TensorFlow, and JAX. This provides the flexibility to use a different framework at each stage of a model’s life; train a model in three lines of code in one framework, and load it for inference in another. Models can also be exported to a format like ONNX and TorchScript for deployment in production environments.'''   )

print(result)

result1=summarizer('''Amazon.com, Inc.[1] (/ˈæməzɒn/ AM-ə-zon UK also /ˈæməzən/ AM-ə-zən) is an American multinational technology company focusing on e-commerce, cloud computing, online advertising, digital streaming, and artificial intelligence. It has been often referred to as "one of the most influential economic and cultural forces in the world",[5] and is often regarded as one of the world's most valuable brands.[6] It is often considered as one of the Big Five American technology companies, alongside Alphabet (parent company of Google), Apple, Meta (formerly Facebook Inc.) and Microsoft.

Amazon was founded by Jeff Bezos from his garage in Bellevue, Washington,[7] on July 5, 1994. Initially an online marketplace for books, it has expanded into a multitude of product categories, a strategy that has earned it the moniker The Everything Store.[8] It has multiple subsidiaries including Amazon Web Services (cloud computing), Zoox (autonomous vehicles), Kuiper Systems (satellite Internet), and Amazon Lab126 (computer hardware R&D). Its other subsidiaries include Ring, Twitch, IMDb, and Whole Foods Market. Its acquisition of Whole Foods in August 2017 for US$13.4 billion substantially increased its footprint as a physical retailer.[9]

Amazon has earned a reputation as a disruptor of well-established industries through technological innovation and "aggressive" reinvestment of profits into capital expenditures.[10][11][12][13] As of 2023, it is the world's largest online retailer and marketplace, smart speaker provider, cloud computing service through AWS,[14] live-streaming service through Twitch, and Internet company as measured by revenue and market share.[15] In 2021, it surpassed Walmart as the world's largest retailer outside of China, driven in large part by its paid subscription plan, Amazon Prime, which has over 200 million subscribers worldwide.[16][17] It is the second-largest private employer in the United States.[18] ''')

print(result1)