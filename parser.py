################################################################
################ Just Change this sections #####################
################################################################
# (1) Type Your Sentence

sent = "I saw the man with a telescope"

# (2) Make your CFG file for parsing your sentence.

# ex. grammar.cfg (see the direction in the powerpoint)

################################################################

import nltk
grammar = nltk.data.load("file:.\\grammar.cfg")
parser = nltk.ChartParser(grammar)
tokens = nltk.tokenize.word_tokenize(sent)
trees = parser.parse(tokens)

with open(".\\result.txt", "w") as f1:
    for tree in trees:
        print(tree)
        f1.write(str(tree)+"\n\n")
        tree.draw()
