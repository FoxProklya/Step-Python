A = int(input())
B = int(input())
H = int(input())
A <= B
if A <= H <= B:
    print("Это нормально")
elif H < A and H < B:
    print("Недосып")
elif H > A and H >= B:
    print("Пересып")
