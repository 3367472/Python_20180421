# encoding: utf-8
# 以正确的宽度在居中的“盒子”内打印一个句子

# 注意，证书出发运算符（//）只能用在Python 2.2以及后续版本，在之前的版本中，只是用普通除法（/）

sentence = raw_input("Sentence: ")

screen_width = 300
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print ' ' * left_margin + '|  ' + ' ' * text_width + '  |'
print ' ' * left_margin + '|  ' + sentence + '  |'
print ' ' * left_margin + '|  ' + ' ' * text_width + '  |'
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print

print
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print ' ' * left_margin + '|' + ' ' * (text_width + 4) + '|'
print ' ' * left_margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|'
print ' ' * left_margin + '|' + ' ' * (text_width + 4) + '|'
print ' ' * left_margin + '+' + '-' * (box_width - 2) + '+'
print
