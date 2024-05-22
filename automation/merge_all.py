from glob import glob

filelist = glob("gugu*.txt")

with open("gugu_all.txt", "w") as handle:
    for filepath in filelist:
        with open(filepath) as handle_read:
            for line in handle_read:
                handle.write(line)
