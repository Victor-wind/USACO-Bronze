import sys

#f = open("demofile.txt", "r")
f = sys.stdin

T = int(f.readline())
#print(T)

def check_conditions(n, conditions: list, conditions_list: list):
    # conditions_list contains indexes of valid (not removed) conditions

    while True:
        conditions_updated = False
        # iterate all bits
        for i in range(n):
            bit_one_list  = list()
            bit_zero_list = list()
            bit_one_val   = set()
            bit_zero_val  = set()

            # iterate all unremoved conditions
            for k in conditions_list:
                condition = conditions[k]
                bit, val = condition[0][i], condition[1]
                if bit == '1':
                    bit_one_val.add(val)
                    bit_one_list.append(k)
                if bit == '0':
                    bit_zero_val.add(val)
                    bit_zero_list.append(k)

            # bit_one_val, bit_zero_val are sets: {0},  {1}, {0, 1}, or {}
            # if bit_one_val AND bit_zero_val len <= 1, then it is done:
            # the possible statement is : if bit i == 1, then output = bit_one_val, else output = bit_zero_val   
            if len(bit_one_val) <= 1 and len(bit_zero_val) <= 1:
                print('OK')
                return

            # all conditions with val 1 could be removed from the list. Then continue to loop through all bits
            # the possible statement is : if bit i == 1, then output = bit_one_val            
            if len(bit_one_val) == 1:
                conditions_updated = True
                conditions_list = bit_zero_list            
                
            # all conditions with val 0 could be removed from the list. Then continue to loop through all bits
            # the possible statement is : if bit i == 0, then output = bit_zero_val
            if len(bit_zero_val) == 1:
                conditions_updated = True
                conditions_list = bit_one_list

            # for other cases, such as len(bit_zero_val) == 2 or len(bit_one_val) == 2,
            # the bit 1/0 could not determine a statement. So no condition is removed

            # len(bit_zero_val) == 0 or len(bit_one_val) == 0, the bit 1/0 does not exist in condition,
            # they could not determine a statement. So no condition is removed

        # as long as conditions_updated is true, it should iterate all bits again!
        # The reason: for bit i, it could not remove conditions; however for bit j (j > i),
        # it may find a statement and remove some conditions. Then bit i May be able to find a statement with reduced (after remove) conditions 
        if conditions_updated == False:
            print('LIE')
            return
            
        
for _ in range(T):
   temp = f.readline()
   #print(f'{temp=}')
   if len(temp) == 1:
      temp = f.readline()
   N, M = [ int(x) for x in temp.split()]
   #print(N, M)
   conditions = list()
   for _ in range(M):
      bits, result = f.readline().split()
      result = int(result)
      cond = [bits, result]
      conditions.append(cond)
      
   #print(conditions)
   conditions_list = [i for i in range(M)]
   
   check_conditions(N, conditions, conditions_list)   
      
