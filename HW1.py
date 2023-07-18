#!/usr/bin/env python
# coding: utf-8

# ## Morgan Tucker, Jiarui Chang, Anurag Arakala, Ian McIntosh
# 
# 
# # Rock, Paper, Scissors (20 points)
# 
# You will code up the game of <a href="http://en.wikipedia.org/wiki/Rock_paper_scissors">Rock, Paper, Scissors.</a>
# 
# Each game round consists two turns, the first by the computer and the second by a human.
# The computer continues playing rounds until the human chooses to quit.
# 
# #### Each round proceeds in the following steps:
# 
# * The computer chooses one of Rock, Paper, and Scissors, but keeps its choice secret.
# * The computer asks for the human's input.
# * The human chooses one of Rock, Paper, and Scissors, or Quit.
# * Unless the human quits, the computer figures out the result of the game, as follows:
#      * Rock smashes Scissors, so Rock beats Scissors.
#      * Scissors can cut up paper, so Scissors beat Paper.
#      * Paper covers Rock, so Paper beats Rock.
#     * If both players chose the same, it is a draw.
# * The computer reports the result of this round.
# * If the human chooses to quit, the computer reports:
#      * the number of games played, and
#      * the number of times the human won.
#      
# #### Computer's brains:
# The computer must be able to exploit some human biases.  If the human
# has played Rock most often, the computer should assume that he or she
# will play Rock in the next round, so the computer should play Paper.
# If the human has played Rock and Paper equally often, and Scissors
# less often, the computer should assume that the human is going to play
# either Rock or Paper (both equally likely) in the next round. (What
# should the computer play?)
# 
# Hence, **your program should remember how many Rock, Paper, or
# Scissors were played by the human.** Note that we don't need to
# remember the order in which the human chooses these; the total counts
# so far for each choice will be enough.
# 
# #### Gotchas:
# 
# * *User input:* How you want to receive the user's input is up
# to you, but you **must** check the user's input to make sure it is
# valid (you can assume that the user input is of the correct type).
# If it isn't, request the user for input again.
# 
# ### TODO:
# 
# * Write code to run the game.
#     * You should have a top-level function called "playGame()"
# * Use as many code cells as you want.
# * If you find yourself reusing any piece of code, write it as a separate function.
# * At the end, show a sample run of your program.
#     * In other words, call "playGame()" and play a game.
# * NOTE: Unlike standard Python, you don't need a "__main__" function here.

# In[2]:


# import random module so computer can randomly choose one of three options if necessary
import random
# computer brain function
def computer_play(rocks, papers, scissors):
    # initialize list of options for computer to play
    play = ['Rock', 'Paper', 'Scissors']
    # if player has played all options an equal amount of times
    if (rocks == papers) & (papers == scissors):
        # pick a random option
        computer_play = play[random.randint(0,2)]
    # if the player has played paper and scissors tied for the most times
    elif  (rocks < papers) & (rocks < scissors) & (papers == scissors):
        # pick scissors
        computer_play = "Scissors"
    # if the player has played paper and rock tied for the most times   
    elif  (scissors < papers) & (scissors < rocks) & (papers == rocks):
        # pick paper
        computer_play = 'Paper'
    # if the player has played scissors and rock tied for the most times   
    elif  (papers < rocks) & (papers < scissors) & (scissors == rocks):
        # pick rock
        computer_play = 'Rock'
    # if the player has chosen rock the most
    elif (rocks > papers) & (rocks > scissors):
        #choose paper
        computer_play = 'Paper'
    # if the player has chosen paper the most
    elif (papers > rocks) & (papers > scissors):
        # choose scissors
        computer_play = 'Scissors'
    # if the player has chosen scissors the most
    elif (scissors > papers) & (scissors > rocks):
        # choose rock
        computer_play = 'Rock'
    # return computer choice
    return(computer_play)


# In[ ]:


# human play function
def human_play():
    # take human input
    human_play = str(input("Choose 'Rock', 'Paper', 'Scissors' or 'Quit'\n"))
    # return what they choose
    return(human_play)


# In[ ]:


# function to play games
def playOnce(rocks, papers, scissors, wins, nonWins):
    # get computer choice
    computer_play2 = computer_play(rocks, papers, scissors)
    # get human choice
    human_play2 = human_play()
    # make sure the player chooses 'Rock', 'Paper' or 'Scissors'
    if (human_play2 != 'Rock') & (human_play2 != 'Paper') & (human_play2 != 'Scissors'):
        # if they dont choose an option, see if they want to quit
        if (human_play2 == 'Quit'):
            # if they want to quit tell them their stats
            print('You played', int(wins + nonWins), 'games')
            print('You won', int(wins), 'games')
        else:
            # if they don't want to quit prompt them to enter one of the options and start the game over
            print('Please enter a valid input')
            playOnce(rocks, papers, scissors, wins, nonWins)
    else:
        # if the human plays rock
        if (human_play2 == 'Rock'):
            # check for draw
            if (human_play2 == computer_play2):
                # Tell and record result
                print("It's a draw")
                nonWins += 1
            # check for win
            elif (computer_play2 == 'Scissors'):
                # Tell and record result                
                print('Rock smashes Scissors. You win!')
                wins += 1
            #check for loss
            elif (computer_play2 == 'Paper'):
                # Tell and record result
                print('Paper covers Rock. You lose :(')
                nonWins += 1
            # play again with human play recorded to inform computer for next round
            playOnce(rocks + 1, papers, scissors, wins, nonWins)
        # if human plays paper
        elif (human_play2 == 'Paper'):
            # check for draw
            if (human_play2 == computer_play2):
                # Tell and record result
                print("It's a draw")
                nonWins += 1
            # check for win
            elif (computer_play2 == 'Rock'):
                # Tell and record result
                print('Paper covers Rock. You win!')
                wins += 1
            # check for loss
            elif (computer_play2 == 'Scissors'):
                # Tell and record result
                print('Scissors can cut up paper. You lose :(')
                nonWins += 1
            # play again with human play recorded to inform computer for next round
            playOnce(rocks, papers + 1, scissors, wins, nonWins)
        # if human plays scissors
        elif (human_play2 == 'Scissors'):
            # check for draw
            if (human_play2 == computer_play2):
                # Tell and record result
                print("It's a draw")
                nonWins += 1
            # check for win
            elif (computer_play2 == 'Paper'):
                 # Tell and record result
                print('Scissors can cut up paper. You win!')
                wins += 1
            # check for loss
            elif (computer_play2 == 'Rock'):
                # Tell and record result
                print('Rock smashes Scissors. You lose :(')
                nonWins += 1
            # play again with human play recorded to inform computer for next round
            playOnce(rocks, papers, scissors + 1, wins, nonWins)


# In[ ]:


# play game function with no inputs
def playGame():
    # call recursive function to play games and set all inputs to 0 to start from scratch
    playOnce(0,0,0,0,0)


# In[ ]:


# play the game!
playGame()


# # Voters in Florida (20 points)
# 
# The file <a href="HW2FloridaVoters.html">HW2FloridaVoters.html</a> contains a Web Table of republican and democratic voters in various counties in Florida.
# 
# Write code that reads in this file **as a standard text file** and prints out the counties, along with the number of republican and democratic voters in those counties, **sorted by the number of democratic voters.**
# 
# The output should look like this:
# <pre>
# LAFAYETTE 1373 2672
# GLADES 2190 3110
# LIBERTY 720 3372
# ...
# MIAMI-DADE 362161 539367
# BROWARD 249762 566185
# Total 4377713 4637026
# </pre>
# 
# #### Notes:
# 
# * The numbers in the HTML file contain commas, but we must get rid of them in order to do the sorting.
# * While we should technically ignore the data for <tt>Total</tt>, let's not worry about it here.
# * **IMPORTANT**: There are many libraries for automatically reading and parsing HTML. **You should not use them.** You must read in the HTML file as a plain text file, and figure out the correct regular expressions to extract the county names and the numbers of voters.
# * *Hint:* You may want to read in the file and create a list of tuples of the form
# <pre> [('ALACHUA', 47329, 77996), ('BAKER', 6963, 5813), ...] </pre>
# and then do the sorting and printing.
# * At the end, show a sample run of your code.

# In[17]:


vote = open('/users/morgantucker/Desktop/DS/HW1/FloridaVoters.html', 'r')
opvote = vote.readline()
opvote
import re

ff = []
while opvote != "":
    opvote = opvote.rstrip()
    opvote = opvote.lstrip()
    if re.findall("[\<td>][A-Z0-9\,]+[\.\s\-]*[A-Z0-9\,]+[\</td>]", opvote):
        ff += (re.findall("[\<td>][A-Z0-9\,]+[\.\s\-]*[A-Z0-9\,]+[\</td>]", opvote))
    opvote = vote.readline()

ff
# Data from 'Total' row is not skipped.
gg = enumerate(ff)
lis = []
for i, st in gg:
    if re.findall("[A-Z]+", st):
        if re.findall("[0-9]+", ff[i+1]):
            lis += [[st.replace('>', "").replace('<', ""),
                     int(ff[i+1].replace('>', "").replace('<', "").replace(',', "")),
                     int(ff[i+2].replace('>', "").replace('<', "").replace(',', ""))]]

lis2 = sorted(lis, key=lambda x: x[2])

# Append the last row ('Total') to the 'lis2' list
last_row = ['Total', int(ff[-2].replace('>', "").replace('<', "").replace(',', "")), int(ff[-1].replace('>', "").replace('<', "").replace(',', ""))]
lis2.append(last_row)

def fin_output(f):
    for j in f:
        print(*j, sep=' ')

fin_output(lis2)


# # Near-duplicate detection (20 points)
# 
# Tweets on a subject are often nearly (but not exactly) duplicates of each
# other. The file Santa.txt contains a few tweets about Santa Claus, one
# tweet per line. We will try to detect tweets that we have already seen before.
# 
# ### (a) Convert each tweet into a dictionary of phrases (6 points).
# Write a function called `moving_window` that takes as input a tweet (that is,
# a string), and converts it into a bunch of phrases. Each phrase is three con-
# secutive words in the tweet. 
# * For example, the tweet `This is an awesome tweet, dude` consists of the phrases
#     * `This is an`
#     * `is an awesome`
#     * `an awesome tweet,`
#     * `awesome tweet, dude` 
# 
# Return a dictionary whose keys are these phrases, and just set the corresponding values to 1. This dictionary contains all the unique 3-word phrases in the tweet.

# In[1]:


def moving_window(tweet):
    phrases = {}
    word = tweet.split()
    for i in range(len(word) - 2):
        phrase = ' '.join(word[i:i+3])
        phrases[phrase] = 1
    return phrases


# ### (b) Calculate similarity between two tweets (6 points).
# To check if one tweet is a near-duplicate of another, we compute their cosine similarity:
# 
# $cosine(\text{tweet}_1, \text{tweet}_2) = \frac{matches}{\sqrt{n1\times n2}}$
# 
# where `matches` is the number of 3-word phrases in common between the two tweets, and
# `n1` and `n2` are the number of phrases in the two tweets respectively.
# 
# Write a function called `cosine` that takes as input two dictionaries. Each
# dictionary contains the 3-word phrases from one tweet. Return the cosine
# similarity between the phrases in the two dictionaries.
# 
# *Hint:* You can use the function `math.sqrt(x)` to calculate the square-root
# of any floating point number x, but you must import the `math` module.

# In[2]:


import math
def cosine(dict1, dict2):
    common_phrases = set(dict1.keys()) & set(dict2.keys())
    matches = len(common_phrases)
    n1 = len(dict1)
    n2 = len(dict2)
    similarity = matches / math.sqrt(n1 * n2)
    return similarity


# ### (c) Read in tweets, and output near-duplicates (8 points).
# Read in the tweets in the file `Santa.txt`. For each tweet, figure out if it is a near-duplicate of any of the previously-seen tweets. We say that the two tweets are near-duplicates if their cosine similarity is greater than 0.5.
# You should call the functions `moving_window` and `cosine` here.

# In[3]:


filename = "~/Desktop/DS/HW1/Santa.txt"

def read_tweets(filename):
    tweets = []
    with open(filename, 'r') as file:
        for line in file:
            tweet = line.strip()
            tweets.append(tweet)
        return tweets
def check_similarity(tweets):
    seen_tweets = []
    near_duplicates = []
    for tweet in tweets:
        phrases_dict = moving_window(tweet)
        for seen_tweet in seen_tweets:
            seen_tweets_dict = moving_window(seen_tweet)
            similarity = cosine(phrases_dict, seen_tweets_dict)
            if similarity > 0.5:
                near_duplicates.append((tweet, seen_tweet))
        seen_tweets.append(tweet)
    return near_duplicates
filename = 'Santa.txt'
tweets = read_tweets(filename)
near_duplicates = check_similarity(tweets)
for tweet1, tweet2 in near_duplicates:
    print(f'The Tweet 1 : {tweet1}')
    print(f'The Tweet 2 : {tweet2}')


# # The Google of Quotes (40 points)
# The file `quotes.txt` contains pairs of lines, with the first line being a quote
# and the following line being the person who said it. We want to build a
# search engine that, given a word or words, finds the best matching quotes.
# 
# ### (a) Build a list of full quotes (5 points).
# Read in the file, and create a list of full quotes of the form *"quote - speaker"*.
# * For example, `"The heart has its reasons, of which the mind knows nothing. - Blaise Pascal"`.

# In[20]:


file_path = '/users/morgantucker/Desktop/DS/HW1/quotes.txt'

with open(file_path, 'rb') as file:
    content = file.read().decode('utf-8', errors='ignore')

lines = content.splitlines()
print(lines)


# In[21]:


quotes = []
for i in range(0, len(lines), 2):
    quote = lines[i]
    speaker = lines[i + 1]
    quote_with_speaker = f"{quote} - {speaker}"
    quotes.append(quote_with_speaker)

print(quotes)


# ### (b) Words from full quotes (5 points).
# Write a function that takes a full quote as argument and outputs a list of the words in the it.
# The words should all be lower-case, and should contain only characters, digits, or underscore.
# 
# *Hint:* Use the `lower()` function of strings, and `re.split()` to split into
# words, but you must figure out the regular expression for `re.split()`.

# In[22]:


#import necessary package
import re
#initialize function
def words(quote):
    #put quote in lowercase
    quote = quote.lower()
    #split quote using spaces, commas, periods and dashes as delimiters
    quote = re.split('[^\w\']+', quote)
    #output split quote
    return(quote)
#example of function runnning    
words(quotes[0])


# ### (c) Build the postings-list dictionary (6 points).
# A postings-list is a dictionary whose keys are full quotes, and whose values are themselves dictionaries with key being a word, and value being the number of times the word occurs in the full quote. 
# * For example, for the key 
#     * `"The heart has its reasons, of which the mind knows nothing. - Blaise Pascal"`.
# * the corresponding value will be the following dictionary:
#     * `{'the':2, 'heart':1, 'has':1, 'its':1, 'reasons':1, 'of':1, 'which':1, 'mind':1, 'knows':1, 'nothing:1, 'blaise':1, 'pascal':1}`.

# In[25]:


#initialize postings-list
fullDict = {}
#for each quote in the list
for quote in quotes:
    #initialize dictionary for value of postings-list
    quoteDict = {}
    #split quote into list of words in quote
    newWords = words(quote)
    #count number of instances of each unique word in list, and make into dictionary with word as key and count as value
    for word in newWords:
        quoteDict[word] = newWords.count(word)
    #populate postings-list with quote as key and dictionary as value
    fullDict[quote] = quoteDict
#preview final postings-list
list(fullDict.items())[:3]


# ### (d) Build the reverse postings-list dictionary (6 points).
# A reverse postings-list is a dictionary whose keys are the words, and the values are
# themselves dictionaries with the key being a full quote, and the value being the number of times the word appeared in the full quote.
# 
# * For example, for the key
#     * `"entertainer"`
# * the value is the following dictionary:
#     * `{'An actor is at most a poet and at least an entertainer.- Marlon Brando':1}`
#     * (only this quote contains the word "entertainer").

# In[26]:


#initialize reverse postings-list
fullDict2 = {}
#for each quote in the list
for quote in quotes:
    #split quote into list of words in quote
    newWords = words(quote)
    #for each word in the list of words in the quote
    for word in newWords:
        #initialize value dictionary
        quoteDict2 = {}
        #find how often each word appears in the wuote
        count = newWords.count(word)
        #populate dictionary with key value pairs of quotes and how many times word appears in quote
        quoteDict2[quote] = count
        #if the word has not been in the dictionary yet
        if word not in fullDict2.keys():
            #append key value pair to dictionary
            fullDict2[word] = (quoteDict2)
        #if word has been in dictionary
        else:
            #add key value pair to dictionary
            fullDict2[word][quote] = count
#preview final reverse postings-list
list(fullDict2.items())[:3]


# ### (e) Write a TF-IDF function (8 points).
# To measure how much a full quote is about a particular word, one typically uses the TF-IDF measure.
# 
# * TF stands for *term frequency*; the term frequency of a word w in a full quote q is the number of times w occurs in q, divided by the maximum number of times any word occurs in q.
# * IDF stands for *inverse document frequency*: the IDF of a word w is the logarithm of the ratio of the total number N of full quotes to the number of full quotes in that contain the word w.
# * TF-IDF of a word w for a full quote q is just the product of the TF and IDF. For example, for the word "entertainer" in the Marlon Brando quote of part (d):
#     * The TF is *0.5* since "entertainer" occurs once, while the most frequent word in that quote is "at", which occurs twice, so the TF ratio is 0.5.
#     * The IDF is *log (886/1)*, since there are 886 documents and the word "entertainer" occurs in only one full quote.
#     
# Write a function to compute the TF-IDF of any word in any full quote, using the postings and reverse-postings.
# 
# *Hint:* Do `import math` and use `math.log()` to get logarithms.

# In[27]:


#import necessary packages
import math
#initialize function
def computeTFIDF(quote, word):
    #find dictionary for specific quote
    quoteDict3 = fullDict[quote]
    #divide number of times the word appears in quote by the maximum number of times any word appears in quote
    tf = quoteDict3[word]/max(quoteDict.values())
    #find dictionary for specific word
    quoteDict4 = fullDict2[word]
    #take log of total number of full quotes divided by how many quotes the specific word appears in
    idf = math.log(len(fullDict)/len(quoteDict4))
    #multiply tf and idf and return value from function
    return(tf * idf)
#example of computeTFIDF in action
print(computeTFIDF('How we spend our days is, of course, how we spend our lives. - Annie Dillard', 'we'))


# ### (f) Quote search using a single word (5 points).
# Write a function that takes a word as argument, and returns a dictionary whose keys are full
# quotes containing that word, and whose values are the TF-IDF score of that
# word for that full quote.

# In[28]:


#initialize function
def findWord(word):
    #initialize dictionary
    newDict = {}
    #for every quote
    for quote in quotes:
        #get individual words in quote
        newWords = words(quote)
        #if the word we are looking for is one of the words in the quote
        if word in newWords:
            #populate dictionary with the quote as the key and the TF-IDF value as the value
            newDict[quote] = computeTFIDF(quote,word)
    #return dictionary
    return(newDict)
#test function
print(findWord('pizza'))


# ### (g) Quote search using multiple words (5 points).
# Write a function that takes a list of words as argument, and returns a dictionary whose keys
# are full quotes containing one or more of the words in that list, and whose
# values are the sum of TF-IDF scores of the words in that list for that full
# quote.
# 
# * For example, if you called the function with the list of words `[heart, mind, disease]`, and you have a full quote `"The heart has its reasons, of which the mind knows nothing - Blaise Pascal"`, then you want to compute the sum of TF-IDF scores of heart and mind for this full quote.

# In[29]:


#initialize function
def findWords(wordlist):
    #initialize dictionary
    newDict = {}
    #for every quote
    for quote in quotes:
        #initialize total
        total = 0
        #get individual words in quote
        newWords = words(quote)
        #parse through each word in list passed into function
        for word in wordlist:
            #if the word we are looking for is one of the words in the quote
            if word in newWords:
                #add the TF-IDF value of the quote and word to the total
                total += computeTFIDF(quote,word)
        #if any of the words in the list are in the quote
        if total > 0:
            #populate dictionary with the quote as the key and the total TF-IDF value as the value
            newDict[quote] = total
    #return dictionary
    return(newDict)
#test function
print(findWords(['heart', 'mind', 'disease']))


# In[ ]:




