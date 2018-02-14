import sqlite3
from itertools import chain

class Database():
   def __init__(self):
      self.dictionary = dict()
      self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/MarkovChain.db')
      self.cursor = self.conn.cursor()
      self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='markov_analysis1'")
      existance = self.cursor.fetchone()  # existance is a tuple  
      if existance:
         print('Table exists.')
      else:
         self.cursor.execute("CREATE TABLE markov_analysis1(word TEXT,following_word TEXT,frequency NUMBER)")
         print('Table created successfully.')

   def data_processing(self,user_text):
       refined_data = user_text.split()
       if len(refined_data) == 1:
          word_list = list(chain(*self.cursor.execute("SELECT word FROM markov_analysis1").fetchall()))
          print(word_list)
          if refined_data[0] in word_list:
              predicting_word = list(self.cursor.execute("SELECT following_word FROM markov_analysis1 WHERE word = ('{0}');".format(refined_data[0])).fetchone())
              print(predicting_word)
          else:
              self.cursor.execute("INSERT INTO markov_analysis1 (word) VALUES ('{0}');".format(refined_data[0]))
              self.conn.commit()
       else:
          for word in range(len(refined_data)-1):
              self.dictionary[refined_data[word]] = refined_data[word+1]
              word_list = self.cursor.execute("SELECT word FROM markov_analysis1").fetchall()
              database_prefix = list(chain(*word_list))
          print(self.dictionary)
          for key,value in self.dictionary.items():
              print(key,value)
              if key in database_prefix:
                  if value in list(self.cursor.execute("SELECT following_word FROM markov_analysis1 WHERE word = ('{0}');".format(key)).fetchone()):
                     self.cursor.execute("UPDATE markov_analysis1 SET frequency = frequency+1 WHERE word = ('{0}');".format(key))
                     self.conn.commit()  
                     print('Frequency for the exiting pair is updated.') 
                  else:
                     self.cursor.execute("INSERT INTO markov_analysis1 (word,following_word,frequency) VALUES ('{0}','{1}','{2}');".format(key,value,1))
                     self.conn.commit()
                     print('New word is added to the existing word.')
              else:
                 self.cursor.execute("INSERT INTO markov_analysis1 (word,following_word,frequency) VALUES ('{0}','{1}','{2}');".format(key,value,1))
                 print('New pair is added in storage.')
                 self.conn.commit()             
           
if __name__ == "__main__":
   database = Database()
   database.data_processing('Hi')

