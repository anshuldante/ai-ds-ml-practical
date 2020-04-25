import glob

# get data file names
path = r'Exercise Files'
filenames = glob.glob(path + "/state_baby_names_*.csv")

for filename in filenames:
    print(f'file name: {filename}')
