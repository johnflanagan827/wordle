import requests
import json
from termcolor import colored

class WordleGame(object):

  MAX_ATTEMPTS = 6
  WORD_LENGTH = 5

  def __init__(self):
    self.correct_word = ''
    self.this_word = ''
    self.word_colors = [None] * 5
    self.qwerty_colors = [None] * 26
    self.curr_try = 1
    self.qwerty_str = ''

  def wordle(self):
    '''runs the entire game - sets a new correct word, gets input from user, shows output to user'''
    word = requests.get('https://random-word-api.herokuapp.com/word?length=' + str(self.WORD_LENGTH)).text
    self.correct_word = word[2:len(word)-2]
    while self.curr_try <= self.MAX_ATTEMPTS:
      self.this_word = input(f'Enter your five word guess: Trial {self.curr_try}: ')
      if not len(self.this_word.rstrip()) == 5:
        print(colored('Only 5 letter words allowed.', color='red'), end='\n\n')
        continue
      if not self.is_word():
        print(colored('Not a real word.', color='red'), end='\n\n')
        continue
      self.update_letters()
      self.display_word()
      self.update_qwerty()
      self.curr_try += 1
      print(self.qwerty_str, end='\n\n')
      if self.this_word == self.correct_word:
        break
    print(f'The correct word was {self.correct_word.upper()}.')

  def is_word(self):
    '''returns True if self.this_word is a real word using dictionary API'''
    data_text = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + self.this_word).text
    json_text = json.loads(data_text)
    return not 'title' in json_text

  def update_letters(self):
    '''updates self.word_colors with the right colors'''
    self.word_colors = [None] * 5
    remaining_word = list(self.correct_word)

    for pos, char in enumerate(self.this_word):
      if char in remaining_word and remaining_word[pos] == char: 
        self.word_colors[pos] = 'green'
        remaining_word[pos] = None
    
    for pos, char in enumerate(self.this_word):
      if char in remaining_word and not self.word_colors[pos]:
        self.word_colors[pos] = 'yellow'
        for i in range(5):
          if remaining_word[i] == char:
            remaining_word[i] = None
            break
      elif not self.word_colors[pos]:
        self.word_colors[pos] = 'grey'

  def display_word(self):
    '''uses self.this_word and self.word_colors to display the self.this_word with appropriate colors'''
    for pos, char in enumerate(self.this_word):
      print(colored(char.upper(), color=self.word_colors[pos]), end="")
    print()

  def update_qwerty(self):
    '''updates self.qwerty_str with the right colors'''
    
    for pos, char in enumerate(self.this_word):
      if self.qwerty_colors[ord(char)-97] == 'yellow' and self.word_colors[pos] == 'green' or self.qwerty_colors[ord(char)-97] == None:
        self.qwerty_colors[ord(char)-97] = self.word_colors[pos]

    self.qwerty_str = ''
    for pos, color in enumerate(self.qwerty_colors):
      self.qwerty_str += ' ' + colored(chr(65+pos), color = color)

if __name__ == '__main__':
  wordle = WordleGame()
  wordle.wordle()
