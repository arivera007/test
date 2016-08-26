## Author: Adriana Rivera
##   Text content analyzer. This is a tool used by writers to find statistics 
## such as word and sentence count on essays or articles they are writing.
## INPUT: Text file
## OUTPUT: Total word count, unique words and sentence count.

## Assuming a number is a word.
## Assuming a line is a paragraph.
## I didn't check for boundary situations, or handleling of special characters like (').

def loadWords(line):
    for word in line.split():
        words[word] = words.get(word, 0) + 1 #Increase counter if neccesaryfor the word read.



sourcefile = open( "sourcefile2.txt", "r", encoding='utf-8' )
words = {}
sentences = 0
for line in sourcefile:
    loadWords( line.strip() )
    sentences = sentences + 1   #For now assuming than sentence number = line#
sourcefile.close()
print("Total word count: ", + sum(words.values()))
print("Unique words: " + str(len([word for word, freq in words.items() if freq == 1])))
print("sentences: " + str(sentences))


## Brownie points :)
# 3. Sort words by frequency
print("Frequency of words used:")
for word in sorted(words, key=words.get, reverse=True):
  print( word, words[word])
