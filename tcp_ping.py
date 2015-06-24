#!/usr/bin/env python
# utf8

from argparse import ArgumentParser
from collections import namedtuple
from itertools import repeat
from socket import gethostbyname
from time import time

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def get_ip(host):
    if "".join(host.split(".")).isdigit():
        return host
    else:
        return gethostbyname(host)


def timestamp():
    return int(str(int(time.time() * 100000))[-8:])


def time_on_the_road(stamp):
    return (timestamp() - stamp + 1) / 100


if __name__ == "__main__":
    parser = ArgumentParser(
        description="publish your word",
        epilog="enjoy it!",
    )
    parser.add_argument("host", help="the host you want to ping")
    parser.add_argument(
        "-p", "--port",
        type=int, default=80,
        help='the port your want to ping'
    )
    parser.add_argument(
        "-c", "--count",
        type=int, default=100,
        help='how many ping packets do you send?'
    )
    args = parser.parse_args()

    try:
        host_ip = get_ip(args.host)
    except StandardError, err:
        print "please check your domain name."
        raise SystemExit
    else:
        print "PING {host} {host_ip} by TCP".format(
            host=args.host,
            host_ip=host_ip,
        )

    rtt_list = list()
    start_time = time.time()

    for i in xrange(args.count):
        ans = sr1(
            IP(dst=host_ip)/TCP(dport=args.port, flags="S", seq=timestamp()),
            verbose=0,
        )
        print ("from {host_ip}: "
               "tcp_req={tcp_req} "
               "ttl={ttl} "
               "time={time_on_road} ms"
               ).format(
                   host_ip=host_ip,
                   tcp_req=i,
                   ttl=ans.ttl,
                   time_on_road=time_on_the_road(ans.ack),
               )
        rtt_list.append(time_on_the_road(ans.ack))

    print "\n--- {host} ping statistics ---".format(host=args.host)
    print ("{packets_total} packets transmitted, "
           "{packets_survival} received, "
           "0% packet loss, time {total_time}ms"
           ).format(
               packets_total=args.count,
               packets_survival=len(rtt_list),
               total_time=(time.time()-start_time)*1000,
           )

    standard_deviation = lambda li: (
        # the average of the sum of square of list
        sum(
            map(
                lambda i: i*i,
                li,
            )
        )
        /
        float(
            len(li)
        )
        -
        # the square of average of list
        (
            sum(li)
            /
            float(
                len(li)
            )
        ) ** 2
    ) ** (  # standard_deviation = variance ** 1/2
        1
        /
        float(2)
    )

    print "rtt min/avg/max/mdev = {min}/{avg}/{max}/{mdev} ms".format(
        min=min(rtt_list),
        avg=sum(rtt_list)/float(len(rtt_list)),
        max=max(rtt_list),
        mdev=int(standard_deviation(rtt_list)),
    )
