#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
获取Excel  测试数据

"""
import os
import xlrd
import readConfig
from datetime import datetime
proDir = readConfig.proDir
# print(proDir)
def Get_xlsx(xls_name,sheet_name):

    cacelist = []
    excelDir = os.path.join(proDir,
                            "testFile",
                            "userCase",
                            xls_name)
    #打开excel文件
    workbook = xlrd.open_workbook(excelDir)
    #获取sheet列表
    sheet  = workbook.sheet_by_name(sheet_name)
    # print(sheet)
    #获取页面里有效行数
    nrows = sheet.nrows
    # print("行数:{}".format(nrows))
    #获取页面里有效列数
    # ncols = sheet.ncols
    # print("列数:{}".format(ncols))
    #获取第N行内容  返回结果是list类型
    # rows = sheet.row_values(1)
    # print("第1行内容:{}".format(rows))
    # 获取第N列内容  返回结果是list类型
    # cols = sheet.col_values(1)
    # print("第1列内容:{}".format(cols))
    #获取第n列的第n行内容
    # print(sheet.cell_value(1, 0).encode("utf-8"))
    # print(sheet.row(1)[0].value.encode("utf-8"))
    # print(sheet.cell(1, 0).value.encode("utf-8"))

    for i in range(nrows):
        if sheet.row_values(i)[0] != "caseNo":
            cacelist.append(sheet.row_values(i))
    return cacelist

def get_reportPath():
    result = os.path.join(proDir,"result")
    rePath = os.path.join(result,str(datetime.now().strftime("%Y%m%d%H%M%S")))

    if not os.path.exists(rePath):
        os.mkdir(rePath)

    reportPath = os.path.join(rePath, "report.html")

    return reportPath
