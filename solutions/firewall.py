# In this program, you have been provided with a file containing IP addresses.
# Your task is to complete two functions below, firewall and read_ips.
# read_ips function, reads IPs from file provided, ips.txt line by line and
# return a list of all the IPs. Those IPs are then passed one by one to function
# firewall, which has to make a dicision to either block the IP or let is pass
# The rule is to block the IP if the third octet of 
# IP address is berween 50 and 100 [50 and 100 inclusive]. Else let the IP pass.
#
# Example
# 213.207.52.20 -> BLOCKED
# 212.58.102.205 -> PASS
#

def firewall(ip):
	octets = ip.split('.')
	third_octet = int(octets[2])
	if 50 <= third_octet <= 100:
		return 'BLOCKED'
	else:
		return 'PASS'

def read_ips(f):
	ips = []
	for line in f:
		ips.append(line[:-1])
	return ips


if __name__ == '__main__':
    f = open('/path-to-file/ips.txt', 'r')
    ips = read_ips(f)

    for ip in ips:
        print('{:20} -> {}'.format(ip, firewall(ip)))
