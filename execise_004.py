#import turtle
#t = turtle.Turtle()
#t.speed(0)
#t.color("pink")
#for x in range(100):
#    t.circle(x)
#    t.left(93)
#input("Press <enter>")

# coding: utf-8

print('我是能减乘除的计算器~')
while True:

    def add(x, y):
        return x + y
    def subtract(x, y):  
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y
    num=input('请输入运算符号:')
    a=int(input('请输入第一个数：'))
    b=int(input('请输入第二个数：'))
    if num =='+':
        print(a,'+',b,'=',add(a,b))
    if num =='-':
        print(a,'-',b,'=',subtract(a,b))
    if num =='*':
        print(a,'*',b,'=',multiply(a,b))
    if num =='/':
        print(a,'/',b,'=',divide(a,b))
    no =input('您还要做其他运算吗？')    
        
    i = input("您还要做其他运算吗？ ")
    if i =='no':
        break
    
    

