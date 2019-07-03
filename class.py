    class Person :
        '这是一个学习Python定义的一个Person类'
        # 下面定义了一个类变量
        hair = 'black'
        def __init__(self, name = 'Charlie', age=8):#__init__，这个方法被称为构造方法。构造方法用于构造该类的对象，Python 通过调用构造方法返回该类的对象
            # 下面为Person对象增加2个实例变量
            self.name = name
            self.age = age
        # 下面定义了一个say方法
        def say(self, content):
            print(content)