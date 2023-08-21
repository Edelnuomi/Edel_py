#!/usr/bin/env python
# coding: utf-8
# -*- coding: UTF-8 -*-

with open("E:\\ldtools\\ide\\workspace\\ExcelMysql\\ttep\\shop_customer1.csv", "r",encoding="utf-8") as file:
    # 读取前5行数据
    print("前5行数据：")
    lines = [file.readline().strip() for i in range(5)]
    print('\n'.join(lines))

    # 读取前5列数据
    print("前5列数据：")
    file.seek(0)
    cols = [[] for i in range(5)]
    for line in file:
        items = line.strip().split(",")
        for i in range(5):
            cols[i].append(items[i])
    for col in cols:
        print(col)

    # 读取后5行数据
    print("后5行数据：")
    lines = []
    for line in file.readlines()[-5:]:
        lines.append(line.strip())
    print('\n'.join(lines))

    # 读取后5列数据
    print("后5列数据：")
    file.seek(0)
    for i in range(5):
        file.readline()
    cols = [[] for i in range(5)]
    for line in file:
        items = line.strip().split(",")
        for i in range(5):
            cols[i].append(items[i])
    for col in cols:
        print(col)

    # 统计文件总行数
    file.seek(0)
    lines = file.readlines()
    print("文件总行数：", len(lines))

