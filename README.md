# selenium-robots
Selenium Applications for monitoring robots

Para usar a versão em Python3 (testado no Python3.10), como alguns pacotes pip adicionados como dependência:

<code> sudo apt install python3-pip ; </code></br>
<code> pip install -U selenium sendmail webdriver-manager ; </code></br>
<code> sudo snap remove firefox ; </code></br>
<code> sudo add-apt-repository ppa:mozillateam/ppa ; </code></br>
<code> echo ' \\ </code></br>
<code>     Package: * \\ </code></br>
<code>     Pin: release o=LP-PPA-mozillateam \\ </code></br>
<code>     Pin-Priority: 1001 \\ </code></br>
<code>     ' | sudo tee /etc/apt/preferences.d/mozilla-firefox ; </code></br>
<code> echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | \\ </code></br>
<code>     sudo tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox ; </code></br>
<code> sudo apt update && sudo apt install -y firefox && sudo apt -fy install ; </code></br>
