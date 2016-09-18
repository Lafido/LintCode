class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if type(nestedList) == int:
            return [nestedList]
        else:
            result = []
            for elem in nestedList:
                if type(elem) == int:
                    result.append(elem)
                else:
                    result.extend(self.flatten(elem))
            return result