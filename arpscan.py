#!/usr/bin/env python
# utf8

from argparse import ArgumentParser

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import srp, Ether, ARP

if __name__ == "__main__":
    parser = ArgumentParser(
        description="arp scan",
        epilog="enjoy it!",
    )
    parser.add_argument(
        "hosts",
        help="the hosts you want to ping",
    )
    args = parser.parse_args()

    packets = Ether(
        dst="ff:ff:ff:ff:ff:ff", type=0x806,
    )/ARP(hwdst="ff:ff:ff:ff:ff:ff", pdst=args.hosts)
    ans, unans = srp(packets, timeout=3, verbose=0)

    mac_info_dict = {}
    with open("mac-company") as fuck:
        for line in fuck:
            mac, info = line.split("|||")
            mac = mac.lower()
            mac_info_dict[mac] = info.rstrip("\n")

    for answer in ans:
        ip_addr = answer[1][ARP].psrc
        hardware_addr = answer[1][ARP].hwsrc
        hardware_info = mac_info_dict.get(hardware_addr[:8], "")
        print ip_addr, "\t", hardware_addr, "\t", hardware_info
