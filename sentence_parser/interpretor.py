import nltk
#nltk.download()


from nltk.parse import RecursiveDescentParser
from nltk import CFG

grammar = CFG.fromstring("""
... S -> NP VP
... PP -> P NP
... NP -> DT N | N PP | DT N PP
... VP -> V NP | V PP | V NP PP
... DT -> 'a'
... DT -> 'the'
... N -> 'cat'
... N -> 'dog'
... N -> 'rug'
... V -> 'chased'
... V -> 'sat'
... P -> 'in'
... P -> 'on'
... """)

rd = RecursiveDescentParser(grammar)

sentence1 = 'the cat chased the dog'.split()
for t in rd.nbest_parse(sentence1):
    print(t)
