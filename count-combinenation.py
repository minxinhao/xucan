import pandas as pd


# 读取 CSV 文件
# file_name = '分支全国-位置.csv'
# file_name = '投资全国-位置.csv'
# file_name = '投资圈内-位置.csv'
# file_name = "供应全国-位置.csv"
# file_name = "新能源.csv"
# file_name = "汽柴油.csv"
file_name = "武汉创新网络.csv"
df = pd.read_csv(file_name)

# 统计 <sheet1, sheet2> 的组合并计数
combination_count = df.groupby(["sheet1", "sheet2"]).size().reset_index(name="count")

# 输出结果到新文件
output_file = "res-" + file_name.split(".")[0] + ".csv"  # 拼接输出文件名
combination_count.to_csv(output_file, index=False)

# 输出结果
print(combination_count)
