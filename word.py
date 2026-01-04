import pandas as pd
import random
import pyttsx3
data=pd.read_csv("./data/french_words.csv")
learned_data=pd.read_csv("./data/french_learned_words.csv")
data_dictionary=data.to_dict("records")
class Word:
    def __init__(self):
        self.learned_word = learned_data.to_dict("records")
        self.data={}
        self.generate_word()
        self.flipped=False
        self.english_word=self.data["English"]
        self.french_word=self.data["French"]
        self.empty=False
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 100)

    def flip(self):
        self.flipped=not self.flipped
        return self.flipped

    def learn(self,word):
        self.learned_word.append(word)

    def create_file(self):
        print(self.learned_word)
        pd.DataFrame(self.learned_word).to_csv('./data/french_learned_words.csv',index=False)

    def generate_word(self):
        if len(self.learned_word) >= len(data_dictionary):
            self.empty = True
            return
        self.data = random.choice(data_dictionary)
        self.flipped=False
        while self.data in self.learned_word:
            self.data = random.choice(data_dictionary)
        self.english_word = self.data["English"]
        self.french_word = self.data["French"]







