%%bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb
pip install playwright
git clone git://github.com/chaowenguoorg/alexamaster
python alexamaster/py/surf.py