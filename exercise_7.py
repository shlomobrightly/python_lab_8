"""

Name: is_matrix_perfect

Input: a matrix

Output: True of False

Algorithm:  1- creates a empty list "cols"
            2- in a for loop in the matrix, ittirates over numbers between 1 and the lenght of the matrix +1. if not in any of the lists in the matrix, return False.
            3- creates "x" as zero, and a for loop, running as long as x is smaller (included) than the length of the matrix - 1.
            4- in the loop above, in a for loop, adds the character in the place of x in every list in the matrix to "cols"
            5- in a for loop in "cols", ittirates over numbers between 1 and the lenght of the matrix +1. if not in "cols", return False.
            6- adds one to "x"
            7- if reached without hitting "False", returns "True".

"""



def is_matrix_perfect(matrix):
    
    cols = []
    for i in matrix:
        for x in range(1,len(matrix) + 1):
            if not x in i:
                return False
    
    x = 0
    while x <= len(matrix) - 1:
        cols = []
        for i in matrix:
            cols.append(i[x])
        for y in range(1,len(matrix) + 1):
            if not y in cols:
                return False
        x += 1
    
    return True            
    







def main():

    a = 1 #temporarely
    while a !=0:
        a = int(input("Enter the matrix dimension :"))
        if a ==0:
            print("Finish")
            return
        print("Enter the entries rowwise:")
        
        rows  = []
        for i in range(a):
            cols = []
            for x in range(a):
                cols.append(int(input()))
            rows.append(cols)
    
        for i in rows:
            print(" "*5, end = "")
            print(i)
        print("")    

        if is_matrix_perfect(rows):
            print("The Matrix is perfect")
        else:
            print("The Matrix is not perfect"  )
 
main()
