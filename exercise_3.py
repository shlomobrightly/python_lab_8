"""

Name: remove_nabor_dups

Input: string 

Output: a string with no adjacent duplicates

Algorithm:  1-  creates an empty string, and starts a_chr as the fist character of a given string
            2- in a for loop, starting from the seccond character, compares the characters to a_chr: if different, adds up to new_string.
            3- changes a to i
            4- adds the last character of the given list to the new string
            5- returns the new string





Name: is_remove_nabor_dups

Input: string 

Output: True or False

Algorithm:  itterates over a list created by remove_nabor_dups function, if finds adjacent duplicates, returns False, else, returns True



"""


def remove_nabor_dups(string):
    new_string = ""
    a_chr = 0
    for i in range(1,len(string)):
        if string[i] != string[a_chr]:
            new_string += string[a_chr]
        a_chr = i
    new_string += string[len(string) - 1]    
    return new_string    

def is_remove_nabor_dups_true(string):
    
    new_string = remove_nabor_dups(string)
    a_chr = 0
    for i in range(1,len(new_string)):
        if new_string[i] == new_string[a_chr]:
            return False
        a_chr = i
    return True    
    
        
        
def main():
    a = input("Enter a string, please: ")
#    print(is_remove_nabor_dups_true(a))
    print("After removing all duplicates:", end = " ")
    print(remove_nabor_dups(a))
    
main()    
