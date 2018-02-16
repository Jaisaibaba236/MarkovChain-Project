from flask import Flask, render_template, request
app = Flask(__name__)
from markov import Database
database = Database()

@app.route('/')
def user_form():
   return render_template('markov.html')

@app.route('/markov_output', methods=['POST'])
def markov_processing():
   user_input = request.form["sequence"]
   return database.data_processing(user_input)

if __name__ == '__main__':
   app.run()
