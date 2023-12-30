import copy

def tribonacci(signature, n):
    if n < len(signature):
        return signature[:n]
    list_of_fibo = copy.copy(signature)
    while len(list_of_fibo) < n:
        sum_of = 0
        for i in range(3):
            sum_of += signature[i]
        list_of_fibo.append(sum_of)
        signature.append(sum_of)
        signature.pop(0)

    return list_of_fibo
