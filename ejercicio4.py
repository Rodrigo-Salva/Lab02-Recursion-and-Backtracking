def find_combinations(N, current=[], total=0):
    if total == N:
        print(" + ".join(map(str, current)))
        return
    if total > N:
        return
    for num in [1, 2, 3]:
        find_combinations(N, current + [num], total + num)

# Ask the user for a number
N = int(input("Enter the value of N: "))
print(f"Ways to obtain {N}:")
find_combinations(N)
