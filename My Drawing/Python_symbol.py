import turtle
rt_1 = turtle.Turtle()
rt_2 = turtle.Turtle()
rt_1.hideturtle()
rt_2.hideturtle()
scr = turtle.Screen()
scr.bgcolor("black")
# up part
rt_1.pencolor("dodger blue")
rt_1.up()
rt_1.goto(-35, 10)
rt_1.down()
rt_1.fillcolor("dodger blue")
rt_1.begin_fill()
rt_1.fd(100)
rt_1.circle(100, 90)
rt_1.fd(50)
rt_1.circle(75, 70)
rt_1.circle(370, 40)
rt_1.circle(75, 70)
rt_1.fd(40)
rt_1.lt(90)
rt_1.fd(150)
rt_1.rt(90)
rt_1.fd(20)
rt_1.rt(90)
rt_1.fd(200)
rt_1.circle(50, 70)
rt_1.circle(245, 40)
rt_1.circle(50, 70)
rt_1.fd(50)
rt_1.lt(90)
rt_1.fd(43)
rt_1.circle(-100,90)
rt_1.fd(60)
rt_1.end_fill()
rt_1.up()
rt_1.goto(-145, 150)
rt_1.down()
rt_1.pencolor("black")
rt_1.fillcolor("black")
rt_1.begin_fill()
rt_1.circle(25,360)
rt_1.end_fill()
#down part
rt_2.pencolor("yellow")
rt_2.up()
rt_2.goto(35, -10)
rt_2.down()
rt_2.fillcolor("yellow")
rt_2.begin_fill()
rt_2.rt(180)
rt_2.fd(100)
rt_2.circle(100, 90)
rt_2.fd(50)
rt_2.circle(75, 70)
rt_2.circle(370, 40)
rt_2.circle(75, 70)
rt_2.fd(40)
rt_2.lt(90)
rt_2.fd(150)
rt_2.rt(90)
rt_2.fd(20)
rt_2.rt(90)
rt_2.fd(200)
rt_2.circle(50, 70)
rt_2.circle(245, 40)
rt_2.circle(50, 70)
rt_2.fd(50)
rt_2.lt(90)
rt_2.fd(43)
rt_2.circle(-100, 90)
rt_2.fd(60)
rt_2.end_fill()
rt_2.up()
rt_2.goto(145, -150)
rt_2.down()
rt_2.pencolor("black")
rt_2.fillcolor("black")
rt_2.begin_fill()
rt_2.circle(25,360)
rt_2.end_fill()
turtle.mainloop()
