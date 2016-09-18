class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        # hashcode("abcd") = (ascii(a) * 33^3 + ascii(b) * 33^2 + ascii(c) *33 + ascii(d)) % HASH_SIZE
        #                               = (97* 33^3 + 98 * 33^2 + 99 * 33 +100) % HASH_SIZE
        #                               = 3595978 % HASH_SIZE
        key_len = len(key)
        hash_code = 0
        power = 1
        for i in range(1, key_len + 1):
            hash_code += ord(key[-i]) * power
            hash_code %= HASH_SIZE
            power *= 33
            power %= HASH_SIZE
        return hash_code