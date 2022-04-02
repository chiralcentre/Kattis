W,S,C,K = map(int,input().split())
# Consider if only two groups are represented.
# If they are wolves and cabbages, transportation is possible.
# If sheep is one of the groups, one group must have size no more than K
# If the smaller group has size < K, leave that group on the boat and send the other group to the other side one by one
# If size of small group == K, one can drop them off on the other side, return to the departure shore
# move another full boat of the larger group to the other side, and then finally move the original K back over to the other side.
# Thus, if smaller group is size K, transportation is possible iff larger group size <= 2K
# If all three groups are represented, we must take either all the sheep or all wolves and cabbages on the first trip
# Thus, if either S or W+C < K, we can once again shuttle as before.
# if S or W+C == K, the same shuffling strategy as before can be performed.
print("YES") if min(S,W+C) < K or (min(S,W+C) == K and max(S,W+C) <= 2*K) else print("NO")
