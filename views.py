import sqlite3

class Database():
   def __init__(self):
      self.conn = sqlite3.connect('/home/jaisaibaba236/Desktop/MarkovChain.db')
      self.cursor = self.conn.cursor()
      self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='markov_chain'")
      existance = self.cursor.fetchone()  # existance is a tuple  
      if existance:
         print('Table exists.')
      else:
         self.cursor.execute("CREATE TABLE markov_chain(word TEXT,f1 TEXT,f2 TEXT,f3 TEXT,f4 TEXT,f5 TEXT,f6 TEXT,f7 TEXT,f8 TEXT,f9 TEXT)")
         print('Table created successfully.')

   def data_processing(self,user_text):
         refined_data = user_text.split()
         for word in range(len(refined_data)-1):
            word_list = self.cursor.execute("SELECT word FROM markov_chain").fetchone()
            if refined_data[word] not in word_list:
                if len(refined_data) == 1:
                    self.cursor.execute("INSERT INTO markov_chain (word) VALUES ('{0}');".format(refined_data[word]))
                    self.conn.commit()
                    print('1')
                elif len(refined_data) == 2:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1) VALUES ('{0}','{1}');".format(refined_data[word],refined_data[word+1]))
                    self.conn.commit()
                    print('2')
                elif len(refined_data) == 3:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2) VALUES ('{0}','{1}','{2}');".format(refined_data[word],refined_data[word+1],refined_data[word+2]))
                    self.conn.commit()
                    print('3')
                elif len(refined_data) == 4:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3) VALUES ('{0}','{1}','{2}','{3}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3]))
                    self.conn.commit()
                    print('4')
                elif len(refined_data) == 5:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4]))
                    self.conn.commit()
                    print('5')  
                elif len(refined_data) == 6:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4,f5) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4],refined_data[word+5]))
                    self.conn.commit()
                    print('6')
                elif len(refined_data) == 7:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4,f5,f6) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4],refined_data[word+5],refined_data[word+6]))
                    self.conn.commit()
                    print('7')
                elif len(refined_data) == 8:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4,f5,f6,f7) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4],refined_data[word+5],refined_data[word+6],refined_data[word+7]))
                    self.conn.commit()
                    print('8')
                elif len(refined_data) == 9:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4,f5,f6,f7,f8) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4],refined_data[word+5],refined_data[word+6],refined_data[word+7],refined_data[word+8]))
                    self.conn.commit()
                    print('9')
                elif len(refined_data) == 10:               
                    self.cursor.execute("INSERT INTO markov_chain (word,f1,f2,f3,f4,f5,f6,f7,f8,f9) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}');".format(refined_data[word],refined_data[word+1],refined_data[word+2],refined_data[word+3],refined_data[word+4],refined_data[word+5],refined_data[word+6],refined_data[word+7],refined_data[word+8]))
                    self.conn.commit()
                    print('10')
            else:
                following_word = self.cursor.execute("SELECT * FROM markov_chain WHERE word = '{0}'".format(refined_data[word])).fetchall()
                print(following_word)

if __name__ == "__main__":
     database = Database()
     database.data_processing('HI THIS IS JUST A TESTING STRING')

