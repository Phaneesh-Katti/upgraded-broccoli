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

# Method 2:
# recursive call with reducing longest prefix
# Time = 20 ms 
# Space = 20 MB
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

menu = input("This is a program to find longest common prefix among a list of strings\n\
For example, the following list:\n\
\tflower,flow,flight\n\
has 'fl' as the longest common prefix\n\
\n\
Enter 1 if you want to use predefined lists of strings\n\
Enter 2 if you want to enter your own list of strings\n\
Your choice: ")

if menu == "1":
    temp.append("brinjal")
    temp.append("bright")
    temp.append("bring") 

if menu == "2":
    user_item = input("Enter one list item per line to find the longest common prefix\n\
Enter 0 to finish\n")
    while user_item != "0":
        temp.append(user_item)
        user_item = input()

result = longestCommonPrefix1(temp)
print("\n\nMethod 1:\n\
string slicing + no recursion\n\
Time = 10 ms\n\
Space = 11.83 MB\n\
Item list: ", temp, "\n\
Longest common prefix: ", result)

result = longestCommonPrefix2(temp)
print("\nMethod 2:\n\
recursive call with reducing longest prefix\n\
Time = 20 ms\n\
Space = 20 MB\n\
Item list: ", temp, "\n\
Longest common prefix: ", result)

print("The Time and Space complexities have been obtained from running the code on Leetcode\n\
https://leetcode.com/")