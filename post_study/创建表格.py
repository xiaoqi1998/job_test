import xlwt


def creat_xls(sheet_name, n1_name, n2_name, table_name):#需要传入分页名称,表头，表格名称，表格名称必须添加后缀为xls
    wb = xlwt.Workbook(encoding='utf-8')  # 定义表格的编码格式
    sheet = wb.add_sheet(sheet_name)
    sheet.write(0, 0, n1_name)  # 编辑第0行第一列
    sheet.write(0, 1, n2_name)
    wb.save(table_name)
creat_xls('表一','中文','英文','翻译日志.xls')