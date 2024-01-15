import csv
import math


mera = {}

# 读取CSV文件并构建字典
with open("面积.csv", 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        county = row['county']
        num_employed = float(row['mera'])
        mera[county] = num_employed
    # 添加总面积
    mera['Total'] = sum(mera.values())
print(mera)


# 文件名列表
filename_list = ['车身发动机.csv', '车身挂车.csv', '零部件.csv','修理.csv','整车.csv']
nw_dict = {}

# 遍历文件名列表
for filename in filename_list:
    # 读取CSV文件
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # 初始化总CBRS和县CBRS字典
        total_cbrs = 0.0
        county_cbrs = {}

        # 解析数据并计算总CBRS和每个县的CBRS
        for row in data:
            county = row[1]
            cbrs = float(row[0])
            total_cbrs += cbrs

            # 创建空列表（如果键不存在）
            if county not in county_cbrs:
                county_cbrs[county] = 0

            # 统计每个县的CBRS
            county_cbrs[county] += cbrs
            
        # 经开区的整车制造人数 / 武汉市整车制造人数 - 经开区汽车产业就业人数/武汉汽车产业总的就业人数
        nw = 0
        sum_xi = 0
        for county, county_cbrs in county_cbrs.items():
            if(total_cbrs<1e-9):
                continue 
            print(county,county_cbrs,total_cbrs,mera[county],mera['Total'])
            nw += math.sqrt(county_cbrs/total_cbrs)*(mera[county]/mera['Total'])
        nw_dict[filename.split('.')[0]] = nw
        

# 将结果保存为CSV文件
output_filename = f"nw.csv"
with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['产业', 'nw'])
    for chanye, nw in nw_dict.items():
        writer.writerow([chanye, nw])

print("Result for", filename, "saved as", output_filename)
print()