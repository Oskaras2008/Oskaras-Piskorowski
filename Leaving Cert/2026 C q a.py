# Question 16 (a)
# Examination Number:

# Function to calculate readability score of text
def calculate_readability_score(text):

# Split the text into a list of words
    words = text.split()
    print("The list of words in the text is:\n", words)

# Initialise the word counters
    word_count = len(words) # Number of words in list
    word_count = int(word_count)
    short_word_count = 0
    for i in words:
        if len(i)<2 or len(i)==2:
            short_word_count +=1
    print("Short word count:",short_word_count)
# Initialise the number of sentences
    sentence_count = text.count(".") or text.count("!")

# Calculate the readability score
    score = 0.4 * ((word_count/sentence_count) +  100 * ((word_count-short_word_count)/word_count))
    score = round(score, 2) # Round the score to 2 d.p.
    return score

# Set the text for analysis
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways."
text2 = "I do not like green eggs and ham! I do not like them Sam I am!"

# Calculate the score for text1
score1 = calculate_readability_score(text1)
print("readability score 1:",score1,"\n")
score2 = calculate_readability_score(text2)
print("readability score 2:",score2,"\n")

if score1 == score2:
    print("both texts are the same")
    
elif score1 < score2:
    print("text 1 is easier to read")

elif score1 > score2:
    print("text 2 is easier to read")