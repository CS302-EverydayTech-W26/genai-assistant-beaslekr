from gemini_client import *
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def website():
    return render_template('website.html')

@app.route('/', methods=['POST'])
def website_post():
    text = request.form['text']
    if text == "exit":
       return "Goodbye!"
    client = GeminiClient()
    return render_template('website.html') + client.generate_response(text)

def main():
    app.run()

if __name__ == "__main__":
  main()
