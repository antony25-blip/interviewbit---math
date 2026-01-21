class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):
        if A==1:
            return 0
        a = int(math.sqrt(A))
        for i in range(2,a+1):
            if A%i ==0:
                return 0
                break
        return 1
       
            
