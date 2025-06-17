"""

Name: most_pos(matrix) 

Input: a list of lists

Output: the index of the row with the msot positive values

Algorithm:  1- creates a List of counters by multiplying zero times the length of the given List
            2- in a for loop in the given list, runs a nested loop over the characters: if the number is positive, adds 1 to the list of counters in the index of i.
            3- sssumes the list with the most positive numbers is the first. resembeled in the list of counters
            4- in a for loop in the list of counters, if a character is larger than "max_m", exchanges with it
            5- returns the index of max_m in the list of counters




"""""



def most_pos(matrix):
    # List of counters:
    n_c = [0]*len(matrix)
    for i in matrix:
        for y in i:
            if y >0:
                n_c[matrix.index(i)] += 1
    # max in n_c:            
    max_m = n_c[0]
    for i in n_c:
        if i > max_m:
            max_m = i
    i_n_c = n_c.index(max_m)
    return i_n_c
    
    
    
def main():
#    m = [[-1,2,3],[-1,-3,-6],[2,-3,33]]
    num_of_rows = int(input("Enter number of rows: "))
    num_of_cols = int(input("Enter number of columns: "))
    print("Enter the matrix elements:")
    cols = []
    for r in range(num_of_rows):
        rows = []
        for c in range(num_of_cols):
            rows.append(int(input()))
        cols.append(rows)
    print("")
    print("The entered matrix is:")
    for i in cols:
        print(i)
    
    print("The row with the most positive values is: ", end = "")    
    print(most_pos(cols))    
        
        
main()    
