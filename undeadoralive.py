print((lambda s: "double agent" if ":)" in s and ":(" in s else "alive" if ":)" in s else "undead" if ":(" in s else "machine")(input().strip()))
