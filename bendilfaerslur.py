from sys import stdin,stdout

def identify_form(ip_addr):
    for char in ip_addr:
        if char == ".":
            return 0
        if char == ":":
            return 1
    return None # not supposed to happen

def append_record(record, parts):
    for p in parts:
        leading_zero = 4 - len(p)
        for i in range(leading_zero):
            record.append("0")
        for char in p:
            record.append(char)
            
def get_ip4_ptr_record(ip_addr):
    blocks = ip_addr.split(".")
    record = [blocks[i] for i in range(len(blocks) - 1, -1, -1)]
    record.append("in-addr.arpa.")
    return ".".join(record)

def get_ip6_ptr_record(ip_addr):
    blocks = ip_addr.split("::")
    record = []
    if len(blocks) == 1: # no adjacent colons present
        parts = blocks[0].split(":")
        append_record(record,parts)
    else: # adjacent colons present
        first_block,second_block = blocks[0],blocks[1]
        first_parts,second_parts = first_block.split(":"),second_block.split(":")
        append_record(record, first_parts)
        for i in range((8 - len(first_parts) - len(second_parts)) << 2):
            record.append("0")
        append_record(record, second_parts)
    record_rev = [record[i] for i in range(len(record) - 1, -1, -1)]
    record_rev.append("ip6.arpa.")
    return ".".join(record_rev)

def get_ptr_record(ip_addr):
    form = identify_form(ip_addr)
    if form == None:
        raise Exception("form for IP address cannot be determined")
    if form == 0:
        return get_ip4_ptr_record(ip_addr)
    else:
        return get_ip6_ptr_record(ip_addr)
    
ip_addr = stdin.readline().strip()
stdout.write(get_ptr_record(ip_addr))
