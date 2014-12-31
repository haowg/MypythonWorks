#encoding: utf-8
import nltk
f=open('d://myyuliao//76report')
raw=f.read()
tokens = nltk.word_tokenize(raw)
report_76 = nltk.Text(tokens)

f=open('d://myyuliao//86report')
raw=f.read()
tokens = nltk.word_tokenize(raw)
report_86 = nltk.Text(tokens)

report_76.collocations()
report_76.concordance('社会主义')
report_76.similar('任务')
report_76.common_contexts(['中国','国家'])

#词表

vocabulary1 =sorted(set (report_76))
Fd=nltk.FreqDist(report_76)
vocabulary1 = Fd.keys()
#词频统计
#fd = nltk.FreqDist(text)
fdist=nltk.FreqDist([len(w)for w in report_76])
cfd =nltk.ConditionalFreqDist(nltk.bigrams(report_76))
cfd.items()  
cfd['毛主席']
cfd['毛主席']['说过']
