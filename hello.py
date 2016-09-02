# name = input("please input your name !")
# print("hello" , name)

# a=input("输入第一个数字：")
# b=input("输入第二个数字：") 
# if a > b :
#     print("运行结果：",a+">"+b) 
# elif a == b : 
#     print("运行结果：",a+"="+b) 
# else : 
#     print("运行结果：",a+"<"+b)

# hei = input("please input your height(m): ")
# wei = input("please input your weight(kg): ")
# BMI = float(wei) / float(hei) ** 2
# if BMI < 18.5:
#     print("过轻")
# elif BMI < 25:
#     print("正常")
# elif BMI < 28:
#     print("过重")
# elif BMI < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# 汉诺塔的移动可以用递归函数非常简单地实现。
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
def move(n, a, b, c):
  if n <= 0:
    return
  if n == 1:
    print(a, '-->', c)
  else:
    move(n - 1, a, c, b)#将前n-1个盘子从x移动到y上
    move(1, a, b, c)#将最底下的最后一个盘子从x移动到z上
    move(n - 1, b, a, c)#将y上的n-1个盘子移动到z上
n = int(input('请输入层数：'))
move(n, 'A', 'B', 'C')































