from flask import Flask, render_template, request
from newspaper import Article
from transformers import BartForConditionalGeneration, BartTokenizer

app = Flask(__name__)
model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_article(article):
    # Load BART model and tokenizer

    # Tokenize and encode the article
    inputs = tokenizer.encode(article, return_tensors='pt',
max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, num_beams=4, max_length=150,
early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', show_summary=False)

    elif request.method == 'POST':
        url = request.form['url']
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        title = article.title

        summary = summarize_article(text)
        return render_template('index.html', summary=summary, text=text, show_summary=True, title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
