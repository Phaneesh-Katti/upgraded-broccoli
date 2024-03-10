temp = []

# Method 1:
# string slicing + no recursion
# Time = 10 ms 
# Space = 11.83 MB

def longestCommonPrefix1(strs):
        def prefix_in_all_elements(prefix, lst):
            for element in lst:
                #print(prefix, element)
                if not element.startswith(prefix):
                    return False
            return True
        
        longest = ""
        
        if len(strs) >= 1:
            #print("in condition >=1")
            longest = strs[0]
            #print(longest)

            while len(longest) > 0:
                #print("len of longest > 0")
                if prefix_in_all_elements(longest, strs[1:]):
                    return longest
                else:
                    longest = longest[:-1]

        elif len(strs) == 1:
            #print("in condition =1")
            longest = strs[0]
        
        return longest

temp = ["flower","flow","flight"]
result = longestCommonPrefix1(temp)
# print("result=", result)