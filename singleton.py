import threading
class Solution:
    __lock = threading.Lock()
    __obj = None
    # @return: The same instance of this class every time

    @classmethod
    def getInstance(cls):
        # write your code here
        if not cls.__obj:
            with cls.__lock:
                if not cls.__obj:
                    cls.__obj = cls()

        return cls.__obj