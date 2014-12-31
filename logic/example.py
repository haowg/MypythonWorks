#_*_coding=utf8_*_
import  nltk
from nltk.sem.logic import *
from nltk.sem import *

###检查类型
from nltk.sem.logic import LogicParser 
lp = LogicParser(True)
print(lp.parse(r'man(x)').type)

#一阶逻辑##证明初级#################################
NotFnS = lp.parse('-north_of(f, s)') 
SnF = lp.parse('north_of(s, f)') 
R = lp.parse('all x. all y. (north_of(x, y) -> -north_of(y, x))') 
prover = nltk.Prover9() 
prover.prove(NotFnS, [SnF, R])
#真值模型#########################################
#真值模型的定义方式
import  nltk
from nltk.sem.logic import *
from nltk.sem import *
import  nltk
from nltk.sem import Valuation, Model

v = """
john => b1
mary => g1
suzie => g2
fido => d1
tess => d2
noosa => n
girl => {g1, g2}
boy => {b1, b2}
dog => {d1, d2}
bark => {d1, d2}
walk => {b1, g2, d1}
chase => {(b1, g1), (b2, g1), (g1, d1), (g2, d2)}
see => {(b1, g1), (b2, d2), (g1, b1),(d2, b1), (g2, n)}
in => {(b1, n), (b2, n), (d2, n)}
with => {(b1, g1), (g1, b1), (d1, b1), (b1, d1)}
"""
val = Valuation.fromstring(v)
dom = val.domain
m = Model(dom, val)
g = Assignment(dom)
val = Valuation.fromstring(v)
print(m.evaluate('see(john, mary)&boy(john)&walk(john)', g))
######################################################
#print(val)
import  nltk
from nltk.sem.logic import *
from nltk.sem import *
import  nltk
from nltk.sem import Valuation, Model

null_binary_rel = set([(None, None)])
v = [('adam', 'b1'), ('betty', 'g1'), ('fido', 'd1'),\
     ('girl', set(['g1', 'g2'])), ('boy', set(['b1', 'b2'])), ('dog', set(['d1'])),
     ('love', set([('b1', 'g1'), ('b2', 'g2'), ('g1', 'b1'), ('g2', 'b1')])),
     ('kiss', null_binary_rel)]
val = Valuation(v)
dom = val.domain
m = Model(dom, val)
g = Assignment(dom)
sorted(val['boy'])
('b1',) in val['boy']
('g1',) in val['boy']
('foo',) in val['boy']
('b1', 'g1') in val['love']
('b1', 'b1') in val['kiss']
sorted(val.domain)

#################################################
#_*_coding=utf8_*_
import  nltk
from nltk.sem.logic import *
from nltk.sem import *
import  nltk
from nltk.sem import Valuation, Model

v = [('adam', 'b1'), ('betty', 'g1'), ('fido', 'd1'),
     ('girl', set(['g1', 'g2'])), ('boy', set(['b1', 'b2'])),
     ('dog', set(['d1'])),
     ('love', set([('b1', 'g1'), ('b2', 'g2'), ('g1', 'b1'), ('g2', 'b1')]))]
val = Valuation(v)
dom = val.domain
m = Model(dom, val)

dom = val.domain
g = Assignment(dom)
print(m.evaluate('all x.(boy(x) -> - girl(x))', g))
print(m.evaluate('all x.(girl(x) -> love(x,adam))', g))
###
#因为包含逻辑运算式所以可以运算任意复杂的表达式
####
###########################################################
###赋值

print(m.evaluate('boy(b2)', g))
#用g赋值
g = nltk.Assignment(dom, [('x', 'b2'), ('y', 'g2')])
print(m.evaluate('boy(x)', g))

print(m.evaluate('girl(x)', g))
print(m.evaluate('girl(suzie)', g))

#################################################
#lambda演算示例
# β约简
lexpr = Expression.fromstring
e = lexpr(r'\x.(walk(x) & chew_gum(x))(gerald)')
print(e.simplify())

x1 = lexpr(r'\a.((\b.like(b,a)(vincent)) & sleep(a))').simplify()
x2 = lexpr(r'\a.(like(vincent,a) & sleep(a))').simplify()
x1 == x2

#嵌套
x3 = lexpr(r'\x.\y.(dog(x) & own(y, x))(cyril)').simplify()
x4 = lexpr(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify()
lexpr(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify()==lexpr(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify()

#参数类型是函数
#自由变量 y 规定是 e 类型， \y.y(angus)只适用于 e 类型的参数,我们可以用QP表示<e,t>类型
#lexpr(r'\y.y(angus)(\x.walk(x))').simplify()
lexpr(r'\P.P(angus)(\x.walk(x))').simplify()

#α转换 和变量名字无关
e1 = lexpr('exists x.P(x)')
print (e1)
e2 = e1.alpha_convert(nltk.Variable('z'))
print (e2)
e1 == e2

#e3 = lexpr('\P.exists x.P(x)(\y.see(y, x))')
#print (e3)
#print (e3.simplify())

