from sys import stdin

simple = {
    "O":  ["O"],
    "A":  ["O", "A"],
    "B":  ["O", "B"],
    "AB": ["O", "A", "B", "AB"],
}
full = {
    "O-":  ["O-"],
    "O+":  ["O-", "O+"],
    "A-":  ["O-", "A-"],
    "A+":  ["O-", "O+", "A-", "A+"],
    "B-":  ["O-", "B-"],
    "B+":  ["O-", "O+", "B-", "B+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
}

def get_all_subsets_bitmask(lst):
    n = len(lst)
    subsets = []
    # Ignore empty set
    for i in range(1,1 << n):
        # Build subset based on which bits are turned on
        subset = [lst[j] for j in range(n) if (i & (1 << j))]
        subsets.append(subset)
    return subsets

# This problem can be viewed as a graph matching problem
# Construct the graph G where vertices are the people, and an edge exists between two people if one can donate to the other
# G is bipartite with the disjoint sets being the donors and the recipients respectively.
# Maximum matching using Hopcraft Karp can be run on G to return R.
# If R = m, it is possible for all recipients to receive a donation. If R <= m, it is impossible.
# Running Hopcraft Karp on G will run in O(E*sqrt(V)) = O((m + n) ^ 1.5), which will exceed the time limit given that m,n <= 10^6
# Instead, we can transform the graph into a vertex weighted graph G', where vertices represent the blood types (separate vertex for donor and recipient blood group), and vertices have a weight representing how many people have that blood type
# G' is still bipartite
# Since G' is small (maximum 16 vertices, 128 edges), we can use a generalised version of Hall's theorem
# Hall's theorem: In a biparitite graph with disjoint vertex sets V_1 and V_2, there exists a matching that saturates vertex set V_1 if and only if for every subset S of V_1, |S| <= |N(S)|.
# Generalised Hall's theorem: For every subset S of the recipient types (only 2^8 = 256 subsets in the full case), the total recipient count in S <= the total donor count among all donor types compatible with at least one type in S.
# Algorithm runs in O(1) time (ignore time taken to construct donor and recipient frequency dictionaries)
def solve(n,m,donors,recipients):
    donor_freq = {}
    for d in donors:
        donor_freq[d] = donor_freq.get(d,0) + 1
    recipient_freq = {}
    for r in recipients:
        recipient_freq[r] = recipient_freq.get(r,0) + 1
    mappings = None
    if list(recipient_freq.keys())[0] in simple:
        mappings = simple
    else:
        mappings = full
    for subset in get_all_subsets_bitmask(list(recipient_freq.keys())):
        L,compatible_donors = 0,set()
        for s in subset:
            L += recipient_freq[s]
            for d in mappings[s]:
                compatible_donors.add(d)
        R = sum(donor_freq.get(d,0) for d in compatible_donors)
        if L > R:
            return "Neibb"
    return "Jebb"
        
n = int(stdin.readline())
donors = stdin.readline().strip().split()
m = int(stdin.readline())
recipients = stdin.readline().strip().split()
print(solve(n,m,donors,recipients))
