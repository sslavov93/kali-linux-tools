splash = """
@@@              #@@@@*
@@@@               (@@@@(
@@@@@#         @     #@@@@#
@@@@@@@.       @@.     %@@@@(
@@@@@@@@@      #@@&      &@@@@/
@@@@@@@@@@@,   .@@@@.      @@@@@,
@@@@@@@@@@@@@@# @@@@@@       @@@@@
@@@@@@@@@@@@@@@@@@@@@@@/      (@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@       @@@@@(
@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               *@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                   /@@@@@@@@@@@@@@@@@@@@@@@@@
                   &@@@@@@@@@@@@@@@@@@@@@@@@@@
                   @@@@@@@@@@@@@@@@@@@@@&@@@@@@
                  .@@@@@@@@@@@@@@@@@@@@@\033[1;31m..\033[1;m,@@@@@
                  *@@@@@@@@@@@@@@@@@@@@@,\033[1;31m...\033[1;m@@@@@
                   @@@@@@@@@@@@@@@@@@@@@@@%\033[1;31m..\033[1;m&@@@@(
                   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
                         /@@@@@@@@@@@@@@@@@@@@@@@@(
                              ,&@@@@@@@@@@@@@@@@@@@@#
                                    (@@@@@@@@@@@@@@@@@@.
                                        %@@@@@@@@@@@@@@@@@
                                          /@@@@@@@@@@@@@@@@@&
                                            /@@@@@@@@@@@@@@@@@@@,
                                              %@@@@@@@@@@@@@@@@@@@@@@%/.
                                                @@@@@@@@@@@@@@@@@@@@@@@@@%
                                                  @@@@@@@@@@@@@@@@@@@@@@@%
                                                   /@@@@@@@@@@@@@@@@@@@@.
                                                     @@@@@@@@@@@@@@@@%
                                                      ,@@@@@@@@@@@@.
                                                        @@@@@@@@@
                                                         ,@@@@#
Kali Linux Tools installer, v1.0

"""

error = "Wrong input. Please try again."

about = """# TODO"""

main_menu = """
1: Install Kali Linux tools
2: Edit repository information
3: About
00: Exit Program
"""

install = """
1: Install all tools
2: Browse and install by categories
0: Return to Main menu
00: Exit Program
"""

sources = """
1: Add Kali Linux repository
2: Remove Kali Linux repository
0: Return to Main menu
00: Exit Program
"""

categories = """
1: Information Gathering            8: Exploitation Tools
2: Vulnerability Analysis           9: Forensics Tools
3: Wireless Attacks                10: Stress Testing
4: Web Applications                11: Password Attacks
5: Sniffing & Spoofing             12: Reverse Engineering
6: Maintaining Access              13: Hardware Hacking
7: Reporting Tools                 14: Extra
"""

contains = "Kali repository/-ies found inside sources list. Aborting now."

repo = "deb http://http.kali.org/kali kali-rolling main contrib non-free"

info = """
                Information Gathering

 1: acccheck              20: enum4linux      39: ntop
 2: ace-voip              21: enumIAX         40: p0f
 3: Amap                  22: exploitdb       41: Parsero
 4: Automater             23: Fierce          42: Recon-ng
 5: bing-ip2hosts         24: Firewalk        43: SET
 6: braa                  25: fragroute       44: smtp-user-enum
 7: CaseFile              26: fragrouter      45: snmpcheck
 8: CDPSnarf              27: Ghost Phisher   46: sslcaudit
 9: cisco-torch           28: GoLismero       47: SSLsplit
10: Cookie Cadger         29: goofile         48: sslstrip
11: copy-router-config    30: hping3          49: SSLyze
12: DMitry                31: InTrace         50: THC-IPV6
13: dnmap                 32: iSMTP           51: theHarvester
14: dnsenum               33: lbd             52: TLSSLed
15: dnsmap                34: Maltego Teeth   53: twofi
16: DNSRecon              35: masscan         54: URLCrazy
17: dnstracer             36: Metagoofil      55: Wireshark
18: dnswalk               37: Miranda         56: WOL-E
19: DotDotPwn             38: Nmap            57: Xplico
"""

vulnerability = """
                Vulnerability Analysis

 1: BBQSQL                          18: ohrwurm
 2: BED                             19: openvas-administrator
 3: cisco-auditing-tool             20: openvas-cli
 4: cisco-global-exploiter          21: openvas-manager
 5: cisco-ocs                       22: openvas-scanner
 6: cisco-torch                     23: Oscanner
 7: copy-router-config              24: Powerfuzzer
 8: DBPwAudit                       25: sfuzz
 9: Doona                           26: SidGuesser
10: DotDotPwn                       27: SIPArmyKnife
11: Greenbone Security Assistant    28: sqlmap
12: GSD                             29: Sqlninja
13: HexorBase                       30: sqlsus
14: Inguma                          31: THC-IPV6
15: jSQL                            32: tnscmd10g
16: Lynis                           33: unix-privesc-check
17: Nmap                            34: Yersinia
"""

wifi = """
            Wireless Attacks

 1: Aircrack-ng          17: kalibrate-rtl
 2: Asleap               18: KillerBee
 3: Bluelog              19: Kismet
 4: BlueMaho             20: mdk3
 5: Bluepot              21: mfcuk
 6: BlueRanger           22: mfoc
 7: Bluesnarfer          23: mfterm
 8: Bully                24: Multimon-NG
 9: coWPAtty             25: PixieWPS
10: crackle              26: Reaver
11: eapmd5pass           27: redfang
12: Fern Wifi Cracker    28: RTLSDR Scanner
13: Ghost Phisher        29: Spooftooph
14: GISKismet            30: Wifi Honey
15: Gqrx                 31: Wifitap
16: gr-scan              32: Wifite
"""

sniff_n_spoof = """
        Sniffing & Spoofing

 1: Burp Suite         17: rtpmixsound
 2: DNSChef            18: sctpscan
 3: fiked              19: SIPArmyKnife
 4: hamster-sidejack   20: SIPp
 5: HexInject          21: SIPVicious
 6: iaxflood           22: SniffJoke
 7: inviteflood        23: SSLsplit
 8: iSMTP              24: sslstrip
 9: isr-evilgrade      25: THC-IPV6
10: mitmproxy          26: VoIPHopper
11: ohrwurm            27: WebScarab
12: protos-sip         28: Wifi Honey
13: rebind             29: Wireshark
14: responder          30: xspy
15: rtpbreak           31: Yersinia
16: rtpinsertsound     32: zaproxy
"""

access = """
      Maintaining Access

1: CryptCat      10: PowerSploit
2: Cymothoa      11: pwnat
3: dbd           12: RidEnum
4: dns2tcp       13: sbd
5: http-tunnel   14: U3-Pwn
6: HTTPTunnel    15: Webshells
7: Intersect     16: Weevely
8: Nishang       17: Winexe
9: polenum
"""

report = """
     Reporting Tools

1: CaseFile   6: MagicTree
2: CutyCapt   7: Metagoofil
3: dos2unix   8: Nipper-ng
4: Dradis     9: pipal
5: KeepNote
"""

exploit = """
              Exploitation Tools

1: Armitage                 10: jboss-autopwn
2: Backdoor Factory         11: Linux Exploit Suggester
3: BeEF                     12: Maltego Teeth
4: cisco-auditing-tool      13: SET
5: cisco-global-exploiter   14: ShellNoob
6: cisco-ocs                15: sqlmap
7: cisco-torch              16: THC-IPV6
8: Commix                   17: Yersinia
9: crackle
"""

forensics = """
          Forensics Tools

 1: Binwalk          13: Galleta
 2: bulk-extractor   14: Guymager
 3: Capstone         15: iPhone Backup Analyzer
 4: chntpw           16: p0f
 5: Cuckoo           17: pdf-parser
 6: dc3dd            18: pdfid
 7: ddrescue         19: pdgmail
 8: DFF              20: peepdf
 9: diStorm3         21: RegRipper
10: Dumpzilla        22: Volatility
11: extundelete      23: Xplico
12: Foremost
"""

stress_test = """
        Stress Testing

1: DHCPig          8: Reaver
2: FunkLoad        9: rtpflood
3: iaxflood       10: SlowHTTPTest
4: Inundator      11: t50
5: inviteflood    12: Termineter
6: ipv6-toolkit   13: THC-IPV6
7: mdk3           14: THC-SSL-DOS
"""

password = """
                      Password Attacks

 1: acccheck              13: HexorBase         25: phrasendrescher
 2: Burp Suite            14: THC-Hydra         26: polenum
 3: CeWL                  15: John the Ripper   27: RainbowCrack
 4: chntpw                16: Johnny            28: rcracki-mt
 5: cisco-auditing-tool   17: keimpx            29: RSMangler
 6: CmosPwd               18: Maltego Teeth     30: SQLdict
 7: creddump              19: Maskprocessor     31: Statsprocessor
 8: crunch                20: multiforcer       32: THC-pptp-bruter
 9: DBPwAudit             21: Ncrack            33: TrueCrack
10: findmyhash            22: oclgausscrack     34: WebScarab
11: gpp-decrypt           23: PACK              35: wordlists
12: hash-identifier       24: patator           36: zaproxy
"""

rev_engineer = """
    Reverse Engineering

1: apktool         7: JD-GUI
2: dex2jar         8: OllyDbg
3: diStorm3        9: smali
4: edb-debugger   10: Valgrind
5: jad            11: YARA
6: javasnoop
"""

hw_hacking = """
     Hardware Hacking
1: android-sdk   4: dex2jar
2: apktool       5: Sakis3G
3: Arduino       6: smali
"""

webapps = """
                  Web Applications

 1: apache-users     15: joomscan        29: ua-tester
 2: Arachni          16: jSQL            30: Uniscan
 3: BBQSQL           17: Maltego Teeth   31: Vega
 4: BlindElephant    18: PadBuster       32: w3af
 5: Burp Suite       19: Paros           33: WebScarab
 6: CutyCapt         20: Parsero         34: Webshag
 7: DAVTest          21: plecost         35: WebSlayer
 8: deblaze          22: Powerfuzzer     36: WebSploit
 9: DIRB             23: ProxyStrike     37: Wfuzz
10: DirBuster        24: Recon-ng        38: WPScan
11: fimap            25: Skipfish        39: XSSer
12: FunkLoad         26: sqlmap          40: zaproxy
13: Grabber          27: Sqlninja
14: jboss-autopwn    28: sqlsus
"""

categories = [info, vulnerability, wifi, sniff_n_spoof, access, report,
              exploit, forensics, stress_test, password, rev_engineer,
              hw_hacking, webapps]
