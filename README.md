# Chatbot Using ChatterBot





- Interactive AI chatbot
- Trained using ChatterBot English Corpus
- Responds to user queries
- Simple command-line interface
- Easy to customize and extend


- Python
- ChatterBot
- ChatterBot Corpus
- spaCy
- PyYAML



```
CHATBOT-USING-CHATTERBOT/
│── app.py
│── requirements.txt
│── README.md
└── screenshots/
    └── output.png
```



1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```


```bash
python app.py
```



```
🤖 Chatbot is ready! Type 'exit' to quit.

You: Hello
Bot: Hello!

You: What is your name?
Bot: I am Assistant.

You: exit
Bot: Goodbye!
```



Developed for **CodTech Internship - Task 4**
