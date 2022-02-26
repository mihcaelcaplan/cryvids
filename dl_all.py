from twitter_video_dl import *
import csv
import os

# grab the data from the google sheets 

# look in the folder
tgram_count = 0
twitter_count = 0

letters = ["a", "b", "c", "d", "e", "f"]

# open output sheet
with open("master.csv", "w") as outf:
    # add header to master csv
    writer = csv.writer(outf)
    writer.writerow(["Topic", "Desc", "Link", "Filename", "Downloaded"])



    for sindex, s in enumerate(os.listdir("sheets")):
        # open each input sheet
        with open("sheets/{}".format(s)) as f:
            # write the name to out sheet
            writer.writerow([s[4:-4], "", "", "", ""])

            reader = csv.reader(f)
            # make a dict of index and if twitter or not?
            for index,row in enumerate(reader):
                filename = "{}{}".format(letters[sindex], index)
                if "twitter" in row[1]:
                    # download and write to master sheet
                    try:
                        download_video(row[1], "out/{}.mov".format(filename))
                    except Exception as e: 
                        print(e)
                    writer.writerow([""]+row+[filename]+["x"])

                    
                    # record type
                    type = "twitter"
                    twitter_count+=1
                elif "t.me" in row[1]: 
                    # don't download but add to master sheet
                    writer.writerow([""]+row+[filename]+[""])
                    # record type
                    type = "telegram"
                    tgram_count+=1
                
                print(filename)

print ("twitter count: {}\ntelegram count: {}".format(twitter_count, tgram_count))


