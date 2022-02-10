#Build a ATM machine that gives money in 100s, 50s, 10s
#Max amount that can be withdrawn is 1000 per transaction
#Max of 100 bills that can be given per transaction is 5

def atm_withdrawl(s):
    if type(s) != int:
        return "Input must be a integer"
    if s < 0:
        return "Input must be greater than zero"
    if s % 10 != 0 :
        return "Input should be a multiple of 10"
    if s > 1000:
        return "Max amount per transaction is 1000"
    
    hundred_count = s // 100
    if hundred_count > 5:
        hundred_count = 5
    balance_after_hundred = s - 100* hundred_count
    fifty_count = balance_after_hundred // 50
    balance_after_50 = balance_after_hundred - 50 * fifty_count
    ten_count = balance_after_50 // 10

    return("Money withdrawn is " + str(hundred_count) + " * 100s; " + str(fifty_count)+" * 50s; "
    + str(ten_count) + " * 10s;" )



print(atm_withdrawl(380))
print(atm_withdrawl(1380))
print(atm_withdrawl(720))
print(atm_withdrawl(-380))
print(atm_withdrawl(38))