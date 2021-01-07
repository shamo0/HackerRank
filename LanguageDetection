'''
Author: shamo0 

Given a snippet of text in English, French, German, or Spanish, detect the
snippet's language and print the language name. You may build an offline 
model for this. The snippet may contain one or more lines.

You may make no more than 15 submissions for this problem, during the contest.

Input Format
One or more lines of text.

Output Format
Print the snippet's language (in Title Case, as written above) on a new line.
'''

text = input()
langlist = text.split(' ')

englishStopwords = ['the','be','and','of','myself','i','a','in','that','have','it','for','not','on','with','he','you','as','do','one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were']
germanStopwords = ['und','ich','seine','dass','dir','der', 'die', 'in', 'den', 'von', 'zu', 'das', 'mit', 'sich', 'des', 'auf', 'für', 'ist', 'im', 'dem', 'nicht', 'ein', 'Die', 'eine', 'als', 'auch', 'es', 'an']
frenchStopwords = ['un','le','et','pour','au','son', 'que', 'il', 'était', 'pour', 'sur','sont','avec','ils','être','à','un','avoir','ce','à partir de','par','chaud','mot','mais','que','certains','est']
spanishStopwords = ['los','el','con','del','por', 'no',  'a',  'la',  'el',  'es',  'y',  'en',  'lo',  'un',  'por',  'qué',  'me',  'una',  'te',  'los',  'se',  'con',  'para',  'mi',  'está',  'si',  'bien',  'pero',  'yo']

langs = {'English' : 0, 'German' : 0, 'French' : 0, 'Spanish' : 0}

for i in langlist:
    if (i.lower() in englishStopwords):
        langs['English']+=1
    if (i.lower() in germanStopwords):
        langs['German']+=1
    if (i.lower() in spanishStopwords):
        langs['Spanish']+=1
    if (i.lower() in frenchStopwords):
        langs['French']+=1

Keymax = max(langs, key=langs.get) 
print(Keymax) 
