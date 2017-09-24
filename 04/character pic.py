#Mainul Nishan


grid=[['.', '.', '.', '.', '.', '.'],    
      ['.', 'O', 'O', '.', '.', '.'],      
      ['O', 'O', 'O', 'O', '.', '.'],   
      ['O', 'O', 'O', 'O', 'O', '.'],   
      ['.', 'O', 'O', 'O', 'O', 'O'],    
      ['O', 'O', 'O', 'O', 'O', '.'],    
      ['O', 'O', 'O', 'O', '.', '.'],   
      ['.', 'O', 'O', '.', '.', '.'],    
      ['.', '.', '.', '.', '.', '.']]

def characgrid():
    for y in range(len(grid[0])):
        print('')
        for x in range(len(grid)):
             print(grid[x][y],end='')
characgrid()
   
   
   #y = the numebr of elemnts in each comun while x is the number of colummn