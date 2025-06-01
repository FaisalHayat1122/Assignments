# 2. Using cls
class Counter:
    count = 0 # class variable

    def __init__(self):
        Counter.count += 1

    @classmethod # decorator
    def show_count(cls): # class method takes cls as first argument
        print(f"Total counts: {cls.count}")    


obj1 = Counter()
obj2 = Counter()
#obj3 = Counter()
Counter.show_count()        