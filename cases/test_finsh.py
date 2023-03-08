# import random
#
# from pages.finsh import Box1
# import os
# import re
# import time
#
#
# # def test_2():
# #     finsh_n='鲫鱼5条，鲤鱼8条，鲢鱼7条，草鱼2条，黑鱼6条，乌龟1条'
# #     fish_n='8,5,2,2,9,8'
# #     num1=0
# #     num2=0
# #     num3=0
# #     for i in range(len(finsh_n)):
# #         if finsh_n[i]=='鱼':
# #             num1=num1+int(finsh_n[i+1])
# #             num3=num3+int(num1)*int((fish_n[num2]))
# #             print('num3为%d'%num3)
# #             num2=num2+2
# #     print("鱼%d条，统计次数%d次，总价格%s"%(num1,num2,num3))
# #
# # def test_2():
# #     list=['a','b','c']
# #     list.append('d')
# #     print(list)
# #     list.insert(0,1)
# #     print(list)
# #     list1=list.index('c',3)
# #     print(list1)
# #     if 'a' in list:
# # #         list[0]='aa'
# # #         print(list)
# # #         list.pop(0)
# # #         print(list)
# # #         list.remove('a')
# #         print(list)
# #         list.clear()
# #         print(list)
# #
# #
# # def test_3():
# #     list_a=['a']
# #     list_b=['b']
# #     list_a.extend(list_b)
# #     print(list_a)
# #     print(list_a+list_b)
# # def test_4():
# #     list_41=['a']
# #     print((id(list_41)))
# #     list_42=list_41.copy()
# #     print((id(list_42)))
# #     list_43=list_42
# #     print((id(list_43)))
# #
# # def test_5():
# #     list_51=['a','c','b']
# #     print(list_51.count('a'))
# #     list_51.reverse()
# #     print(list_51)
# #
# # def test_6():
# #     """冒泡排序"""
# #     list_61=[2,6,1,9,4,5,3]
# #     for i in range(len(list_61)):
# #         for j in range(i+1,len(list_61)):
# #             if list_61[i]>list_61[j]:
# #                 list_61[i],list_61[j]=list_61[j],list_61[i]
# #     print(list_61)
# # def test_7():
# #     dit={"测试数据":'aaa',"测试数据1":"bbb"}
# #     print(dit["测试数据"])
# #     print(dit.get('测试数据'))
# #     print(dit.get("aaa"))
# #     dit["测试数据"]="ccc"
# #     print(dit)
# #     dit.setdefault("测试数据3","ddd")
# #     print(dit)
# #     dit1={"测试数据1":"通过update更新值"}
# #     dit.update(dit1)
# #     dit.pop('测试数据1')
# #     print(dit)
# #     del(dit['测试数据3'])
# #     print(dit)
# #     print(dit.items())
# #     dit.setdefault("重新测试1","重新测试数据")
# #     for i in dit.values():
# #         print(i)
# #     for i in dit:
# #         print(dit[i])
#
#
# # class Box1():
# #     def __init__(self):
# #         self.height=999
# #         self.w=0
# # box1=Box1()
# # print(box1.height)
# class Test_box():
#     def test_aa(self):
#         my_box = Box1()
#         print(my_box.height)
#
# # def test_11():
# #     n = 0
# #     m = 0
# #     a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# #     for i in a:
# #         if i > 0:
# #             n = n + 1
# #         elif i < 0:
# #             m = m + 1
# #         else:
# #             pass
# #     print("正数有%d,负数有%d" % (n, m))
# #
# #
# # def test_33():
# #     b = 'axbyczdj'
# #     print(b[::2])
# #
# #
# # def test_44():
# #     c = "hello_world_yoyo"
# #     c1 = c.split('_')
# #     print(c1)
# #
# #
# # def test_55():
# #     d = [1, 3, 5, 7]
# #     d[0], d[2] = d[2], d[0]
# #     print(d)
# #
# #
# # def test_66():
# #     num = 0
# #     for i in range(100, 1000):
# #         e = str(i)
# #         e1 = (int(e[0]) ** 3 + int(e[1]) ** 3 + int(e[2]) ** 3)
# #         if e1 == i:
# #             num = num + 1
# #             print(e1)
# #     print(num)
# #
# #
# # def test_77():
# #     f = [1, 3, 6, 9, 7, 3, 4, 6]
# #     f.sort(reverse=False)
# #     print(f)
# #     b = list(set(f))
# #
# #
# # def digui(n):
# #     if n - 1 < 0:
# #         return digui(n - 1) * (n)
# #     else:
# #         pass
# #
# #
# # digui(10)
#
#
# def test_88():
#     a="hello"
#     print(a.upper())
# def test_99():
#     a='hello'
#     print(a[::-1])
# def test100():
#     a='hello/world/haha'
#     print(a.split('/'))
# def test101():
#     a=' hello word '
#     print(a.strip())
#     print(a.title())
#
# def test_102():
#     a=['I','love','you']
#     print(''.join(a))
# def test_103():
#     a="233333"
#     print(list(map(int,a)))
# def test_104():
#     start=time.time()
#     for i in range(1,10000):
#         print(i)
#     print('共消耗时间',time.time()-start)
#
# def test_105():
#     a=[1,2,3,4]
#     print(random.sample(a,3))
#     print(len(a))
#
# def test_106():
#     a=[1,2,3,4]
#     for i in range(len(a)):
#         print(i)
#
#
#
#
#
import sys
def test_01():
    print(sys.getdefaultencoding())
