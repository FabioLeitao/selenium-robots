# selenium-robots
Selenium Applications for monitoring robots

Para usar a versão em Python3 (testado no Python3.10), como alguns pacotes pip adicionados como dependência:

<code> sudo apt update -o Acquire::http::No-Cache=True && sudo apt-get check && sudo apt install -y python3-pip && sudo apt -fy install ; </code></br>
<code> pip install -U selenium sendmail webdriver-manager ; </code></br>
<code> echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" \\ </code></br>
<code>     sudo tee /etc/apt/sources.list.d/google-chrome.list ; </code></br>
<code> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; </code></br>
<code> sudo apt install ./google-chrome-stable_current_amd64.deb && sudo apt -fy install ; </code></br>
<code> curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg ; </code></br>
<code> sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/ ; </code></br>
<code> echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] \\ </code></br>
<code>     https://packages.microsoft.com/repos/edge stable main" | \\ </code></br>
<code>     sudo tee /etc/apt/sources.list.d/microsoft-edge.list' && sudo rm microsoft.gpg ; </code></br>
<code> sudo snap remove firefox ; </code></br>
<code> sudo add-apt-repository ppa:mozillateam/ppa ; </code></br>
<code> echo ' \\ </code></br>
<code>     Package: * \\ </code></br>
<code>     Pin: release o=LP-PPA-mozillateam \\ </code></br>
<code>     Pin-Priority: 1001 \\ </code></br>
<code>     ' | sudo tee /etc/apt/preferences.d/mozilla-firefox ; </code></br>
<code> echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | \\ </code></br>
<code>     sudo tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox ; </code></br>
<code> sudo apt update -o Acquire::http::No-Cache=True && sudo apt install -y microsoft-edge-stable firefox && sudo apt -fy install ; </code></br>
