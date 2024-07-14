import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def outputsumm(input_text, no_of_sentences=5):  # Default to 5 sentences if not provided
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(input_text)
    f = dict()
    for i in words:
        i = i.lower()
        if i in stopWords:
            continue
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    sentences = sent_tokenize(input_text)
    fsent = dict()
    for j in sentences:
        for x, y in f.items():
            if x in j.lower():
                if j in fsent:
                    fsent[j] += y
                else:
                    fsent[j] = y
    count = 0
    for k in fsent:
        count += fsent[k]
    average = int(count / len(fsent))
    output_text = ''
    for p in sentences:
        if (p in fsent) and (fsent[p] > (1.2 * average)):
            output_text += " " + p
    return output_text


def outputsumm(input_text, no_of_sentences=5):  # Default to 5 sentences if not provided
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(input_text)
    f = dict()
    for i in words:
        i = i.lower()
        if i in stopWords:
            continue
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    sentences = sent_tokenize(input_text)
    fsent = dict()
    for j in sentences:
        for x, y in f.items():
            if x in j.lower():
                if j in fsent:
                    fsent[j] += y
                else:
                    fsent[j] = y
    count = 0
    for k in fsent:
        count += fsent[k]
    average = int(count / len(fsent))
    output_text = ''
    for p in sentences:
        if (p in fsent) and (fsent[p] > (1.2 * average)):
            output_text += " " + p
    # Limit summary to no_of_sentences
    summarized_sentences = sent_tokenize(output_text)[:no_of_sentences]
    summarized_text = ' '.join(summarized_sentences)
    return summarized_text


































from flask import Flask, redirect, url_for, request, render_template
from main import outputsumm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/caption')
def caption():
    return render_template('caption.html')

@app.route('/output', methods=['POST'])
def output():
    if request.method == 'POST':
        textvalue = request.form.get("textarea", None)
        if textvalue:
            res = outputsumm(textvalue)
            return render_template('Output_Content.html', res=outputsumm(textvalue))
        else:
            return "No input provided."

if __name__ == '__main__':
    app.run(debug=True)

















    from flask import Flask, render_template, request
from main import outputsumm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        textvalue = request.form.get("textarea", None)
        no_of_sentences = int(request.form.get("no_of_sentences", 5))  # Default to 5 if not provided
        if textvalue:
            res = outputsumm(textvalue, no_of_sentences)  # Pass no_of_sentences to outputsumm
            print("Summary:", res)  # Print the summary for debugging
            return render_template('output_content.html', res=res)
        else:
            return "No input provided."

if __name__ == '__main__':
    app.run(debug=True)























import nltk
nltk.download('punkt')


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def outputsumm(input_text):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(input_text)
    f = dict()
    for i in words:
        i = i.lower()
        if i in stopWords:
            continue
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    sentences = sent_tokenize(input_text)
    fsent = dict()
    for j in sentences:
        for x, y in f.items():
            if x in j.lower():
                if j in fsent:
                    fsent[j] += y
                else:
                    fsent[j] = y
    count = 0
    for k in fsent:
        count += fsent[k]
    average = int(count / len(fsent))
    output_text = ''
    for p in sentences:
        if (p in fsent) and (fsent[p] > (1.2 * average)):
            output_text += " "+p
    return output_text








