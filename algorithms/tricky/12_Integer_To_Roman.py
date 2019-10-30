class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        roman = ""
        
        list_factor = [1000, 100, 10, 1]
        cur_factor_index = 0
        while num < list_factor[cur_factor_index]:
            cur_factor_index += 1
        while num:
            cur_val = list_factor[cur_factor_index]
            factor = num // cur_val
            num = num % cur_val
            cur_factor_index += 1
            
            if factor < 4:
                roman += dict[cur_val] * factor
            elif factor == 4:
                roman += dict[cur_val] + dict[cur_val * 5]
            elif factor < 9:
                roman += dict[cur_val * 5] + dict[cur_val] * (factor - 5)
            elif factor == 9:
                roman += dict[cur_val] + dict[cur_val * 10]
                
        return roman
        