"""
Level 1: http://www.pythonchallenge.com/pc/def/map.html

Use string.maketrans and `translate` string method.

K -> M
O -> Q
E - G
"""
import string
to = 'cdefghijklmnopqrstuvwxyzab'
frm = 'abcdefghijklmnopqrstuvwxyz'

trans_table = string.maketrans(frm, to)
clue = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print clue.translate(trans_table)

next_url = 'map'.translate(trans_table)
print 'http://www.pythonchallenge.com/pc/def/{}.html'.format(next_url)
