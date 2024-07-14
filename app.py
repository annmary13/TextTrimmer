from flask import Flask, jsonify, render_template, request
from capt import generate_summary
from main import outputsumm

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/details')
def details():
    return render_template("details.html")

@app.route('/caption')
def caption():
    return render_template("caption.html")

@app.route('/cap')
def cap():
    return render_template("cap.html")


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



@app.route('/summar', methods=['POST'])
def summar():
    data = request.get_json()
    text = data['text']
    summary = generate_summary(text)
    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)
