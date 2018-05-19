# encoding: utf-8
def combine(parameter):
    print(parameter + globals()['parameter'])


parameter = 'berry'
combine('Shrub')
