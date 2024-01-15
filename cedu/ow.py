import csv
import itertools
import math

# 文件名列表
filename_list = ['车身发动机.csv', '车身挂车.csv', '零部件.csv','修理.csv','整车.csv']
county_list = []
cbrs_dict = {}


# 遍历文件名列表
for filename in filename_list:
    # 读取CSV文件
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # 初始化总CBRS和县CBRS字典
        total_cbrs = 0.0
        induct_name = filename.split('.')[0]
        cbrs_dict[induct_name] = {}

        # 解析数据并计算总CBRS和每个县的CBRS
        for row in data:
            county = row[1]
            if county not in county_list:
                county_list.append(county)
            
            if county not in cbrs_dict[induct_name]:
                cbrs_dict[induct_name][county] = 0.0
            cbrs_dict[induct_name][county] += float(row[0])
            total_cbrs += float(row[0])
        cbrs_dict[induct_name]['Total'] = total_cbrs

# 为cbrs_dict中的每个induct添加默认值为0的县
for induct in cbrs_dict:
    for county in county_list:
        if county not in cbrs_dict[induct]:
            cbrs_dict[induct][county] = 0.0

print("num of county:", len(county_list))
print("出现的所有县：", county_list)

print("cbrs_dict")
for induct in cbrs_dict:
    print(induct,cbrs_dict[induct])

# 遍历induct的两两组合
induct_combinations = list(itertools.combinations(cbrs_dict.keys(), 2))
print("induct的两两组合：")
ow_dict = {}
for combination in induct_combinations:
    print(combination)
    sum_mul = 0.0
    sum_div_1 = 0.0
    sum_div_2 = 0.0
    for county in county_list:
        p1 = cbrs_dict[combination[0]][county]/cbrs_dict[combination[0]]['Total']
        p2 = cbrs_dict[combination[1]][county]/cbrs_dict[combination[1]]['Total']
        sum_mul += p1 * p2
        sum_div_1 += p1 ** 2
        sum_div_2 += p2 ** 2
    res_o = sum_mul / math.sqrt(sum_div_1 * sum_div_2)
    print(res_o)
    ow_dict[combination] = res_o

# 将结果保存为CSV文件
output_filename = f"ow.csv"
with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['产业', 'ow'])
    for chanye, ow in ow_dict.items():
        writer.writerow([chanye, ow])

print("Result for", filename, "saved as", output_filename)
print()