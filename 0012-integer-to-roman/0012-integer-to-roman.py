class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        
        # decreasing order
        ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # subtractive forms from rule 2
        
        i = 0
        while num > 0:
            if num >= ints[i]: # roman numeral can fit
                res += roman[i]
                num -= ints[i]
            else:
                i += 1
        return res