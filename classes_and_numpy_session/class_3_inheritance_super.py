class A:
	def hello(self):
		print ("I am in A")


class B(A):
	def hello(self):
		# super(B,self).hello()
		print ("I am in B")

def main():
	b1 = B()
	b1.hello()
	print (dir(b1))
	
if __name__ == "__main__":
	main()