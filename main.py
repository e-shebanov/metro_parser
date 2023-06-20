from metro_parser import MetroParser
from excel_writer import ExcelWriter

msc = 31
spb = 16

metro = MetroParser()
metro.get_cookie()
products = metro.parse_catalog(msc)
ExcelWriter.write_products_to_excel(products, "metro_msc.xlsx")
products = metro.parse_catalog(spb)
ExcelWriter.write_products_to_excel(products, "metro_spb.xlsx")
