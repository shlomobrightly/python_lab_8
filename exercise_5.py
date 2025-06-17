"""

Name: is_some_row

Input: "row": list , "num": integer

Output: True or False

Algorithm:  1- defines "some_row" as zero
            2- in a for loop in "row": adds up the numbers to "some_row"
            3- returns True if the some above is equal to "num", otherwise returns False
            
            
            

Name: is_diagnal_positive

Input: a matrix

Output: True or False

Algorithm:  1- defines "index_diagnal" as zero.
            2- in a while loop, runs as long as "index_diagnal" is smaller than the length of the matrix.
            3- in a for loop in the matrix if ether one of the elements in the matrix is smaller than zero, returns false, and adds 1 to "index_diagnal". otherwise, returns true

"""            


def is_some_row(row, num):
    some_row = 0
    for i in row:
        some_row += i
    if some_row == num:
        return True
    else:
        return False


    
def is_diagnal_positive(matrix):
    index_diagnal = 0
    
    while index_diagnal < len(matrix) :
        for i in matrix:
            if i[index_diagnal] < 0:
                return False
            index_diagnal += 1    
    return True
    
    
def main():
    print("Please enter the matrix elements:")
    lst_matrix = []
    for i in range(5):
        lst_row  = []
        for i in range(5):
            lst_row.append(int(input()))
        lst_matrix.append(lst_row)
            
    print("The matrix is:")
    print("")
    for i in lst_matrix:
        print(i)    
    
    
    for y in range (len(lst_matrix) - 1):
        if not is_some_row(lst_matrix[y], y) or not is_diagnal_positive(lst_matrix):
            print("The matrix is illegal !")
            return
        else:
            print("The matrix is legal !")
            return
    
        
main()    
