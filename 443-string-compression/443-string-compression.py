class Solution:
    def compress(self, chars: List[str]) -> int:
#         # we can use two pointer, if the frist elemnt and the second elemnt are the same then we increment the two pointers and if they are not we move the first pointer to the second place. 
            
            
            write = 0  # update chars
            count = 1  # count consdcuteive repeatin chars
            # iterate over the string
            for read in range(1, len(chars) + 1):
                # chek for the equlaity of the chrs
                if read < len(chars) and chars[read] == chars[read - 1]:
                    count += 1
                else:
                    chars[write] = chars[read - 1]
                    write+= 1
                    if count > 1:
                        for k in str(count):
                            chars[write] = k
                            write += 1
                    count = 1
            # remove the rest of the elmets
            chars = chars[:write]
            print(chars)       
            return write
        
            


