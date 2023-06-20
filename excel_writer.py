from openpyxl import Workbook

class ExcelWriter:
    @staticmethod
    def write_products_to_excel(products, filename):
        # Создание новой рабочей книги Excel
        workbook = Workbook()

        # Создание нового листа
        sheet = workbook.active

        # Запись заголовков столбцов
        sheet['A1'] = 'Product ID'
        sheet['B1'] = 'Name'
        sheet['C1'] = 'URL'
        sheet['D1'] = 'Regular Price'
        sheet['E1'] = 'Promo Price'
        sheet['F1'] = 'Brand'

        # Добавление данных товаров в таблицу
        row = 2
        for product in products:
            sheet['A' + str(row)] = product.product_id
            sheet['B' + str(row)] = product.name
            sheet['C' + str(row)] = product.url
            sheet['D' + str(row)] = product.regular_price
            sheet['E' + str(row)] = product.promo_price
            sheet['F' + str(row)] = product.brand
            row += 1

        # Сохранение файла Excel
        workbook.save(filename)