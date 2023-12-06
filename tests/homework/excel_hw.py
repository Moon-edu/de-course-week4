from openpyxl import load_workbook

def find_corp_total_asset() -> int:
    nsum_est_asset_dollar = 0

    workbook = load_workbook('../../hw_data/assets.xlsx')
    worksheet = workbook.worksheets[0]

    dict_column = {}
    for i in range(0, worksheet.max_column):
        dict_column[worksheet.cell(row=1, column=i+1).value] = i

    for worksheet_data in worksheet:
        if(str(worksheet_data[dict_column['company']].value).endswith('Corp.')):
            nsum_est_asset_dollar += int(worksheet_data[dict_column['est_asset_dollar']].value)

    return nsum_est_asset_dollar

def find_llc_total_asset() -> int:
    nsum_est_asset_dollar = 0
    ncount = 0

    workbook = load_workbook('../../hw_data/assets.xlsx')
    worksheet = workbook.worksheets[0]

    dict_column = {}
    for i in range(0, worksheet.max_column):
        dict_column[worksheet.cell(row=1, column=i + 1).value] = i

    for worksheet_data in worksheet:
        if(str(worksheet_data[dict_column['company']].value).endswith('LLC')):
            nsum_est_asset_dollar += int(worksheet_data[dict_column['est_asset_dollar']].value)
            ncount += 1

    return nsum_est_asset_dollar / ncount