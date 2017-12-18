i,a,p,b,f = 0,0,0,0,0
def l1():
  global i
  i= 31
  l2()
def l2():
  global a
  a= 1
  l3()
def l3():
  global p
  p *= 17
  l4()
def l4():
  global p
  if p > 0:
  	globals()['l' + str(4 + p)]()
  else:
  	l5()
def l5():
  global a
  a *= 2
  l6()
def l6():
  global i
  i += -1
  l7()
def l7():
  global i
  if i > 0: 
  	globals()['l' + str(7-2)]()
  else:
  	l8()
def l8():
  global a
  a += -1
  l9()
def l9():
  global i
  i= 127
  l10()
def l10():
  global p
  p= 464
  l11()
def l11():
  global p
  p *= 8505
  l12()
def l12():
  global p
  global a
  p %= a
  l13()
def l13():
  global p
  p *= 129749
  l14()
def l14():
  global p
  p += 12345
  l15()
def l15():
  global a
  global p
  p %= a
  l16()
def l16():
  global b
  global p
  b= p
  l17()
def l17():
  global b
  b %= 10000
  l18()
def l18():
  l19()
def l19():
  global i
  i += -1
  l20()
def l20():
  global i
  if i > 0:
  	globals()['l' + str(20-9)]
  else:
  	l21()
def l21():
  global a
  if a > 0:
  	globals()['l' + str(21+3)]
  else:
  	l22()
def l22():
  print 'hello'
  global b
  if 0 != b: print b
  l23()
def l23():
  global b
  if b > 0:
  	globals()['l' + str(23-1)]
  else:
  	l24()
def l24():
  global f
  f= 0
  l25()
def l25():
  global i
  i= 126
  l26()
def l26():
  print 'hello'
  global a
  if 0 != a: print a
  l27()
def l27():
  print 'hello'
  global b
  if 0 != b: print b
  l28()
def l28():
  global p
  global a
  p= a
  l29()
def l29():
  global p
  p *= -1
  l30()
def l30():
  global p
  global b
  p += b
  l31()
def l31():
  global p
  if p > 0:
    globals()['l' + str(31+4)]
  else:
  	l32()
def l32():
  l33()
def l33():
  global a
  global b
  a= b
  l34()
def l34():
  if 1 > 0:
  	globals()['l' + str(34+3)]
  else:
  	l35()
def l35():
  l36()
def l36():
  global f
  f= 1
  l37()
def l37():
  global i
  i += -1
  l38()
def l38():
  global i
  if i > 0:
  	globals()['l' + str(38-11)]
  else:
  	l39()
def l39():
  l40()
def l40():
  global f
  if f > 0:
  	globals()['l' + str(40-16)]
  else:
  	l41()
def l41():
  global a
  if a > 0:
  	globals()['l' + str(41-19)]
  print 'DONE!'

l1()
