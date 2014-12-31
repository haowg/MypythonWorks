#_*_coding : utf8 _*_
#概率文法的基本应用
import nltk
from nltk.grammar import PCFG
grammar = PCFG.fromstring("""
S -> NP VP [1.0]
VP -> TV NP [0.4]
VP -> IV [0.3]
VP -> DatV NP NP [0.3]
TV -> 'saw' [1.0]
IV -> 'ate' [1.0]
DatV -> 'gave' [1.0]
NP -> 'telescopes' [0.8]
NP -> 'Jack' [0.2]
""")
prod = grammar.productions()[0]
from nltk.parse import pchart
parser = pchart.InsideChartParser(grammar)
for t in parser.parse(['Jack', 'saw', 'telescopes']):
    print(t)
for t in parser.parse('Jack saw telescopes'.split()):
    print(t)
    
#(S (NP Jack) (VP (TV saw) (NP telescopes))) (p=0.064)
#概率文法歧义展示
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.parse import ViterbiParser
tokens = "Jack saw Bob with my cookie".split()
grammar = toy_pcfg2
from nltk.parse import pchart   
parser = pchart.InsideChartParser(grammar)
for t in parser.parse(tokens):
    print(t)