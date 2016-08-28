echo "Installing DBPwAudit...."
wget http://www.cqure.net/tools/dbpwaudit_0_8.zip
sudo apt-get -y install unzip
unzip dbpwaudit_0_8.zip
sudo mkdir -p /opt/downloads/
sudo mv DBPwAudit/ /opt/downloads/
sudo rm dbpwaudit_0_8.zip

echo "export PATH=/opt/downloads/DBPwAudit:$PATH" >> ~/.bashrc
source ~/.bashrc
echo "Installation completed."
