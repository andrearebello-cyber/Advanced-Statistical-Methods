#Non parametric tests- I,II
##SIGN TEST

data = [6,5,1,5,2,2,7,5,3,7,7,4]
median = 3

print("Question:",data)
print("H0: median ==",median)

data_n = [ i - 3 for i in data]

print("After subtracting by",3,"we get:",data_n)

#REMOVE ZERO
signs = [ i > 0 for i in data_n if i != 0]

p_signs = sum(signs)
n_signs =len(signs) - p_signs
print("T+ Positive:",p_signs)
print("T- Negative:",n_signs)

T = min(p_signs,n_signs)
print("Mininum T:",T)
