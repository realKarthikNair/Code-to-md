# **Code-to-md**

*inspired by [code_to_md](https://github.com/Dinex-dev/code_to_md) by @Dinex-dev*

### So What is it?

So you provide a folder with a bunch of code files, for example .c files; and this Python script will generate a single .md file with 
all these files in the following format

    1. <first comment in file> as title 
    The rest as code block
    
    2. <first comment in file> as title
    The rest as code block

and so on with next file and so on and so on and.... (RIP Engish)

### Why?

**To automate stuff like [this](https://github.com/realKarthikNair/Learning-C-Lang/blob/main/Recursion/readme.md), for example.**

### How to use (incase you didn't figure out)

##### Method 1 (for terminal lovers <3)

###### 1. On Linux and MacOS (prolly on other unix derivatives too)

    git clone https://github.com/realKarthikNair/Code-to-md
    cd Code-to-md
    chmod +x code-to-md.py

###### Usage
The script actually has a CLI based user interface as well if you run as `./code-to-md.py` or `python3 code-to-md-py` but if you want to give the path as arguments, here is how:

    ./code-to-md.py "<code-files-path>" "<extension>" "<md-file-destination>" "<md-filename>"
    # eg ./code-to-md.py "/home/karthik/karthik/Learning-C-Lang/While loops/programs" ".c" "/home/karthik/karthik/mdtest" "code.md"

###### 2. On Windows

    git clone https://github.com/realKarthikNair/Code-to-md
    cd Code-to-md
    
###### Usage (CLI based interface)

    python code-to-md.py

I haven't tested the code on Windows, so I am not sure if [passing arguments](#usage) works on the platform

##### Method 2 (for others)

1. Download [this](https://github.com/realKarthikNair/Code-to-md/archive/refs/heads/main.zip)
2. Unzip it and go to the unzipped folder
3. Run the main.py file

### Features

- Supports 2 Languages (Python and C) + can be extended for any other language with a few lines of code
- Really helpful if you need to create something like [this](https://github.com/realKarthikNair/Learning-C-Lang/blob/main/basics/basics.md) frequently

### Why not use [code_to_md](https://github.com/Dinex-dev/code_to_md) itself instead of making the same thing again from scratch in python?

~~Because I suck at bash and python is love~~

1. Bash isn't really cross-platform (e.g., Windows)
2. The more 'features' you add on a bash script, god it looks so awful for normies like me to understand (I am a linux user but making and maintaining bash scripts isn't really my cup of tea so i can't make his existing project better on my own)

### Okay so that's it: Enjoy!

### How to reach me?

<p align="left">
    <a href="https://www.instagram.com/harry_kris_" alt="instagram">
        <img src="https://img.shields.io/badge/Instagram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-yellowgreen" /></a>
    <a href="https://www.telegram.me/realkarthiknair" alt="Telegram">
        <img src="https://img.shields.io/badge/Telegram-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
    <a href="https://www.twitter.com/realkarthiknair" alt="twitter">
        <img src="https://img.shields.io/badge/Twitter-%F0%9F%91%A8%E2%80%8D%F0%9F%92%BB-orange" /></a>
</p>

### Incase you want to buy me a coffee...

<a slign="left" href="https://coindrop.to/realkarthiknair" target="_blank"><img align="left" src="https://coindrop.to/embed-button.png" style="border-radius: 10px; height: 57px !important;width: 229px !important;" alt="Coindrop.to me"></img></a>
