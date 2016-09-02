# kali-linux-tools
An automated installation script for the Kali Linux pentesting tools

# About
KLT automatically installs Kali specific packages. You can either install all tools at once or specific tools, divided by a total of 13 categories. There is also basic "sources.list" configuration edit (add/remove kali rolling repository)

# Warning
### OS Signature
Be sure to know that adding the kali-repository in your sources.list will most certainly break the OS signature - it will either show up as Kali or as nothing at all (both in grub and in UI prompts)

### Run as root
Some of the tools may be run using regular user privileges, others absolutely require root. 

### VMs
If you are running this on a Virtual Machine inside a Windows host - when installing some of the tools, your antivirus software will block the connection.

# Usage
```
$ git clone https://github.com/sslavov93/kali-linux-tools.git
$ sudo python3 install.py
```

# Used Tools
List of all Kali tools and categories can be found [here](http://tools.kali.org/tools-listing)

However, some were not included because either the installation/configuration process was far too extensive or the tool was nowhere to be adequately found (either using apt-get or from the developers' site).

List of the tools that were not included:
```
BlueMaho    SniffJoke
Bluepot     WebSlayer
Capstone    android-sdk
DFF         bing-ip2hosts
GSD         diStorm3
Inundator   gr-scan
JD-GUI      isr-evilgrade
OllyDbg     oclgausscrack
RegRipper   openvas-administrator
SQLdict 
```

# Additional Information
Installation is separated away from the main python scripts into basic shell files - this enables additional customization for each individual tool before you run the installation process.

# Tests
Extensive testing is executed using the latest [Ubuntu](http://www.ubuntu.com/) and [Debian](https://www.debian.org/distrib/) images inside a [VirtualBox](https://www.virtualbox.org/wiki/Downloads) environment. I strongly advise you to perform the setup on a fresh install, rather than on an often-used machine.


# Conclusion
In any situation will I prefer a regular and pre-setup Kali installation to this, because of the additional tools and custom kernel patches. However, if you absolutely need to execute on a Ubuntu/Debian box, give this a shot.

I created this to address the issues, posed by [katoolin](https://github.com/LionSec/katoolin). I am not trying to gain any profit out of it. It was just a fun 2-day hobby project.