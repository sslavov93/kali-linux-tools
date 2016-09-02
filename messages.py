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

 1: acccheck              20: enumIAX        39: p0f
 2: ace-voip              21: exploitdb      40: Parsero
 3: Amap                  22: Fierce         41: Recon-ng
 4: Automater             23: Firewalk       42: SET
 5: braa                  24: fragrouter     43: smtp-user-enum
 6: CaseFile              25: fragrouter     44: snmpcheck
 7: CDPSnarf              26: GhostPhisher   45: sslcaudit
 8: cisco-torch           27: GoLismero      46: SSLsplit
 9: CookieCadger          28: goofile        47: sslstrip
10: copy-router-config    29: hping3         48: SSLyze
11: DMitry                30: InTrace        49: THC-IPV6
12: dnmap                 31: iSMTP          50: theHarvester
13: dnsenum               32: lbd            51: TLSSLed
14: dnsmap                33: MaltegoTeeth   52: twofi
15: DNSRecon              34: masscan        53: URLCrazy
16: dnstracer             35: Metagoofil     54: Wireshark
17: dnswalk               36: Miranda        55: WOL-E
18: DotDotPwn             37: Nmap           56: Xplico
19: enum4linux            38: ntop
"""

vulnerability = """
              Vulnerability Analysis

 1: BBQSQL                        17: ohrwurm
 2: BED                           18: openvas-cli
 3: cisco-auditing-tool           19: openvas-manager
 4: cisco-global-exploiter        20: openvas-scanner
 5: cisco-ocs                     21: Oscanner
 6: cisco-torch                   22: Powerfuzzer
 7: copy-router-config            23: sfuzz
 8: DBPwAudit                     24: SidGuesser
 9: Doona                         25: SIPArmyKnife
10: DotDotPwn                     26: sqlmap
11: GreenboneSecurityAssistant    27: Sqlninja
12: HexorBase                     28: sqlsus
13: Inguma                        29: THC-IPV6
14: jSQL                          30: tnscmd10g
15: Lynis                         31: unix-privesc-check
16: Nmap                          32: Yersinia
"""

wifi = """
         Wireless Attacks

 1: Aircrack-ng        16: Kismet
 2: Asleap             17: mdk3
 3: Bluelog            18: mfcuk,
 4: BlueRanger,        19: mfoc
 5: Bluesnarfer        20: mfterm
 6: Bully              21: Multimon-NG
 7: coWPAtty           22: PixieWPS,
 8: crackle,           23: Reaver
 9: eapmd5pass         24: redfang
10: FernWifiCracker    25: RTLSDRScanner
11: GhostPhisher       26: Spooftooph
12: GISKismet          27: WifiHoney
13: Gqrx               28: Wifitap
14: kalibrate-rtl      29: Wifite
15: KillerBee
"""

sniff_n_spoof = """
        Sniffing & Spoofing

 1: BurpSuite          16: rtpmixsound
 2: DNSChef            17: sctpscan
 3: fiked              18: SIPArmyKnife
 4: hamster-sidejack   19: SIPp
 5: HexInject          20: SIPVicious
 6: iaxflood           21: SSLsplit
 7: inviteflood        22: sslstrip
 8: iSMTP              23: THC-IPV6
 9: mitmproxy          24: VoIPHopper
10: ohrwurm            25: WebScarab
11: protos-sip         26: WifiHoney
12: rebind             27: Wireshark
13: responder          28: xspy
14: rtpbreak           29: Yersinia
15: rtpinsertsound     30: zaproxy
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
2: BackdoorFactory          11: LinuxExploitSuggester
3: BeEF                     12: MaltegoTeeth
4: cisco-auditing-tool      13: SET
5: cisco-global-exploiter   14: ShellNoob
6: cisco-ocs                15: sqlmap
7: cisco-torch              16: THC-IPV6
8: Commix                   17: Yersinia
9: crackle
"""

forensics = """
          Forensics Tools

 1: Binwalk          11: Guymager
 2: bulk-extractor   12: iPhoneBackupAnalyzer
 3: chntpw           13: p0f
 4: Cuckoo           14: pdf-parser
 5: dc3dd            15: pdfid
 6: ddrescue         16: pdgmail
 7: Dumpzilla        17: peepdf
 8: extundelete      18: Volatility
 9: Foremost         19: Xplico
10: Galleta
"""

stress_test = """
         Stress Testing

1: DHCPig          8: rtpflood
2: FunkLoad        9: SlowHTTPTest
3: iaxflood       10: t50
4: inviteflood    11: Termineter
5: ipv6-toolkit   12: THC-IPV6
6: mdk3           13: THC-SSL-DOS
7: Reaver
"""

password = """
            Password Attacks

 1: acccheck              18: MaltegoTeeth
 2: BurpSuite             19: Maskprocessor
 3: CeWL                  20: multiforcer
 4: chntpw                21: Ncrack
 5: cisco-auditing-tool   22: PACK
 6: CmosPwd               23: patator
 7: creddump              24: phrasendrescher
 8: crunch                25: polenum
 9: DBPwAudit             26: RainbowCrack
10: findmyhash            27: rcracki-mt
11: gpp-decrypt           28: RSMangler
12: hash-identifier       29: Statsprocessor
13: HexorBase             30: THC-pptp-bruter
14: THC-Hydra             31: TrueCrack
15: JohntheRipper         32: WebScarab
16: Johnny                33: wordlists
17: keimpx                34: zaproxy
"""

rev_engineer = """
     Reverse Engineering

1: apktool        5: javasnoop
2: dex2jar        6: smali
3: edb-debugger   7: Valgrind
4: jad            8: YARA
"""

hw_hacking = """
   Hardware Hacking

1: apktool  4: Sakis3G
2: Arduino  5: smali
3: dex2jar
"""

webapps = """
                  Web Applications

 1: apache-users    14: jboss-autopwn   27: Sqlninja
 2: Arachni         15: joomscan        28: sqlsus
 3: BBQSQL          16: jSQL            29: ua-tester
 4: BlindElephant   17: MaltegoTeeth    30: Uniscan
 5: BurpSuite       18: PadBuster       31: Vega
 6: CutyCapt        19: Paros           32: w3af
 7: DAVTest         20: Parsero         33: WebScarab
 8: deblaze         21: plecost         34: Webshag
 9: DIRB            22: Powerfuzzer     35: WebSploit
10: DirBuster       23: ProxyStrike     36: Wfuzz
11: fimap           24: Recon-ng        37: WPScan
12: FunkLoad        25: Skipfish        38: XSSer
13: Grabber         26: sqlmap          39: zaproxy
"""

categories = [info, vulnerability, wifi, sniff_n_spoof, access, report,
              exploit, forensics, stress_test, password, rev_engineer,
              hw_hacking, webapps]
