N= int(input())

tuitions  = [ int(x) for x in input().split()]

tuitions.sort()

max_income = 0
optimal_tuition = tuitions[0]

for i in range(N):
    num = N-i
    tuition = tuitions[i]
    income = num*tuition
    if income > max_income:
        optimal_tuition = tuition
        max_income = income

print(max_income, optimal_tuition)
    
