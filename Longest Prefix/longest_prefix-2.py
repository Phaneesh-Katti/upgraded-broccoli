def longestCommonPrefix2(strs):
    def prefix_in_all_elements(initial, lst):
        prefix = initial
        #print("\t", prefix)
        for element in lst:
            #print("\t", prefix, element)
            if not element.startswith(prefix):
                prefix = prefix[:-1]
                prefix = prefix_in_all_elements(prefix, lst)
        return prefix
    
    if len(strs) == 0:
        return ""
    else:
        initial_prefix = strs[0]
        #print(initial_prefix)
        prefix = prefix_in_all_elements(initial_prefix, strs[1:])
    return prefix

temp = ["flower","flow","flight"]
result = longestCommonPrefix2(temp)