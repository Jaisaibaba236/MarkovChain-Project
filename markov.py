import sqlite3
from itertools import chain

class Database():
   def __init__(self):
      self.dictionary = dict()
      self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/MarkovChain-Project/MarkovChain.db')
      self.cursor = self.conn.cursor()
      self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='markov_analysis'")
      existance = self.cursor.fetchone()  # existance is a tuple  
      if existance:
         print('Table exists.')
      else:
         self.cursor.execute("CREATE TABLE markov_analysis(prefix TEXT,suffix TEXT,frequency NUMBER)")
         print('Table created successfully.')

   def data_processing(self,user_text):
       refined_data = user_text.split()
       if len(refined_data) == 1:
          word_list = list(chain(*self.cursor.execute("SELECT prefix FROM markov_analysis").fetchall()))
          if refined_data[0] in word_list:
              predicting_word = list(self.cursor.execute("SELECT suffix FROM markov_analysis WHERE prefix = ('{0}');".format(refined_data[0])).fetchone())
              if predicting_word[0] is None:
                  return ('No suffix found for this word.')  
              else:
                  return (self.cursor.execute("SELECT suffix,frequency FROM markov_analysis WHERE prefix = ('{0}') order by frequency desc limit 1;".format(refined_data[0])).fetchone())
                  #return predicting_word[0]
          else:
              self.cursor.execute("INSERT INTO markov_analysis (prefix) VALUES ('{0}');".format(refined_data[0]))
              self.conn.commit()
              return ('New word is added in Markov Dictionary.')
       else:
          for word in range(len(refined_data)-1):
              word_list = self.cursor.execute("SELECT prefix FROM markov_analysis").fetchall()
              database_prefix = list(chain(*word_list))
              if refined_data[word] in database_prefix:
                  if refined_data[word+1] in list(chain(*self.cursor.execute("SELECT suffix FROM markov_analysis WHERE prefix = ('{0}');".format(refined_data[word])).fetchall())):
                     self.cursor.execute("UPDATE markov_analysis SET frequency = frequency+1 WHERE prefix = ('{0}') AND suffix = ('{1}');".format(refined_data[word],refined_data[word+1]))
                     self.conn.commit()
                     print ('Frequency for the exiting pair is updated.') 
                  else:
                     self.cursor.execute("DELETE FROM markov_analysis WHERE prefix = ('{0}') AND suffix IS NULL;".format(refined_data[word]))
                     self.cursor.execute("INSERT INTO markov_analysis (prefix,suffix,frequency) VALUES ('{0}','{1}','{2}');".format(refined_data[word],refined_data[word+1],1))
                     self.conn.commit()
                     print ('Existing prefix: New pair is added in Markov Dictionary.')
              else:
                 self.cursor.execute("INSERT INTO markov_analysis (prefix,suffix,frequency) VALUES ('{0}','{1}','{2}');".format(refined_data[word],refined_data[word+1],1))
                 self.conn.commit()
                 print ('New prefix: New pair is added in Markov Dictionary.')         

       return ("Processed.")
