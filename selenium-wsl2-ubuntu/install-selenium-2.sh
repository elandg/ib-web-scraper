#!/usr/bin/bash

# echo "Download the 105.0.5195.52 Chrome .deb file..."
# # wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_107.0.5286.2-1_amd64.deb
# # wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-unstable/google-chrome-unstable_107.0.5286.2-1_amd64.deb
# # wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-beta/google-chrome-beta_106.0.5249.30-1_amd64.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb


echo "Install Google Chrome..."
sudo dpkg -i google-chrome-stable_current_amd64.deb

echo "Fix dependencies..."
sudo apt --fix-broken install -y

chrome_version=($(google-chrome --version))
echo "Chrome version: ${chrome_version[2]}"

# chromedriver_version=$(curl "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
# echo "Chromedriver version: ${chromedriver_version}"
# if [ "${chrome_version[2]}" == "$chromedriver_version" ]; then
#     echo "Compatible Chromedriver is available..."
#     echo "Proceeding with installation..."
# else
#     echo "Compabible Chromedriver not available...exiting"
#     exit 1
# fi

# echo "Downloading latest Chromedriver..."
# curl -Lo chromedriver_linux64.zip "https://chromedriver.storage.googleapis.com/${chromedriver_version}/chromedriver_linux64.zip"

# echo "Unzip the binary file and make it executable..."
# mkdir -p "chromedriver/stable"
# unzip -q "chromedriver_linux64.zip" -d "chromedriver/stable"
# chmod +x "chromedriver/stable/chromedriver"

# echo "Install Selenium..."
# python3 -m pip install selenium

# popd