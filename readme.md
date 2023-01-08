# **Code-to-md**

*inspired by [code_to_md](https://github.com/Dinex-dev/code_to_md) by @Dinex-dev*


## **Generate a markdown file from a folder of programs, each program numbered with the first comment as title and the rest as code block**

### **1. Why?**

#### To generate a file like [this](https://github.com/realKarthikNair/Learning-C-Lang/blob/main/Learning_C/F.%20Loops/1.%20For%20loops/programs0/readme.md) from a directory filled with programs.

### **2. How to set-up**

Method 1: Clone the repo

        git clone https://github.com/realKarthikNair/Code-to-md
        cd Code-to-md


Method 2: [Download zip](https://github.com/realKarthikNair/Code-to-md/archive/refs/heads/main.zip) and extract it


### **3. Usage**

    ./code-to-md.py -idir <path-to-code-directory> -e <extension> -odir <md-file-destination> -o <md-filename>

for example, 
    
    ./code-to-md.py -idir /home/karthik/Temp/python/new/programs/ -e .py -odir /home/karthik/Temp/python/ -o programs.md

To choose \<current directory/programs\> as code dir and \<current directory\> as markdown location without any further prompts

    ./code-to-md.py -d

> The script also has a CLI-based interface, so you can even skip entering path as shell arguments

> The default code directory is \<current working directory\>/programs/ and the default output directory is \<current working directory\>/

> I personally have this script placed at /usr/local/bin so that I can use it from anywhere

> Okay so that's it: Enjoy!

### **4. How to reach me?**

<p align="left">
    <a href="https://www.instagram.com/karthiknair.sh" alt="instagram">
        <img src="https://img.shields.io/badge/Instagram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-yellowgreen" /></a>
    <a href="https://www.telegram.me/realkarthiknair" alt="Telegram">
        <img src="https://img.shields.io/badge/Telegram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
    <a href="https://www.twitter.com/realkarthiknair" alt="twitter">
        <img src="https://img.shields.io/badge/Twitter-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
</p>

### Incase you want to buy me a coffee...

<a slign="left" href="https://coindrop.to/realkarthiknair" target="_blank"><img align="left" src="https://coindrop.to/embed-button.png" style="border-radius: 10px; height: 57px !important;width: 229px !important;" alt="Coindrop.to me"></img></a>
