# Main
from asyncio import subprocess
import sys # System stuff.
import os # Operating System functions.
from colorama import Fore

# For text colour.

# Modules
# SECURITY.
# ENUMERATION.
import src.modules.recpull as recpull
# OSINT.
import src.modules.shodan as shodan
import src.modules.numlook as numlook
import src.modules.geolock as geolock
# CASE-GEN.
# SDB.
# Loki.
import src.modules.loki_keygen as loki_keygen
import src.modules.loki_discovery as loki_discovery
import src.modules.loki_encrypt as loki_encrypt
import src.modules.loki_decrypt as loki_decrypt
import src.modules.cryptotrace as cryptotrace
import src.modules.vt as vt
import src.modules.mactrace as mactrace
import src.modules.ovpn as ovpn
import src.modules.pvpn as pvpn
import src.modules.flightinfo as flightinfo
import src.modules.wigle as wigle
import src.modules.bankindex as bankindex
import src.modules.exif as exif
import src.modules.ytd as ytd
import src.modules.falcon as falcon

from . import apicon
from .utils import print_hero, PROMPT

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0


def main_script():
    try:
        print_hero()
        option = input(f"{PROMPT} ")
        # SECURITY.
        # ENUMERATION.
        # OSINT.
        if option.lower() == "shodan":
            shodan.run_shodan()
            os._exit(0)

        if option.lower() == "numlook":
            numlook.numlook()
            os._exit(0)

        if option.lower() == "geolock":
            geolock.geolock()
            os._exit(0)

        if option.lower() == "cryptotrace":
            cryptotrace.cryptotrace()
            os._exit(0)

        if option.lower() == "vt":
            vt.vt()
            os._exit(0)

        if option.lower() == "ovpn":
            ovpn.ovpn()
            os._exit(0)

        if option.lower() == "pvpn":
            pvpn.pvpn()
            os._exit(0)

        if option.lower() == "mactrace":
            mactrace.mactrace()
            os._exit(0)

        if option.lower() == "flightinfo":
            flightinfo.flightinfo()
            os._exit(0)

        if option.lower() == "wigle":
            wigle.wigle()
            os._exit(0)

        if option.lower() == "bankindex":
            bankindex.bankindex()
            os._exit(0)

        if option.lower() == "ytd":
            ytd.ytd()
            os._exit(0)
        # CASE-GEN.
        # SDB.
        # Loki.
        # FORENSICS.

        # Loki.
        if option.lower() == "lokigen":
            loki_keygen.loki_keygen()
            os._exit(0)

        if option.lower() == "lokidiscovery":
            loki_discovery.loki_discovery()
            os._exit(0)

        if option.lower() == "lokiencrypt":
            loki_encrypt.loki_encrypt()
            os._exit(0)

        if option.lower() == "lokidecrypt":
            loki_decrypt.loki_decrypt()
            os._exit(0)
        # FORENSICS.
        # API config.
        if option.lower() == "apicon":
            apicon.apicon()
            os._exit(0)

        if option.lower() == "exif":
            exif.exif()
            os._exit(0)

        if option.lower() == "falcon":
            falcon.falcon()
            os._exit(0)

        if option.lower() == "recpull":
            recpull.recpull()
            os._exit(0)


    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}You interrupted the program.{Fore.WHITE}')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
