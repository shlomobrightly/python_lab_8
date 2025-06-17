"""

Name: sep_words

Input: string

Output: prints a single word for a line

Algorithm:  1- creates a new string " "
            2- in a while loop, as long as string is not empty, creates empty "word"
            3- inputs a string
            4- ittirates over the string, and as long as the characters are not space, add them up to "word"
            5- if string in index i is equal to the length of thr given string, prints "word"
            6- if string in index i is equal to space, prints "word", then clears word
            7- if given string is empty, prints "Finish" and exits the program


"""


def sep_words():
    string = " "
    while string != "":
        word = ""
        string = input("Enter a string, please: ")
        for i in range(len(string)):
            
            if string[i] != " " or string[i] != "\t":
                word += string[i]
                
                if i == len(string) - 1:
                    print(word)

            else:
                print(word)
                word = ""
    print("Finish")    

    


def main():
    sep_words()
    
    
main()    
