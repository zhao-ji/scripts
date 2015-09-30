#!/usr/bin/env python
# utf8

from argparse import ArgumentParser
from socket import gethostbyname
from time import time

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sr1, IP, UDP, DNS, DNSQR


def get_ip(host):
    if "".join(host.split(".")).isdigit():
        return host
    else:
        return gethostbyname(host)


def timestamp(need=1):
    if need == 1:
        return int(bin(int(time()*10**6))[-32:], 2)
    elif need == 2:
        return int(bin(int(time()*10**6))[-16:], 2), \
            int(bin(int(time()*10**6))[-32:-16], 2)


def time_on_the_road(stamp_base, stamp_high=0):
    # if use udp ping, stamp split to two parts, each parts is 16 bit
    # and if use tcp ping, stamp is 32 bits
    stamp = stamp_high and stamp_high * 2 ** 16 + stamp_base or stamp_base

    stamp_now = timestamp()
    if stamp_now < stamp:
        # the 32 bit stamp is overflow
        stamp_now = stamp_now + 2 ** 32

    return float(stamp_now - stamp) / (10 ** 3)


def standard_deviation(li):
    return (
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


if __name__ == "__main__":
    parser = ArgumentParser(
        description="publish your word",
        epilog="enjoy it!",
    )
    parser.add_argument("host", help="the host you want to ping")
    parser.add_argument(
        "-p", "--port",
        type=int, default=53,
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
        print "PING {host} {host_ip} by UDP".format(
            host=args.host,
            host_ip=host_ip,
        )

    rtt_list = list()
    actually_ping_count = 0
    start_time = time()

    # ans = sr1(IP(dst=host_ip)/TCP(
    #     dport=args.port, flags="S", seq=timestamp()),
    #           verbose=0)
    for i in xrange(args.count):
        stamp_base, stamp_high = timestamp(need=2)
        print "send", stamp_base, stamp_high
        print "type", type(stamp_base), type(stamp_high)
        ans = sr1(
            IP(
                dst=host_ip
            )/UDP(
                sport=stamp_base,
                dport=args.port,
            )/DNS(
                rd=0,
                id=stamp_high,
                qd=DNSQR(qname="www.baidu.com"),
            ),
            timeout=2,
            verbose=0,
        )
        print 'recv', ans.dport, ans.id
        print 'type', type(ans.dport), type(ans.id)
        print 'now', timestamp(need=2)
        print ("from {host_ip}: "
               "udp_req={udp_req} "
               "ttl={ttl} "
               "time={time_on_road} ms"
               ).format(
                   host_ip=host_ip,
                   udp_req=i,
                   ttl=ans.ttl,
                   time_on_road=time_on_the_road(ans.dport, ans.id),
        )
        rtt_list.append(time_on_the_road(ans.dport, ans.id))

    print "\n--- {host} ping statistics ---".format(host=args.host)
    print ("{packets_total} packets transmitted, "
           "{packets_survival} received, "
           "0% packet loss, time {total_time}ms"
           ).format(
               packets_total=args.count,
               packets_survival=len(rtt_list),
               total_time=(time()-start_time)*1000,
    )
    print "rtt min/avg/max/mdev = {min}/{avg}/{max}/{mdev} ms".format(
        min=min(rtt_list),
        avg=sum(rtt_list)/float(len(rtt_list)),
        max=max(rtt_list),
        mdev=standard_deviation(rtt_list),
    )
