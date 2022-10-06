#hello.py

from flask import Flask, render_template, request
import markovify
import random



app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html', flag=False)


@app.route('/haiku', methods=["POST"])
def display_haiku():
    with open("static/haiku_wakatigaki.txt") as f:
        lines = f.readlines()
        random.shuffle(lines)
        #print(lines[:4])
        texts = "".join(lines[i] for i in range(len(lines)))

    model = markovify.NewlineText(texts, state_size=2)
    haiku = model.make_sentence(tries=100)
    
    dict = {}    
    
    if haiku is None:
        dict["haiku"] = "詠めませんでした"
        
        #print("無理")
    else:
        
        dict["haiku"] =  ''.join(haiku.split())[:-1]#句点を除く
        
    
    #return render_template('result.html', dict=dict)
    return render_template('index.html', flag=True, dict=dict)
if __name__ == "__main__":
    app.run(debug=True)