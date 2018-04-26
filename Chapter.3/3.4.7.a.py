# encoding: utf-8
from string import maketrans

table = maketrans('cs', 'kz')
print len(table)
print table[97:123]
print maketrans('', '')[97:123]

print 'this is an incredible test'.translate(table)
print 'this is an incredible test'.translate(table, ' ')
