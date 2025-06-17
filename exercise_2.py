'''
Name:largest_letter(s)

Input:string

Output: the largest letter in the string, no matter if it is in capital or lowercase

Algorithm:  1- in a for loop in s, if the characters are in the range of a-z acii wise, ads there delta from "a" to "A", then adds them up to a new string. otherwise, adds them up to the same list.
            2- in a for loop in the range of the length of the capital list (created above), finds the first letter, assuming it is the largest, then exists the loop 
            3- in a for loop in the range of the length of the capital list (created above), if a character is larger than capital in index "index_l" , exchanges it with "index_l", then returns the largest number in the original list.




Name:smallest_letter(s)

Input:string

Output: the smallest letter in the string, no matter if it is in capital or lowercase

Algorithm:  1- in a for loop in s, if the characters are in the range of a-z acii wise, ads there delta from "a" to "A", then adds them up to a new string. otherwise, adds them up to the same list.
            2- in a for loop in the range of the length of the capital list (created above), finds the first letter, assuming it is the largest, then exists the loop 
            3- in a for loop in the range of the length of the capital list (created above), if a character is smaller than capital in index "index_l" , exchanges it with "index_l", then returns the smallest number in the original list.



'''
def largest_letter(s):
   # new string with capital
    capital = ""
    for i in s:
        if "a" <= i <= "z":
            delta = ord(i) - ord("a")
            i = chr(ord("A") + delta)
            capital += i
        else:
            capital += i
          
    # find the first letter
    for i in range (len(capital)):
        if  "A" <= capital[i] <= "Z" or "a" <= capital[i] <= "z":
            index_l = i 
            
    
    # find index of largest
    for i in range (len(capital)):
        if "A" <= capital[i] <= "Z" or "a" <= capital[i] <= "Z":
            if capital[i] > capital[index_l]:
                index_l = i
    return s[index_l]
    
    
def smallest_letter(s):
    
   # new string with capital
    capital = ""
    for i in s:
        if "a" <= i <= "z":
            delta = ord(i) - ord("a")
            i = chr(ord("A") + delta)
            capital += i
        else:
            capital += i
          
    # find the first letter
    for i in range (len(capital)):
        if  "A" <= capital[i] <= "Z" or "a" <= capital[i] <= "z":
            index_s = i 
            


    # find index of smallest
    for i in range (len(capital)):
        if "A" <= capital[i] <= "Z" or "a" <= capital[i] <= "Z":
            if capital[i] < capital[index_s]:
                index_s = i
    return s[index_s]
    
    
    
def main():
    a = input("Enter your sentence: ")
    is_a_l = False
    for i in a:
        if "A" <= i <= "Z" or "a" <= i <= "z":
            is_a_l = True
    if not is_a_l:
        print("There were no letters")
    else:    
        print("Largest and smallest letters are:", end = " ")
        print(largest_letter(a), end = " ")
        print(smallest_letter(a))
    
    
    
    
    
main()    
    
