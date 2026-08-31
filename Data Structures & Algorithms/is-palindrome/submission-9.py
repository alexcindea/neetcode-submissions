class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower().replace(" ", "")



        front_pointer = 0
        end_pointer = len(s) - 1
       
        while front_pointer < end_pointer:
            
            print(f"Position: {front_pointer}, Front pointer: {s[front_pointer]}")
            print(f"Position: {end_pointer}, Back pointer: {s[end_pointer]}")

            while front_pointer < end_pointer and s[front_pointer].isalnum() == False:
                front_pointer +=1
                continue
            while end_pointer > front_pointer and s[end_pointer].isalnum() == False:
                end_pointer -=1
                continue
            
            
            
            if s[front_pointer] != s[end_pointer]:
                print(f"different: {s[front_pointer]}")
                print(f"different: {s[end_pointer]}")
                return False

            front_pointer += 1
            end_pointer -= 1

        return True
            