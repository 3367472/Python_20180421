# encoding: utf-8
from string import maketrans

print 'BØLLEFRØ'.lower()
print u'BØLLEFRØ'.lower()

table = maketrans('ÆØÅ', 'æøå')
word = 'KÅPESØM'
print word.lower()
print word.translate(table)
print word.translate(table).lower()
