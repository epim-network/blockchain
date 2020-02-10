import pandas as pd
import os

folder_path = "/home/epim/epim"
save_path = "/home/epim/epim-merged"
save_name = "merged.csv"

os.chdir(folder_path)
file_list = os.listdir()

print(file_list)

df = pd.read_csv(folder_path + "/" + file_list[0])
df.to_csv(save_path + "/" + save_name, encoding = "utf_8_sig", index = False)

for i in range(1, len(file_list)):
	df = pd.read_csv(folder_path + "/" + file_list[i])
	df.to_csv(save_path + "/" + save_name, encoding = "utf_8_sig", index = False, header = False, mode = 'a+')