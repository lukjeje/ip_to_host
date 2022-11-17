import socket
def masterf():
    print('enter ip to get doman names:')
    print('----------------------------')
    inp = input('>>>')
    print('')   


    def domain_name(ip_addr):
        dom_name = socket.gethostbyaddr(ip_addr)
        print("The domain name for " + ip_addr + " is", dom_name)
        print('---------------------------------------------------------------')
        print('')
        print('do you wnat to do another ip?')
        print('------------------------------')
        inp2 = input('(y/n)>>')
        print('')
        print('###############################################')
        if inp2 == 'y':
           print('')
           masterf()


    ip_addr = inp
    domain_name(ip_addr)
  
masterf()


