"""

Name: combineStr()

Input: two strigns: s1,s2 and a number: x

Output: string s1, with s2 inserted in capital letters in the index of x in s1

Algorithm:  1- forms a new string "comb_str"
            2 - if x is nagitive or larger than s1, exits the program with "invlid index"
            3 - adds the first x characters to comb_str
            4 - transfers s2 to capital: in a for loop, adds the difference of j from "a" to "A". then adds them up to capital_s2
            5- adds capital_s2 to comb_str, then the characters from s1, starting at s1[x], ending with s1[len(s1)]
            6 - prints(comb_str)
"""


def combineStr():
    

    s1 = input("Enter the first string:")
    s2 = input("Enter the second string:")
    x = int(input("Enter index x:"))
    
    # exit program if x is illigal
    if x < 0 or x > len(s1):
        print("Invalid index x")
        return
    
    comb_str = ""
    
    
    # add first x characters to comb_str
    for i in range (x):
        comb_str += s1[i]
    
    
    # add s2 in capital
    capital_s2 = ""
    for j in s2:
        if "A" <= j <= "Z":
            capital_s2 += j
        else:
            delta = ord(j) - ord("a")
            capital_s2 += chr(ord("A") + delta)
    comb_str += capital_s2
    
    
    # add the rest of s1
    for y in range(x,len(s1)):
        comb_str += s1[y]
    
    print("combined string" , comb_str)
def main():
    
    combineStr()    
    

main()
