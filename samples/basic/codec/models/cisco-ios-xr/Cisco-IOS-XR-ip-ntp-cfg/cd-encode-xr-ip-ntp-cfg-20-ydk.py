#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Encode configuration for model Cisco-IOS-XR-ip-ntp-cfg.

usage: cd-encode-xr-ip-ntp-cfg-20-ydk.py [-h] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  print debugging messages
"""

from argparse import ArgumentParser
from urlparse import urlparse

from ydk.services import CodecService
from ydk.providers import CodecServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_ip_ntp_cfg \
    as xr_ip_ntp_cfg
import logging


def config_ntp(ntp):
    """Add config data to ntp object."""
    peer_vrf = ntp.peer_vrfs.PeerVrf()
    peer_vrf.vrf_name = "default"
    peer_ipv4 = peer_vrf.peer_ipv4s.PeerIpv4()
    peer_ipv4.address_ipv4 = "10.0.0.1"
    peer_type_ipv4 = peer_ipv4.PeerTypeIpv4()
    peer_type_ipv4.peer_type = xr_ip_ntp_cfg.NtpPeerEnum.SERVER
    peer_ipv4.peer_type_ipv4.append(peer_type_ipv4)
    peer_vrf.peer_ipv4s.peer_ipv4.append(peer_ipv4)
    ntp.peer_vrfs.peer_vrf.append(peer_vrf)


if __name__ == "__main__":
    """Execute main program."""
    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", help="print debugging messages",
                        action="store_true")
    args = parser.parse_args()

    # log debug messages if verbose argument specified
    if args.verbose:
        logger = logging.getLogger("ydk")
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(("%(asctime)s - %(name)s - "
                                      "%(levelname)s - %(message)s"))
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # create codec provider
    provider = CodecServiceProvider(type="xml")

    # create codec service
    codec = CodecService()

    ntp = xr_ip_ntp_cfg.Ntp()  # create object
    config_ntp(ntp)  # add object configuration

    # encode and print object
    print(codec.encode(provider, ntp))

    provider.close()
    exit()
# End of script
