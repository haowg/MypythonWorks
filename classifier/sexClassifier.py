#encoding: utf-8
import  nltk
import random
f=open('D://myyuliao//male.txt_gbk')
malelist = f.read()
f = open('d://myyuliao//female.txt_gbk')
femalelist = f.read()
#定义特征提取器
def borg_features(word):
    return {'last_letter':word[-1]}
#制作训练集和测试集
names = ([(name,'男')for name in malelist.splitlines()]+
    [(name,'女')for name in femalelist.splitlines()])
random.shuffle(names)
featuresets = [(borg_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
#训练
classifier = nltk.NaiveBayesClassifier.train(train_set)
print (nltk.classify.accuracy(classifier, test_set))
classifier.classify(borg_features('杨其文'))


#重新定义特征提取器
def borg_features_2(word):
    return {'last_letter':word[-1],'second_letter':word[-2]}
featuresets_2 = [(borg_features_2(n), g) for (n,g) in names]
train_set_2, test_set_2 = featuresets_2[500:], featuresets_2[:500]
classifier_2 = nltk.NaiveBayesClassifier.train(train_set_2)
print (nltk.classify.accuracy(classifier_2, test_set_2))
classifier_2.classify(borg_features_2('王丽坤'))
