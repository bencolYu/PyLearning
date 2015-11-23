import os
def h(): 
    print ('Wen Chuan')
    yield 5
    print ('Fighting!')

def g(n):
    for i in range(n):
        yield 'a'*i


#for i in g(5):
t=h()
print(t.send(None))
#print(t.send(None))

for i in g(5):
    print(i)

print(c.send(None))
print(c.send(None))
print(c.send(None))
print(c.send(None))
print(c.send(None))
print('end')