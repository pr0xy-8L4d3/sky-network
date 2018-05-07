# coding=utf-8
import multiprocessing
import subprocess
import os
import argparse
import datetime
import time
from tqdm import tqdm
from multiprocessing import Pool

os.system('clear')  # Clear the console window
print "\033[1;31m"
print ("         .▄▄ · ▄ •▄  ▄· ▄▌                   ")
print ("         ▐█ ▀. █▌▄▌▪▐█▪██▌                   ")
print ("         ▄▀▀▀█▄▐▀▀▄·▐█▌▐█▪                   ")
print ("         ▐█▄▪▐█▐█.█▌ ▐█▀·.                   ")
print ("          ▀▀▀▀ ·▀  ▀  ▀ •                    ")
print (" ▐ ▄ ▄▄▄ .▄▄▄▄▄▄▄▌ ▐ ▄▌      ▄▄▄  ▄ •▄       ")
print (" •█▌▐█▀▄.▀·•██  ██· █▌▐█▪     ▀▄ █·█▌▄▌▪     ")
print (" ▐█▐▐▌▐▀▀▪▄ ▐█.▪██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·     ")
print (" ██▐█▌▐█▄▄▌ ▐█▌·▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█.█▌     ")
print (" ▀▀ █▪ ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀·▀  ▀     ")
print ("                                             ")
print (" by: pr()xy 8l4d3 ")
print (" ver.: 1.0 ")
print
line = "+" * 80
desc = '\033[1;34m' + line + '''\n Subnet detection !! by: Pr0xy bl4d3, v: 0.1

 Example: python sky.py 192.168.x.x
          
 The above example will scan for subnets and live hosts in subnet 192.168.x.0/24 \n''' + line + "\n"
line = "+" * 80
# Just a description about the script and how to use it


# parse arguments
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('host', help='Define subnet e.g. 192.168.x.x')
args = parser.parse_args()

host = args.host


def pinger(job_q, results_q):
    """
    Do Ping
    :param job_q:
    :param results_q:
    :return:
    """
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_q.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', '-b', ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

def map_network0(pool_size=255):

    ip0_list = list()

    ip_parts1 = host.split('.')  # type: object
    base_ip1 = ip_parts1[0] + '.' + ip_parts1[1] + '.' + ip_parts1[2]  + '.' + ip_parts1[3] # type: object


    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

    for p in pool:
        p.start()

    # cue the ping processes
    for i in range(0, 255):
        jobs.put(ip_parts1[0] + '.' + ip_parts1[1] + '.' + '{0}' .format(i) + '.' + '1')


    for p in pool:
        jobs.put(None)

    for p in pool:
        p.join()

    # collect he results
    while not results.empty():
        ip = results.get()
        ip0_list.append(ip)

    return ip0_list

print "\033[0;0m"
print "+" * 40

if __name__ == '__main__':

    print "+" * 40
    starting_time = time.time()  # Get the time at which the scan was started
    print " Scanning started at %s" % (time.strftime("%I:%M:%S %p"))
    print "+" * 40
    print " Network mapping for subnets: %s" % (host)
    print "+" * 40
    print " Subnets list: "
    print "\033[1;31m"
    lst1 = map_network0()
    print '\n' .join(sorted(lst1))
    print
    print "\033[0;0m+" * 40
    my_list_len = len(sorted(lst1))


print "\n Scanning completed at %s" % (time.strftime("%I:%M:%S %p"))
ending_time = time.time()
total_time = ending_time - starting_time

if total_time <= 60:
    total_time = str(round(total_time, 2))
    print " Scanning completed in %s seconds" % (total_time)
    print
    print "+" * 40

else:
    total_time = total_time / 60
    print " Scanning completed in %s Minutes" % (total_time)
    print
    print "\033[0;0m+" * 40



while True:
    cmd = raw_input('\n\033[1;31m Do you want to scan for live hosts in subnet? Enter \'yes\'!'
                    '\n If you want to quit? Enter \'q\'!'
                    '\n ')
    if cmd == 'q':
        break
    if cmd == 'yes':
        print
        print "+" * 40
        host2 = raw_input("\033[1;31m Enter the subnet from above results to scan for live hosts: ")
        print
        print "\033[0;0m+" * 40
        print (" Please wait, scanning for live hosts in subnet"), host2
        def map_network(pool_size=255):
            ip_list = list()

            ip_parts1 = host2.split('.')  # type: object
            base_ip1 = ip_parts1[0] + '.' + ip_parts1[1] + '.' + ip_parts1[2]  + '.' + ip_parts1[3] # type: object


            jobs = multiprocessing.Queue()
            results = multiprocessing.Queue()

            pool = [multiprocessing.Process(target=pinger, args=(jobs, results)) for i in range(pool_size)]

            for p in pool:
                p.start()

    # cue the ping processes
            for i in range(0, 255):
                jobs.put(ip_parts1[0] + '.' + ip_parts1[1] + '.' + ip_parts1[2] + '.' + '{0}' .format(i))


            for p in pool:
                jobs.put(None)

            for p in pool:
                p.join()

    # collect he results
            while not results.empty():
                ip = results.get()
                ip_list.append(ip)

            return ip_list

        if __name__ == '__main__':

            print "+" * 40
            starting_time1 = time.time()  # Get the time at which the scan was started
            print " Scanning started at %s" % (time.strftime("%I:%M:%S %p"))
            print "+" * 40
            print " Network mapping in subnet: %s" % (host2)
            print "\033[0;0m+" * 40
            print " Hosts list: "
            print "\033[1;31m"

            lst1 = map_network()
            print '\n[+] ' .join(sorted(lst1))
            print "\033[0;0m+" * 40
            my_list_len = len(sorted(lst1))


        print "\n Scanning completed at %s" % (time.strftime("%I:%M:%S %p"))
        ending_time1 = time.time()
        total_time1 = ending_time1 - starting_time1

        if total_time1 <= 60:
            total_time1 = str(round(total_time1, 2))
            print " Scanning completed in %s seconds" % (total_time1)
            print
            print "+" * 40
            print
        else:
            total_time1 = total_time1 / 60
            print " Scanning completed in %s Minutes" % (total_time1)
            print
            print "+" * 40
            print







