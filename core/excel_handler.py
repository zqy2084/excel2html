import xlrd


def excel_reader(filename):
    """
    read excel file and return list of sheet
        >>> import core.excel_handler
        >>> content = core.excel_handler.excel_reader('datas/test_data.xls')
        >>> len(content)
        1
        >>> keys = list(content[0].keys())
        >>> keys.sort()
        >>> keys
        ['datas', 'headers', 'name']
        >>> list(content[0]['headers'])
        ['id', 'name', 'ability', 'score']
        >>> content[0]['datas'][0]
        ['20111005.0', 'steve jobs', 'creative', '90.0']

    """
    tables = []
    rbook = xlrd.open_workbook(filename)
    for sheet in rbook.sheets():
        row_num = sheet.nrows
        col_num = sheet.ncols
        _sh = dict(name=sheet.name, headers=sheet.row_values(0))
        datas = []
        for i in range(1, row_num):
            row = [parse_cell(sheet.cell(i, j)) for j in range(col_num)]
            datas.append(row)
        _sh.update(dict(datas=datas))
        tables.append(_sh)
    return tables

def parse_cell(cell):
    """parse cell base on certain parsing rules"""
    # FIXME simply return str
    return str(cell.value)
