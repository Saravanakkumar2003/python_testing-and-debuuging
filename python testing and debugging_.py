#library
python –m pdb script.py

#normal program
def fact(x):
   f = 1
   for i in range(1,x+1):
      print (i)
      f = f * i
   return f
if __name__=="__main__":
   print ("factorial of 3=",fact(3))
#output
  C:\python36>python -m pdb fact.py
> c:\python36\fact.py(1)<module>()
-> def fact(x):
(Pdb)



#program pdb library step command
(Pdb) list
1 -> def fact(x):
2    f = 1
3    for i in range(1,x+1):
4 print (i)
5 f = f * i
6 return f
7 if __name__=="__main__":
8 print ("factorial of 3 = ", fact(3))


(Pdb) step
#output
> c:\python36\fact.py(7)<module>()
-> if __name__=="__main__":
(Pdb) next
> c:\python36\fact.py(8)<module>()
-> print ("factorial of 3 = ", fact(3))
(Pdb) next
1
2
3
factorial of 3= 6
--Return--
> c:\python36\fact.py(8)<module>()->None
-> print ("factorial of 3 = ", fact(3))
# program output next command
C:\python36>python -m pdb fact.py
> c:\python36\fact.py(1)<module>()
-> def fact(x):
(Pdb) s
> c:\python36\fact.py(7)<module>()
-> if __name__=="__main__":
(Pdb) n
> c:\python36\fact.py(8)<module>()
-> print ("factorial of 3=",fact(3))
(Pdb) s
--Call--
> c:\python36\fact.py(1)fact()
-> def fact(x):
(Pdb) n
> c:\python36\fact.py(2)fact()
-> f = 1
(Pdb) n
> c:\python36\fact.py(3)fact()
-> for i in range(1,x+1):
(Pdb) n
> c:\python36\fact.py(4)fact()
-> print (i)
(Pdb) n
1
> c:\python36\fact.py(5)fact()
-> f = f * i
(Pdb) n
> c:\python36\fact.py(3)fact()
-> for i in range(1, x + 1):
(Pdb) n
> c:\python36\fact.py(4)fact()
-> print (i)
(Pdb) f,i
(1, 2)
(Pdb)
#using break point

(Pdb) list
2 f = 1
3 for i in range(1, x + 1):
4 print (i)
5 f = f * i
6 return f
7 -> if __name__=="__main__":
8 print ("factorial of 3=",fact(3))
[EOF]
(Pdb) break 5
Breakpoint 1 at c:\python36\fact.py:5
(Pdb) continue
1
> c:\python36\fact.py(5)fact()
-> f = f * i
(Pdb) break
Num Type Disp Enb Where
1 breakpoint keep yes at c:\python36\fact.py:5
breakpoint already hit 1 time
(Pdb) continue
2
> c:\python36\fact.py(5)fact()
-> f = f * i
(Pdb) b

#break point
(Pdb) disable 1
Disabled breakpoint 1 at c:\python36\fact.py:5
(Pdb) b
Num Type Disp Enb Where
1
#breakpoint keep no at c:\python36\fact.py:5
#--breakpoint already hit 2 times


#set_trace() method to output the fact() function


