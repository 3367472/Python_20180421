# encoding: utf-8
from string import Template

s = Template('$x, glorious $x!')
print s.substitute(x='slurm')

s = Template("It's ${x}tastic!")
print s.substitute(x='slurm')

s = Template("Make $$ selling $x!")
print s.substitute(x='slurm')

s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print s.substitute(d)
