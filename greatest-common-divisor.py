class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
        a= min(A,B)
        if a==0:
            return max(A,B)
        for i in range(a,-1,-1):
            if A%i==0 and B%i==0:
                return i
                break
