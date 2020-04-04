# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:39:09 2019

@author: mh70
"""
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')



import nltk
import spacy
sentence_cs = "Ve snaze o podporu znalostní ekonomiky, odchod od ekonomiky montoven a konec levné práce se vláda rozhodla dodatečně zdanit dva nejpokročilejší sektory naší ekonomiky, finanční služby a telco."
sentence_en = "Bring us food, or be food yourself."
article_cs = """Ve stavbě letadel byli pak relativně úspěšní bratři Eugen a Hugo Čihákovi, mimo jiné bratranci Kašpara. 
Jejich nejpovedenější stroj se zrodil koncem roku 1912, nesl jméno Rapid a ne úplnou náhodou svými tvary připomínal francouzské stroje Morane-Saulnier. 
Rapid se vlastně stal i nejúspěšnější leteckou konstrukcí do roku 1914 u nás."""
#%%

sentence = sentence_en
article = article_cs

#%%
tokens = nltk.word_tokenize(sentence)
tagged_tokens = nltk.pos_tag(tokens)



nlp = spacy.load("en")
doc = nlp(sentence)
sp_tokens = [t for t in doc]
sp_tagged_tokens = [(t.text, t.tag_) for t in sp_tokens ] 


print(tagged_tokens)
print()
print(sp_tagged_tokens)

#%%
tokens_sen = nltk.sent_tokenize(article)

a_doc = nlp(article)
sp_tokens_sen = list(a_doc.sents)


