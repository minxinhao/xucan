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

        # 解析数据并计算总CBRS和每个县的CBRS
        for row in data:
            county = row[1]
            if county not in county_list:
                county_list.append(county)
            
            if county not in cbrs_dict:
                cbrs_dict[county]= []
            cbrs_dict[county].append(float(row[0]))

print("num of county:", len(county_list))
print("出现的所有县：", county_list)

print("cbrs_dict")
hhi_dict = {}
for county in cbrs_dict:
    total_cbrs = sum(cbrs_dict[county])
    # print(county,total_cbrs,cbrs_dict[county])
    if(total_cbrs < 1e-9):
        continue
    hhi =  sum(((1.0*cbrs) / total_cbrs) ** 2 for cbrs in cbrs_dict[county])
    # hhi =  sum(((1.0*cbrs) / total_cbrs) for cbrs in cbrs_dict[county])
    print(county,hhi)
    hhi_dict[county] = hhi

# 将结果保存为CSV文件
output_filename = f"hhi-for-county.csv"
with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['county', 'hhi'])
    for county, hhi in hhi_dict.items():
        writer.writerow([county, hhi])

print("Result for", filename, "saved as", output_filename)
print()