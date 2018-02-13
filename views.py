import sqlite3

class Database():
   def __init__(self):
      self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/MarkovChain.db')
      self.cursor = self.conn.cursor()
      self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='markov_analysis'")
      existance = self.cursor.fetchone()  # existance is a tuple  
      if existance:
         print('Table exists.')
      else:
         self.cursor.execute("CREATE TABLE markov_analysis(word TEXT,following_word TEXT,frequency INTEGER )")
         print('Table created successfully.')

   def data_processing(self,user_text):
         refined_data = user_text.split()
         if len(refined_data) == 1:
              word_list = self.cursor.execute("SELECT word FROM markov_analysis").fetchall()
              if refined_data[0] in word_list:
                 predicting_word = self.cursor.execute("SELECT following_word FROM markov_analysis where word = refined_data[0]")
                 print(predicting_word)
              else:
                 self.cursor.execute("INSERT INTO markov_analysis (word) VALUES ('{0}');".format(refined_data[0]))
                 self.conn.commit()
         else:
              for word in range(len(refined_data)-1):
                  dictionary[refined_data[word]] = refined_data[word+1]
                  word_list = self.cursor.execute("SELECT word FROM markov_analysis").fetchall()
              for key,value in dictionary.items():
                  if key not in word_list:
                      self.cursor.execute("INSERT INTO markov_analysis (word,following_word) VALUES ('{0}','{1}');".format(key,value))
                      self.conn.commit()               
           
if __name__ == "__main__":
     database = Database()
     database.data_processing('HI THIS IS JUST A TESTING STRING')

