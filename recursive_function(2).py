no=int(input("Enter a Number of given number:"))
def my_sum(num):
    if num < 10:
        return num
    else:
        s = (num%10)+my_sum(num//10)
        return s
ans= my_sum(no)
print(ans)