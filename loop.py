for letter in 'Python':     
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        
   print '当前水果 :', fruit
 
print "Good bye!"
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):       #range()函式與len()一起用於字串索引。
顯示字串中每個字元及其索引值。
   print '当前水果 :', fruits[index]
 
print "Good bye!"
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'