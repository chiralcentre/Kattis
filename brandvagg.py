from sys import stdin,stdout

mappings = {"accept": 0, "log": 1, "drop": 2}
reverseMappings = {0: "accept", 1: "log", 2: "drop"}

# returns a list x
# x[0] contains list of all ports
# x[1] contains list of all IP addresses
# x[2] contains limit if it exists
# x[3] contains type of rule (0 for accept, 1 for log, 2 for drop)
def parse(rule):
    keywords = rule.split()
    ans = [[],[],None,mappings[keywords[0]]]
    for i in range(1,len(keywords)):
        args = keywords[i].split("=")
        if args[0] == "port":
            ans[0].append(args[1])
        elif args[0] == "ip":
            ans[1].append(args[1])
        else: # limit
            ans[2] = int(args[1])
    return ans

def runFirewallRules(ip,port,rules,packetId,window):
    # run through rules until packet is accepted or dropped
    for ports,ipAddresses,limit,ruleType in rules:
        # check if there is only one port and one IP address
        # impossible for packet to come from more than one IP address and sent to more than one port
        if len(ports) <= 1 and len(ipAddresses) <= 1:
            satisfyPortConds,satisfyIpConds,satisfyLimit = True,True,True
            if ports:
                satisfyPortConds = port in ports
            if ipAddresses:
                satisfyIpConds = ip in ipAddresses
            # set default value as 1001 if ip address does not exist in sliding window
            if limit:
                satisfyLimit = window.get(ip,1001) >= limit
            if satisfyPortConds and satisfyIpConds and satisfyLimit:
                stdout.write(f"{reverseMappings[ruleType]} {packetId + 1}\n")
                if ruleType != 1:
                    return           
            
N = int(stdin.readline())
rules = [parse(stdin.readline().strip()) for _ in range(N)]
P,packetIps,window,windowSize = int(stdin.readline()),[],{},0
for i in range(P):
    packet = stdin.readline().strip()
    ip,port = packet.split(":")
    packetIps.append(ip)
    if windowSize < 1000:
        windowSize += 1
    else:
        window[packetIps[i - 1000]] -= 1
    window[ip] = window.get(ip,0) + 1
    runFirewallRules(ip,port,rules,i,window)

