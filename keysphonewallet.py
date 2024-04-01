items = {input().strip() for _ in range(int(input()))}
ans = []
if "keys" not in items:
    ans.append("keys")
if "phone" not in items:
    ans.append("phone")
if "wallet" not in items:
    ans.append("wallet")
print("ready") if not ans else print("\n".join(elem for elem in ans))