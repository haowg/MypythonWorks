#encoding: utf-8
#量化

import nltk
from nltk.sem import *
lexpr = Expression.fromstring
lexpr(r'\P x.(dog(x) & P(x)) (\x.bark(x))').simplify()

tvp = lexpr(r'\X x.X(\y.chase(x,y))')
np = lexpr(r'(\P.exists x.(dog(x) & P(x)))')
vp = nltk.ApplicationExpression(tvp, np)
print (vp)
vp.simplify()

##################################
#演示分析句子得到句意
nltk.data.show_cfg('grammars/book_grammars/simple-sem.fcfg')
#from nltk import load_parser
#parser = load_parser('grammars/book_grammars/simple-sem.fcfg', trace=0)
sentence = 'Angus gives a bone to every dog'
s2 = 'a man sees a dog'
#tokens = sentence.split()
trees = nltk.sem.util.interpret_sents([sentence,s2],'grammars/book_grammars/simple-sem.fcfg')
for tree in trees:
    print (tree[0][0].label()['SEM'])
print (trees[0][0][0].label()['SEM'])

#################################################
#句子真假
import  nltk
from nltk.sem.logic import *
from nltk.sem import *
from nltk.sem import Valuation, Model
v = """
bertie => b
angus => a
cyril => c
boy => {b}
girl => {a}
dog => {c}
walk => {a, c}
see => {(b, a), (c, b), (a, c)}
"""
val = Valuation.fromstring(v)
g = nltk.Assignment(val.domain)
m = nltk.Model(val.domain, val)
sent = 'Cyril sees every boy'
sent2 = 'Angus sees a girl'
grammar_file = 'grammars/book_grammars/simple-sem.fcfg'
results = nltk.sem.util.evaluate_sents([sent,sent2], grammar_file, m, g)
for result in results:
    for (syntree, semrel, value) in result:
    #print(syntree)
        print (semrel)
        print (value)






