import random
word_bank = ['deftones', 'fontains', 'arctic', 'luvcat', 'the cure']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 8
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('WHAT A NERD! Great guess!')
    else:
        attempts -= 1
        print('LOSER! Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations you nerd! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)