from multiping import multi_ping

addrs = ["192.168.0.1", "192.168.0.100", "192.168.0.2", "192.168.0.102", "192.168.0.101"]
responses, no_responses = multi_ping(addrs, timeout=3, retry=3)
# Ping the addresses up to 4 times (initial ping + 3 retries), over the
# course of 2 seconds. This means that for those addresses that do not
# respond another ping will be sent every 0.5 seconds.
for addr, rtt in responses.items():
    print(f"{addr} responded in {rtt} seconds")	