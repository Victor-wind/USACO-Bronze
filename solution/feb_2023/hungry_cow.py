import sys

N, T = [int(x) for x in input().split()]

# print(N, T)

days = list()
for _ in range(N):
    day = [int(x) for x in input().split()]
    days.append(day)

total = 0
hays = 0
# d1 < d2 < d3 ... <= T
# process all days except the last one
for i in range(N-1):
    day_i, hays_i = days[i]
    day_i_next = days[i+1][0]
    # from d_i to d_i+1 [d_i, d_i+1), there are day_i_next - day_i days 
    # Bessie may / may not eat all hays_i.
    # if she cann't eat all, add the remaining hays to days[i][1]
    days_between = day_i_next - day_i
    if days_between >= hays_i:
        total += hays_i
    else:
        total += days_between
        days[i+1][1] += (hays_i-days_between)

#process the last day, days_between should include T
day_n_1, hays_n_1 = days[N-1]
days_between = T - day_n_1 + 1 
total += min(days_between, hays_n_1)
print(total)
