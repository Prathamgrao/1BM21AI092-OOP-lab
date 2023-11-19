def largest_element(li):
    num1=0
    for num in li:
        if num>num1:
            num1=num
    return(num1)
  li=[2,34,56,1]
x=largest_element(li)
print(x)
