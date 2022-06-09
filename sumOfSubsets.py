def SumOfSubsets(index, weight, total):
    if promising(index, weight):
        if(weight == M):
            global count
            print('Answer is: ',x)
            count += 1
            
        else:
            x[index] = 1
            SumOfSubsets(index+1, weight + W[index+1], total - W[index+1])
            
            x[index] = 0
            SumOfSubsets(index+1, weight, total - W[index+1])
            
def promising(index, weight):
    if index > N-1:
        return False

    if index == N-1:
        return ( (weight + total >= M) and ( (weight == M) ))
    return ( (weight + total >= M) and ( (weight == M) or ( weight + W[index+1] <= M) ))

lst = input("Enter the weights of the items: ").split(" ")
W = [int(weight) for weight in lst]+[0]
W.sort()

M = int(input("Enter the Value M: "))
N = len(W)
total = sum(W)
weight = 0
index = 0
x = [0] * (N-1) 
count = 0

print("\nThe SUM OF SUBSETS:\n")
print("Given set: ",W[1:])
SumOfSubsets(index, weight, total)
if(count == 0):
    print("No Solution for the given Sum of Subsets problem.")
