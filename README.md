# kali-linux-tools
An automated installation script for the Kali Linux pentesting tools

# About
KLT automatically installs Kali specific packages. You can either install all tools at once or specific tools, divided by a total of 13 categories. There is also basic "sources.list" configuration edit (add/remove kali rolling repository)

# Used Tools
List of all included Kali tools and categories can be found [here](http://tools.kali.org/tools-listing)

# Additional Information
Installation is separated away from the main python scripts into basic shell files - this enables additional customization for each individual tool before you run the installation process.

# Tests
Extensive testing is executed using the latest [Ubuntu](http://www.ubuntu.com/) and [Debian](https://www.debian.org/distrib/) images inside a [VirtualBox](https://www.virtualbox.org/wiki/Downloads) environment. I strongly advise you to perform the setup on a fresh install, rather than on an often-used machine.

# Usage
```
$ git clone https://github.com/sslavov93/kali-linux-tools.git
$ sudo python3 install.py
```

# Conclusion
I created this to address the issues, posed by [katoolin](https://github.com/LionSec/katoolin). I am not trying to gain any profit out of it.