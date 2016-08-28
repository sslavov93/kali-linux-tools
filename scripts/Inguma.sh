echo "Installing inguma...."
wget https://inguma.eu/attachments/download/105/inguma-0.4.tar.gz
tar -zxvf inguma-0.4.tar.gz
sudo mkdir -p /opt/downloads
sudo mv inguma-0.4/ /opt/downloads/
sudo rm inguma-0.4.tar.gz

echo "export PATH=/opt/downloads/inguma-0.4:$PATH" >> ~/.bashrc
source ~/.bashrc
echo "Installation completed."
