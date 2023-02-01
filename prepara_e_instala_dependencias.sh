#!/bin/bash
 sudo apt update -o Acquire::http::No-Cache=True && sudo apt-get check && \
     sudo apt install -y python3-pip && sudo apt -fy install ; 
 pip install -U selenium sendmail webdriver-manager ; 
 echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" \ 
     sudo tee /etc/apt/sources.list.d/google-chrome.list ; 
 wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; 
 sudo apt install ./google-chrome-stable_current_amd64.deb && sudo apt -fy install ; 
 curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg ; 
 sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/ ; 
 echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] \ 
     https://packages.microsoft.com/repos/edge stable main" | \ 
     sudo tee /etc/apt/sources.list.d/microsoft-edge.list && sudo rm microsoft.gpg ; 
 sudo snap remove firefox ; 
 sudo add-apt-repository ppa:mozillateam/ppa ; 
 echo ' \ 
     Package: * \ 
     Pin: release o=LP-PPA-mozillateam \ 
     Pin-Priority: 1001 \ 
     ' | sudo tee /etc/apt/preferences.d/mozilla-firefox ; 
 echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | \ 
     sudo tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox ; 
 sudo apt update -o Acquire::http::No-Cache=True && \ 
     sudo apt install -y microsoft-edge-stable firefox && \ 
     sudo apt -fy install ;
