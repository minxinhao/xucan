import csv

# 文件名列表
filename_list = ['车身发动机.csv', '车身挂车.csv', '零部件.csv','修理.csv','整车.csv']

# 遍历文件名列表
for filename in filename_list:
    # 读取CSV文件
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)

    # 初始化总CBRS和县CBRS字典
    total_cbrs = 0
    total_hhi = 0
    county_cbrs = {}
    county_hhi = {}

    # 解析数据并计算总CBRS和每个县的CBRS
    for row in data:
        county = row[1]
        cbrs = int(row[0])
        total_cbrs += cbrs

        # 创建空列表（如果键不存在）
        if county not in county_cbrs:
            county_cbrs[county] = []

        # 统计每个县的CBRS
        county_cbrs[county].append(cbrs)

    # 计算每个县的 HHI
    for county, cbrs_list in county_cbrs.items():
        country_total_cbrs = sum(cbrs_list)
        if country_total_cbrs == 0:
            county_hhi[county] = 0
        else:
            hhi = sum((cbrs / country_total_cbrs) ** 2 for cbrs in cbrs_list)
            county_hhi[county] = hhi

    # 计算总HHI的平方和
    for row in data:
        cbrs = int(row[0])
        total_hhi += (cbrs / total_cbrs) ** 2

    print("HHI for each county in", filename, ":", county_hhi)
    print("Total CBRS in", filename, ":", total_cbrs)
    print("Square Sum in", filename, ":", total_hhi)

    # 将结果保存为CSV文件
    output_filename = f"hhi-for-{filename.split('.')[0]}.csv"
    with open(output_filename, 'w', newline='', encoding='utf-8-sig') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['County', 'HHI'])
        for county, hhi in county_hhi.items():
            writer.writerow([county, hhi])
        writer.writerow(['Total HHI', total_hhi])

    print("Result for", filename, "saved as", output_filename)
    print()