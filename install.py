import os
import shutil
# import sys
# import traceback

import messages
import packages


class Installer():
    def __init__(self):
        self.exit = False
        self.m_menu = {"1": self.install, "2": self.sources_list,
                       "3": self.about, "00": self.exit_tool}

        self.inst_menu = {"1": self.install_all, "2": self.install_specific,
                          "3": "", "0": self.main_menu, "00": self.exit_tool}
        self.src_menu = {"1": self.setup, "2": self.remove_kali_repo,
                         "0": self.main_menu, "00": self.exit_tool}

# INSTALLER
    def install(self):
        print(messages.install)
        cmd = input("Install >>> ")
        if cmd in self.inst_menu:
            self.inst_menu[cmd]()
        else:
            print(messages.error)

    def setup(self):
        self.add_kali_repo()
        os.system("sh scripts/util/setup.sh")

    def cleanup(self):
        os.system("sh scripts/util/teardown.sh")

    def install_all(self):
        self.setup()
        for tool in packages.all_packages:
            os.system("sh " + packages.all_packages[tool])
        self.cleanup()

    def pick_packages(self):
        all_chosen = set()
        prt_count = 0
        for cat in packages.categories:
            print(messages.categories[prt_count])
            prt_count += 1
            choices = input(
                "Choose packages (comma-separated numbers) >>> ").strip(
            ).replace(" ", "").split(",")
            if choices == "all":
                for each in cat:
                    all_chosen.add(cat[each])
            else:
                for choice in choices:
                    if choice in cat:
                        all_chosen.add(cat[choice])
        return all_chosen

    def install_specific(self):
        self.setup()
        pkgs = self.pick_packages()
        for package in pkgs:
            os.system("sh " + packages.all_packages[package])
        self.cleanup()


# SOURCES
    def sources_list(self):
        print(messages.sources)
        cmd = input("Sources >>> ")
        if cmd in self.inst_menu:
            self.src_menu[cmd]()
        else:
            print(messages.error)

    def backup_sources_list(self):
        shutil.copy2("/etc/apt/sources.list", "/etc/apt/sources.list.backup")

    def add_kali_repo(self):
        self.backup_sources_list()
        with open("/etc/apt/sources.list", "r") as f:
            for line in f.readlines():
                if "kali" in line:
                    print(messages.contains)
                    return
        with open("/etc/apt/sources.list", "a") as f:
            f.write("\n\n## Kali Linux Rolling repository\n" + messages.repo)

    def remove_kali_repo(self):
        self.backup_sources_list()
        new = []
        with open("/etc/apt/sources.list", "r") as f:
            lines = f.readlines()
            for each in lines:
                if each.find("kali") < 0:
                    new.add(each)
        with open("/etc/apt/sources.list", "w") as f:
            f.write("\n".join(new))


# HELPER
    def about(self):
        print(messages.about)

# UTIL / MISC
    def exit_tool(self):
        self.exit = True
        return "Program will exit now."

    def main_menu(self):
        print(messages.main_menu)
        cmd = input("KLT >>> ")
        if cmd in self.m_menu:
            self.m_menu[cmd]()
        else:
            print(messages.error)

    def start(self):
        # print(messages.splash)
        while self.exit is False:
            self.main_menu()


inst = Installer()
inst.start()
