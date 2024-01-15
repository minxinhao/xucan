import csv

total_num_of_employed = 0
num_of_employed = {}

# 文件名列表
filename_list = ['车身发动机.csv', '车身挂车.csv', '零部件.csv','修理.csv','整车.csv']

# 遍历文件名列表
for filename in filename_list:
    # 读取CSV文件
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # 解析数据并计算总CBRS和每个县的CBRS
        for row in data:
            county = row[1]
            cbrs = int(row[0])

            # 创建空列表（如果键不存在）
            if county not in num_of_employed:
                num_of_employed[county] = 0

            # 统计每个县的CBRS
            num_of_employed[county]+=cbrs
            total_num_of_employed+=cbrs

 # 将结果保存为CSV文件
output_filename = f"num_of_employed.csv"
with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['County', 'num_of_employed'])
    for county, num in num_of_employed.items():
        writer.writerow([county, num])
    writer.writerow(['total_num_of_employed', total_num_of_employed])

print("Result for", filename, "saved as", output_filename)
print()