#import files
import random
import hangman_words
import hangman_art
stages = hangman_art.stages
used = []
#chose random word
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#print gameboard
print(hangman_art.logo)
#Testing code
#print(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

    #check for already guessed letter
  if guess in used:
    print("you used that already")
  used += guess 


    #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      #test letter placement
       # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

    #Check if user is wrong.
  if guess not in chosen_word:
        
      print("that letter is not in the word.")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")

    #update gameboard.
  print(f"{' '.join(display)}")

    #Check if user has got all letters.
  if "_" not in display:
      end_of_game = True
      print("You win.")

   
  print(stages[lives])