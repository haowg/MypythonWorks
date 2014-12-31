#encoding: utf-8

############################################################
#跟踪基于特征的分析器
import nltk
#查看语法文件
nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')
#解析带步骤
from nltk.grammar import PCFG, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.parse import ViterbiParser
tokens = 'Kim likes children'.split()
from nltk import load_parser 
cp = load_parser('grammars/book_grammars/feat0.fcfg', trace=2) 
trees = cp.parse(tokens)


#####################################################
#用基于特征的方式分析助动词和倒装句
import nltk   
nltk.data.show_cfg('grammars/book_grammars/feat1.fcfg')

tokens = 'who do you claim that you like'.split()
from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.parse(tokens):
    print (tree)
    
###########################################################    
#基于特征的文法解析自然语言为sql语句

nltk.data.show_cfg('grammars/book_grammars/sql0.fcfg')

query = 'What cities are located in China'
results = nltk.sem.util.interpret_sents([query],'grammars/book_grammars/sql0.fcfg')
print(str(results[0][0][0].label()['SEM']).replace(',',''))
results[0][0][0].draw()    
    
    
    
    
    
    
    
    
#########################################################
###合并解析    
import nltk
parsers = [nltk.parse.featurechart.FeatureChartParser,
           nltk.parse.featurechart.FeatureTopDownChartParser,
           nltk.parse.featurechart.FeatureBottomUpChartParser,
           nltk.parse.featurechart.FeatureBottomUpLeftCornerChartParser,
           nltk.parse.earleychart.FeatureIncrementalChartParser,
           nltk.parse.earleychart.FeatureEarleyChartParser,
           nltk.parse.earleychart.FeatureIncrementalTopDownChartParser,
           nltk.parse.earleychart.FeatureIncrementalBottomUpChartParser,
           nltk.parse.earleychart.FeatureIncrementalBottomUpLeftCornerChartParser,
           ]
def unittest(grammar, sentence, nr_trees):
    sentence = sentence.split()
    trees = None
    for P in parsers:
        result = P(grammar).parse(sentence)
        result = set(tree.freeze() for tree in result)
        if len(result) != nr_trees:
            print("Wrong nr of trees:", len(result))
        elif trees is None:
            trees = result
        elif result != trees:
            print("Trees differ for parser:", P.__name__)

isawjohn = nltk.parse.featurechart.demo_grammar()
unittest(isawjohn, "I saw John with a dog with my cookie", 5)  
   
whatwasthat = nltk.grammar.FeatureGrammar.fromstring('''
S[] -> NP[num=?N] VP[num=?N, slash=?X]
NP[num=?X] -> "what"
NP[num=?X] -> "that"
VP[num=?P, slash=none] -> V[num=?P] NP[]
V[num=sg] -> "was"
''')
unittest(whatwasthat, "what was that", 1)