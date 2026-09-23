numbers = [10,15,20,25,30]

def cal_avg_abv_20(numbers):
    lst = []
    for n in numbers:
        if n > 20:
            lst.append(n)

    return sum(lst)/len(lst)

print(cal_avg_abv_20(numbers))






    