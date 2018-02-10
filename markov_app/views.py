from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView
import sqlite3
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

# Create your views here
class HomePageView(TemplateView):
   def get(self, request, *args, **kwargs):
      return render(request, 'index.html')

class Database():

   def __init__(self):
      self.word_dictionary = dict()
      self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/markov_project/MarkovChain.db')
      self.cursor = self.conn.cursor()
      self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='MARKOV'")
      existance = self.cursor.fetchone()  # existance is a tuple  
      if existance:
         print('Table exists.')
      else:
         cursor.execute("CREATE TABLE MARKOV(Word TEXT, Following_Word TEXT)")
         print('Table created successfully.')

#This funciton is not in use as of now
   def word_matchcase(self,user_input):
      sentence_words = user_input.split()

      for word in range(len(sentence_words)-1):
         word_list = self.cursor.execute("SELECT WORD FROM MARKOV").fetchall()
         if sentence_words[word] not in word_list:
            self.cursor.execute("INSERT INTO MARKOV VALUES ('{0}','{1}');".format(sentence_words[word],sentence_words[word+1]))
            self.conn.commit()
         else: 
            following_word = self.cursor.execute("SELECT FOLLOWING_WORD FROM MARKOV WHERE WORD = '{0}'".format(sentence_words[word])).fetchall()
            print(following_word)

   @app.route('/localhost/request',methods=['POST']) 
   def database_update(self,request):
      with app.test_request_context():
         print(app.test_request_context())
         start_word = request.form.get('starting_word')
         print(start_word)
         for word in range(len(start_word)-1):
            word_list = self.cursor.execute("SELECT WORD FROM MARKOV").fetchall()
            if start_word[word] not in word_list:
                self.cursor.execute("INSERT INTO MARKOV VALUES ('{0}','{1}');".format(start_word[word],start_word[word+1]))
                self.conn.commit()
            else: 
                following_word = self.cursor.execute("SELECT FOLLOWING_WORD FROM MARKOV WHERE WORD = '{0}'".format(start_word[word])).fetchone()
                print(following_word)
         #Issue in below line maybe
         return render_template('index.html')

database_init = Database()
#database_init.database_update()
