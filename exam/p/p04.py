def p04(input=2):
    output_list=None
    # ↓程式區域↓
    def dfs(i,arr):
        front = (int(i)-2)*3+97

        if(int(i)>=8):
            front+=1

        end = front + 3
        if(i== '7' or i=='9'):
            end+=1
    
        new = []

        for t in arr:
            for y in range(front,end):
                new.append(t+chr(y))

        return new
        
        output_list = ['']
        
        for i in input:
           output_list = dfs(i,output_list)
        
        if output_list == ['']:
            output_list = None
print(w)
    # ↑程式區域↑
    return output_list
