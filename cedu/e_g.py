import csv

num_of_employed = {}

# 读取CSV文件并构建字典
# with open("num_of_employed.csv", 'r', encoding='utf-8-sig') as file:
with open("就业人数.csv", 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        county = row['County']
        num_employed = float(row['num_of_employed'])
        num_of_employed[county] = num_employed
    # 添加总就业人数
    # total_num_employed = int(num_of_employed.pop('total_num_of_employed'))
    # num_of_employed['Total'] = total_num_employed
    num_of_employed['Total'] = sum(num_of_employed.values())
print(num_of_employed)


hhi_dict = {'车身发动机':0.260649180307467,'车身挂车':0.018533184874926646,'零部件':0.03230874163211397,'修理':0.03219288386697385,'整车':0.5080233349545078}

# 文件名列表
filename_list = ['车身发动机.csv', '车身挂车.csv', '零部件.csv','修理.csv','整车.csv']
eg_dict = {}

# 遍历文件名列表
for filename in filename_list:
    hhi = hhi_dict[filename.split('.')[0]]
    # 读取CSV文件
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
        
        # 初始化总CBRS和县CBRS字典
        total_cbrs = 0.0
        total_hhi = 0.0
        county_cbrs = {}
        county_hhi = {}

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
        g_i = 0
        sum_xi = 0
        for county, county_cbrs in county_cbrs.items():
            print(county, county_cbrs,total_cbrs, num_of_employed[county],num_of_employed['Total'])
            print(county,"g_i:",(county_cbrs/total_cbrs - (num_of_employed[county]/num_of_employed['Total'])) ** 2)
            # print(county_cbrs/total_cbrs,(num_of_employed[county]/num_of_employed['Total']))
            # print((county_cbrs/total_cbrs - (num_of_employed[county]/num_of_employed['Total'])) ** 2)
            # print(county,num_of_employed[county],num_of_employed['Total'],(num_of_employed[county]/num_of_employed['Total'])**2)
            if(total_cbrs<1e-9 or num_of_employed[county]<1e-9):
                continue 
            g_i += (county_cbrs/total_cbrs - (num_of_employed[county]/num_of_employed['Total'])) ** 2
            sum_xi += (num_of_employed[county]/num_of_employed['Total'])**2

        print("hhi",hhi)
        print("g_i:sum(zi-xi)^2",g_i)
        print("sum_xi",sum_xi)
        print("1-sum_xi",1-sum_xi)
        print("(g_i - sum_xi * hhi) / sum_xi")
        sum_xi = 1 - sum_xi

        eg = (g_i - sum_xi * hhi) / sum_xi
        print("eg",eg)

        eg_dict[filename.split('.')[0]] = eg

        

# 将结果保存为CSV文件
output_filename = f"eg.csv"
with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['产业', 'eg'])
    for chanye, eg in eg_dict.items():
        writer.writerow([chanye, eg])

print("Result for", filename, "saved as", output_filename)
print()