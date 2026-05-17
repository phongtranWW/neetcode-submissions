class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ap = 0
        wp = 0
        while ap < len(abbr) and wp < len(word):
            if abbr[ap].isalpha():
                if abbr[ap] != word[wp]: return False
                ap += 1
                wp += 1
                continue
            if abbr[ap] == '0': return False
            num = 0
            while ap < len(abbr) and abbr[ap].isdigit():
                num = num * 10 + int(abbr[ap])
                ap += 1
            wp += num
        return wp == len(word) and ap == len(abbr)
                
        

            
            
            