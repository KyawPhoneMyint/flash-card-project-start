import pandas as pd
import random
from gtts import gTTS
import pygame
import os
import re
def sanitize(word):
    # Remove all non-alphanumeric characters
    return re.sub(r'[^A-Za-z0-9]', '', word)

data=pd.read_csv("./data/french_words.csv")
learned_data=pd.read_csv("./data/french_learned_words.csv")
data_dictionary=data.to_dict("records")
class Word:
    def __init__(self):
        self.learned_word = learned_data.to_dict("records")
        self.data={}
        self.is_French=True
        self.generate_word()
        self.english_word=self.data["English"]
        self.french_word=self.data["French"]
        self.empty=False
        pygame.mixer.init()

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
        self.is_French=True
        while self.data in self.learned_word:
            self.data = random.choice(data_dictionary)
        self.english_word = self.data["English"]
        self.french_word = self.data["French"]

    def speak_word(self,word_text, lang):
        safe_name = f"{lang}_{sanitize(word_text)}.mp3"

        if not os.path.exists(safe_name):
            tts = gTTS(text=word_text, lang='fr' if lang == "French" else 'en')
            tts.save(safe_name)

        # Play with Pygame
        pygame.mixer.music.stop()
        pygame.mixer.music.load(safe_name)
        pygame.mixer.music.play()






