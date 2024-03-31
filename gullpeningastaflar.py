n = int(input())
# take i coins from the ith stack
# stack with real coins can be found in one weighing
print("? " + " ".join(str(i) for i in range(1,n + 1)),flush = True)
expected = (n * n * (n + 1)) >> 1
actual = int(input())
print(f"! {actual - expected}",flush = True)
