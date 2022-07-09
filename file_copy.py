"""
This code takes data from one file and creates its copy
    from_name -> Enter the full path of file you want to copy
    to_name -> Enter the full path of file to which you want to copy.
           * The code can overwrite existing data
"""

from_name = "" # Enter the source filename
to_name = ""  # Enter the destination filename

print(f"[+] Copying: {from_name} \n[+] Destination: {to_name}")
with open(from_name, "rb") as from_file:

    with open(to_name, "wb") as to_file:

        for line in from_file:

            to_file.write(line)

print("[+] Process complete")
