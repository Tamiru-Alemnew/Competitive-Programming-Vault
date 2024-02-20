class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            if rowIndex == 0:
                return [1]
            if rowIndex == 1 :
                return [1,1]
            
            prev_row = self.getRow(rowIndex - 1)
    
            return [1] +[prev_row[i-1]+prev_row[i] for i in range(1,len(prev_row))] +[1]
            




            

            
        