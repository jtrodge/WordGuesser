import random
lines = []
with open('words.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

randWord = ""
random.shuffle(lines)
for x in range(0, 1):
    randWord = lines[x]

print(randWord)
countWord = 0
for x in randWord:
    countWord += 1

print("Hey! Welcome to my word guesser game\n")
print("HINT: The word contains " + str(countWord) + " letters.\n")

guess = ''
print("Guess the word: ")
guess = input()
letterCounter = 0
pos = []
minSize = min(len(guess), len(randWord))
while guess != randWord:
    for i in range(minSize):
        if guess[i] == randWord[i]:
            letterCounter += 1
            pos.append(i)
    print("Your guess contains " + str(letterCounter) + " of the same letters.")
    print("Your guess matches the correct word at positons: ")
    print(pos)
    print("Try again, guess the word: ")
    guess = input()



print("Congratulations, you have guessed the word!!!")