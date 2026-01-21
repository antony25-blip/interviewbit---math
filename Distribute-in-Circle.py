class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer             
    # @return an integer
    def solve(self, A, B, C):       
        x=int((A+C-1)%B)  
        return x
