import os
def check_ping(host):
    response = os.system("ping -n 4 " + host)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus
print(check_ping('192.168.0.100'))