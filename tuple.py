tuple1, tuple2 = (123, 'xyz'), (456, 'abc')#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

print cmp(tuple1, tuple2);#比较2个对象，前者小于后者返回-1，相等则返回0，大于后者返回1
print cmp(tuple2, tuple1);
tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)
tuple4 = (123, 'xyz')
print cmp(tuple1, tuple4)