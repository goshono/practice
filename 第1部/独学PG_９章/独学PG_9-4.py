
import csv

nums1 = ["one", "two", "three"]
nums2 = ["four", "five","six"]

with open("st.csv", "w", newline= "") as f:
    # ファイルオブジェクトをcsvオブジェクトに変換
    w = csv.writer(f, delimiter=",")
    w.writerow(nums1)
    w.writerow(nums2)