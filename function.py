from random import sample
def cr_nln(num):
        if num > 0:
            list_num = sample(range(1, num * 2),num)
            return list_num
        return "Negative value of the number of numbers!"
    #print(list_num)
    # return list_num