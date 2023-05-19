def bin2dec(bin):
    total = 0
    n = len(bin)
    for i in range(n):
        total += int(bin[n-i-1]) * (2 ** i)
    return str(total)