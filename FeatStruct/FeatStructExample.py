#encoding: utf-8
from __future__ import print_function
from nltk.featstruct import FeatStruct
from nltk.sem.logic import Variable, VariableExpression, Expression
fs1 = FeatStruct(number='singular', person=3)
print(fs1)
#包含   一组特征中的一个特征是另一个特征组
fs2 = FeatStruct(type='NP', agr=fs1)
print(fs2)
#统一     合并两组特征
fs3 = FeatStruct(agr=FeatStruct(number=Variable('?n')),
                 subj=FeatStruct(number=Variable('?n')))
print(fs3)
print(fs2.unify(fs3))
#共享
fs1 = FeatStruct(x='val')
fs2 = FeatStruct(a=fs1, b=fs1)
print(fs2)
    