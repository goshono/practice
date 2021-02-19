lists = []

rap = ["John", "Mary", "Sam"]
rock = ["Bob", "Alex", "Eve"]
djs = ["Lee", "Tanaka"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

# 新しい要素を追加するとlistsも更新されている
rap.append("George")
print(lists)
