import turtle
colors = ['red','purple','blue','green','yellow','orange']
t = turtle.Pen()
t.speed(1)
turtle.bgcolor('black')
for x in range(10):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)


for chu in 'quantrimang':
   print('Chữ cái hiện tại:', chu)

