import glob

# Get a list of all text files ending in '_headlines.txt'
file_list = glob.glob('*_headlines.txt')

# Combine the contents of all files into 'allheadlines.txt'
with open('allheadlines.txt', 'w', encoding='utf-8') as outfile:
    for file_name in file_list:
        print("Working with file..." + file_name)
        with open(file_name, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())

print("Combined headlines saved to allheadlines.txt")
