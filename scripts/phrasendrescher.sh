echo "Installing phrasendrescher...."
wget http://www.leidecker.info/projects/phrasendrescher/phrasendrescher-1.2.2b.tar.gz
tar -zxvf phrasendrescher-1.2.2b.tar.gz
sudo apt-get -y install libssh2-1-dev libssl-dev libgpgme11-dev
cd phrasendrescher-1.2.2b
./configure --with-plugins
make
sudo make install
cd ~
sudo rm -rf phrasendrescher-1.2.2b
echo "Installation completed."
