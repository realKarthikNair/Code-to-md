#!/usr/bin/python3
#This was used to generate md files in my Learning-C-Lang repo

import os

md_file=open(f"programs.md","w"); sno=1
for i in sorted(os.listdir("programs")):
    path=os.path.join("programs", i)
    file=open(path, 'r')
    data= file.readlines(); j=0
    try:
        flag=False; first=True
        rt=1
        while True:
            title=f"### {data[j]}"; line_1=f"### {sno}. {data[j]}"
            if data[0][0:2]=='//' and j==0:
                md_file.write(line_1)
                sno+=1
            elif data[0][0:2]=="/*" and j==0:
                md_file.write(line_1)
                flag=True
                sno+=1
            elif j==0:
                md_file.write(f"### {sno}. {i}\n")
                sno+=1
            elif flag==True:
                if data[j][-3:-1]=="*/":
                    flag=False
                md_file.write(title)
            else:
                if (first!=True) and (j!=(len(data)-1)): md_file.write(f"{data[j]}")
                elif first==True:
                    md_file.write(f"```c\n{data[j]}")
                    first=False
                else:
                    md_file.write(f"{data[j]}\n```")                    
            j+=1
            
    except:
        md_file.write("\n\n")
        continue
    print(f"{output_filename} saved successfully at {output_path} !")
