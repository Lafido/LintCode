class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, number):
        '''
        每一次插入一个数字，都有可能产生最新的最小值。需要对以前的最小值进行记录。采用下面的方式：
        每次都将number-self.min_value压栈，如果number比当前的最小值self.min_value小，那么number就成了最小值，同时压入栈中的数字小于0。
        在出栈操作时，弹出的数字value<0的时候，就采用self.min_value -= value恢复上一个最小值即可。
        '''
        if not self.stack:
            self.min_value = number
            self.stack.append(0)
        else:
            self.stack.append(number - self.min_value)
            if self.min_value > number:
                self.min_value = number

    def pop(self):
        '''在弹出一个数字的时候，需要判断栈中数字是否小于0，如果小于0，需要进行最小值恢复。
       此时的self.min_value就是对应插入的那个最小值，因此恢复上一个最小值只需要self.min_value -= value。
        '''
        value, element = self.stack.pop(), 0
        if value < 0:
            element = self.min_value
            self.min_value -= value
        else:
            element = self.min_value + value
        return element

    def min(self):
        return self.min_value