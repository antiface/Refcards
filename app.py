from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_card, get_cards

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        pass
        
        
    if request.method == 'POST':
        created_at = request.form.get('created_at')
        context = request.form.get('context')
        refcard = request.form.get('refcard')
        create_card(context, refcard)

    refcards = get_cards()


    return render_template('index.html', refcards=refcards)

if __name__ == '__main__':
    app.run(debug=True)
