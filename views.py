from django.shortcuts import render
from django.views.generic import TemplateView
import sqlite3

# Create your views here
class HomePageView(TemplateView):
   def get(self, request, **kwargs):
      return render(request, 'index.html', context=None)


class Database():

     def __init__(self):
        self.word_dictionary = dict()
        self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/markov_project/MarkovChain.db')
        print(type(self.conn))
        
     def db_connection(self):
#        connection = sqlite3.connect(db_file)
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Markov'")
        existance = cursor.fetchone()
        if existance:
#            cursor.execute("INSERT INTO Markov VALUES(1,'Audi',52642)")
             print('Table exists.')
        else:
             cursor.execute("CREATE TABLE MARKOV(Word TEXT, Following_Word TEXT)")
             print('Table created successfully.')
        
#       cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Markov'")
#       rows = cur.fetchone()
#       for row in rows:
#            print (row)
#       self.conn.close()
 
     def word_matchcase(self,user_input):
        sentence_words = user_input.split()

        for word in range(len(sentence_words)-1):
            cursor.execute('SELECT Word FROM Markov WHERE Word ='+str(sentence_words[word]))
            word_list = cursor.fetchone()

            if sentence_words[word] not in word_list:
                 cursor.execute('INSERT INTO Markov (Word) VALUES('+str(sentence_words[word])
    cursor.execute('INSERT INTO Markov (Following_Word) VALUES('+str(sentence_words[word+1])+') WHERE Word =str(sentence_words[word])')
#                 self.conn[sentence_words[word]] = sentence_words[word+1]
            else:
                 if self.conn[sentence_words[word]] == sentence_words[word+1]:
                     print(self.conn[sentence_words[word]])
                 else:
                     self.conn[sentence_words[word]] = sentence_words[word+1]
        print(self.conn)

#if __name__ == '__main__':
#    db_connection('/home/jaisaibaba236/Desktop/markov_project/MarkovChain.db')      
  

database_init = Database() 
database_init.db_connection()

database_init.word_matchcase('this is a python tutorial and this is a very interesting development language as compared to other development languages')

