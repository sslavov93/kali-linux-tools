echo "Installing webshag...."
sudo apt-get -y install nmap
wget http://www.scrt.ch/outils/webshag/ws110.tar.gz
sudo mkdir -p webshag/
mv ws110.tar.gz webshag
cd webshag
tar -zxvf ws110.tar.gz
sudo chmod +x setup.linux.py
./setup.linux.py
cd ../


sudo mkdir -p /opt/downloads
sudo mv webshag/ /opt/downloads/
sudo chmod +x webshag_cli.py
echo "export PATH=/opt/downloads/webshag:$PATH" >> ~/.bashrc
source ~/.bashrc
echo "Installation completed."