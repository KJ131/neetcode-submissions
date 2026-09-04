class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            number = len(i)
            string += str(number) + "#"  + i
        return string
        


    def decode(self, s: str) -> List[str]:
        string = ""
        list = []
        j = 0
        i = 0
        while i !=len(s):
            if s[i] == '#':
                number = int(s[j:i])
                for x in range(i+1, i+number+1):
                    string += s[x]
                j = i+number+1
                list.append(string)
                string = ""
                i=j
            else:
                i+=1
            
            

        return list

