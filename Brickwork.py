#OOP Part of the salution

class BrickWork:
    #Sizes of the Brick Layout and the Input/Output layout arrays
    Rows = 0
    Cols = 0
    InputLayout = []
    OutputLayout = []
    #Inputs the Rows & Cols and runs it trough a check. 
    def Input_sizes(self):
        Rows_Cols=input('Enter the Rows and Cols sizes:  ')
        S=Rows_Cols.split()
        if self.ValidateSizes(S) == False:
           print( "The entered sizes are bigger than 100 or more than 2." )
           return False
    #Inputs the matrix values
    def Input_layout(self):
        self.InputLayout = []
        for i in range(self.Rows):
           grid_nums=list(map(int, input("Enter the grid values: ").split()))
           if len( grid_nums ) != self.Cols:
               print( "The entered column count is different from the sizes you entered." )
               return False
           else:
               self.InputLayout.append(grid_nums)

        if len(self.InputLayout) != self.Rows:
            print( "The entered row count is different from the sizes you entered." )
            return False

        if self.Validation_layout() == False:
           print( "The entered rows are invalid, try again" )
           return False
    #Checks if the input value is according to the rules.
    def ValidateSizes(self,S):
        if len(S) != 2:
           return False
        self.Rows = int(S[0])
        self.Cols = int(S[1])
        if self.Rows > 100:
            return False
        if self.Cols > 100:
            return False
        return True
     #Appends checked values from layout        
    def Validation_layout(self):
        Brick_Pallet = []
        for i in range(self.Rows):
            for j in range(self.Cols):
                if self.Value_check(self.InputLayout[i][j], Brick_Pallet) == False:
                    return False
        return True
     #Checks values from layout  
    def Value_check(self,Brick_number, Brick_Pallet):
        for i in range(len(Brick_Pallet)):
            if Brick_number == Brick_Pallet[i]:
                return True
        Brick_Pallet.append(Brick_number)
        index= -1
        row_num= -1
        for j in range(self.Rows):
            try:
                index = self.InputLayout[j].index(Brick_number)
                if index != -1:
                   row_num = j
                   break
            except ValueError:
                continue
        if index + 1 != self.Cols:
            if self.InputLayout[row_num][index + 1] == Brick_number:
                if index + 2 != self.Cols:
                    if self.InputLayout[row_num][index + 2] == Brick_number:
                        return False
                    else:
                        return True
            elif row_num + 1 != self.Rows:
               if self.InputLayout[row_num + 1][index] == Brick_number:
                if row_num + 2 != self.Rows:
                    if self.InputLayout[row_num + 2][index] == Brick_number:
                        return False
                    else:
                        return True
    #Validates if the entered value is compatable.
    def GenerateOutput(self):
        if self.Cols % 2 == 0: # If the column size is even
            return self.GenerateOutputForEvenRows()
        else:
            return -1 # If the column size is odd
    #Takes the checked values from layout and Rows and Cols, and asembles in a brick wall
    def GenerateOutputForEvenRows(self):
        BrickCounter = 0
        NewLayout = []
        LayoutLastRow = []
        NewLayoutRow = []
        NewLayoutFirstRow = []
        NewLayoutSecondRow = []
        #gets the checked values in the new arrays
        LayoutLastRow.append( self.InputLayout[self.Rows - 2] )
        LayoutLastRow.append( self.InputLayout[self.Rows - 1] )
        #Adds base rows
        for i in range( 0, (int)( self.Cols ), 2 ):
            if self.InputLayout[self.Rows - 1][i] == self.InputLayout[self.Rows - 1][i + 1]:
                BrickCounter = BrickCounter + 1
                NewLayoutFirstRow.append( BrickCounter )
                BrickCounter = BrickCounter + 1
                NewLayoutFirstRow.append( BrickCounter )
            else:
                BrickCounter = BrickCounter + 1
                NewLayoutFirstRow.append( BrickCounter )
                NewLayoutFirstRow.append( BrickCounter )
        
        NewLayoutRow.append( NewLayoutFirstRow )

        nIndex = 0
        while( nIndex < self.Cols - 1 ):
            if NewLayoutFirstRow[nIndex] == NewLayoutFirstRow[nIndex + 1]:
                BrickCounter = BrickCounter + 1
                NewLayoutSecondRow.append( BrickCounter )
                NewLayoutSecondRow.append( BrickCounter )
                nIndex = nIndex + 2
            else:
                NewLayoutSecondRow.append( NewLayoutFirstRow[nIndex] )
                nIndex = nIndex + 1
                if nIndex == self.Cols - 1:
                    NewLayoutSecondRow.append( NewLayoutFirstRow[nIndex] )

        NewLayoutRow.append( NewLayoutSecondRow )

        if( self.Rows == 2 ):
            return NewLayoutRow

        for i in range( (int)( self.Rows - 1 ) ):
            if( i == 0 ):
                NewLayout.append( NewLayoutRow[0] )
                NewLayout.append( NewLayoutRow[1] )
            else:
                if( i % 2 != 0 ):
                    NewLayoutFirstRow = []
                    for i in range( 0, (int)( self.Cols ), 2 ):
                        if NewLayout[ len( NewLayout ) - 1 ][i] == NewLayout[ len( NewLayout ) - 1][i + 1]:
                            BrickCounter = BrickCounter + 1
                            NewLayoutFirstRow.append( BrickCounter )
                            BrickCounter = BrickCounter + 1
                            NewLayoutFirstRow.append( BrickCounter )
                        else:
                            BrickCounter = BrickCounter + 1
                            NewLayoutFirstRow.append( BrickCounter )
                            NewLayoutFirstRow.append( BrickCounter )
                    NewLayout.append( NewLayoutFirstRow )
                else:
                    nIndex = 0
                    NewLayoutSecondRow = []
                    while( nIndex < self.Cols - 1 ):
                        if NewLayoutFirstRow[nIndex] == NewLayoutFirstRow[nIndex + 1]:
                            BrickCounter = BrickCounter + 1
                            NewLayoutSecondRow.append( BrickCounter )
                            NewLayoutSecondRow.append( BrickCounter )
                            nIndex = nIndex + 2
                        else:
                            NewLayoutSecondRow.append( NewLayoutFirstRow[nIndex] )
                            nIndex = nIndex + 1
                            if nIndex == self.Cols - 1:
                                NewLayoutSecondRow.append( NewLayoutFirstRow[nIndex] )
                    NewLayout.append( NewLayoutSecondRow )

        return NewLayout


if __name__ == "__main__":
    BrickBuilder = BrickWork()
    Materials_Check = False
    while( Materials_Check == False ):
        Materials_Check = BrickBuilder.Input_sizes()
    Materials_Check=False
    while(Materials_Check == False):
        Materials_Check = BrickBuilder.Input_layout()

    Output = BrickBuilder.GenerateOutput()
    if( Output == -1 ):
        print ( Output )
    else:
        for i in range( len( Output ) ):
            print( Output[i] )