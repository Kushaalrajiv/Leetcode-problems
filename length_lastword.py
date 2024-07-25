class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            strings=s.split(' ')
            new_list=list(strings)
            c=2
            final_word=new_list[len(new_list)-1]
            while final_word=='':
                final_word=new_list[len(new_list)-c]
                c=c+1
            return len(final_word)