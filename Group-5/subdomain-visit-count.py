class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        names =defaultdict(int)
        number=0
        text=""

        for i in range (len(cpdomains)):
            number,text=cpdomains[i].split()
            number=int(number)
            names[text]+=number
            text=text.split(".")
            
            for i in range(1,len(text)):
                names[".".join(text[i:])]+=number
        
        ans=[]
        for key , value in names.items():
            ans.append(str(value)+" "+key)
            
        return ans