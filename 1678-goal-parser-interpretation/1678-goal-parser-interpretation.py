class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while  i < (len(command)):
            if command[i:i+2]=="()":
                res.append("o")
                i = i+2
            elif command[i:i+4]=="(al)":
                res.append("al")
                i=i+4
            else:
                res.append(command[i])
                i= i+1
        return "".join(res)