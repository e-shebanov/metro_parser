from selenium import webdriver
import json
import requests
from product import Product


class MetroParser(object):

    def __init__(self):
        self.cookie = None

    def get_cookie(self):
        # Открываем браузер и получаем свежие куки
        driver = webdriver.Chrome()

        # Открываем сайт
        driver.get('https://online.metro-cc.ru/')

        # Получаем все куки
        cookies = driver.get_cookies()

        self.cookie = ""
        # Сохраняем куки в переменной self.cookie
        for cookie in cookies:
            self.cookie += cookie['name'] + '=' + cookie['value'] + "; "

        # Закрываем браузер
        driver.quit()

    def parse_catalog(self, city_code):

        url = 'https://api.metro-cc.ru/products-api/graph'

        # Определите параметры запроса в соответствии с вашими требованиями
        payload = {
            "query": "query Query($storeId: Int!, $slug: String!, $attributes:[AttributeFilter], $filters: ["
                     "FieldFilter], $from: Int!, $size: Int!, $sort: InCategorySort, $in_stock: Boolean, "
                     "$eshop_order: Boolean, $is_action: Boolean, $price_levels: Boolean) {\n    category (storeId: "
                     "$storeId, slug: $slug, inStock: $in_stock, eshopAvailability: $eshop_order, "
                     "isPromo: $is_action, priceLevels: $price_levels) {\n      id\n      name\n      slug\n      "
                     "id\n      parent_id\n      meta {\n        description\n        h1\n        title\n        "
                     "keywords\n      }\n      disclaimer\n      description {\n        top\n        main\n        "
                     "bottom\n      }\n      breadcrumbs {\n        category_type\n        id\n        name\n        "
                     "parent_id\n        parent_slug\n        slug\n      }\n      promo_banners {\n        id\n      "
                     "  image\n        name\n        category_ids\n        virtual_ids\n        type\n        "
                     "sort_order\n        url\n        is_target_blank\n        analytics {\n          name\n         "
                     " category\n          brand\n          type\n          start_date\n          end_date\n        "
                     "}\n      }\n\n\n      dynamic_categories(from: 0, size: 9999) {\n        slug\n        name\n   "
                     "     id\n      }\n      filters {\n        facets {\n          key\n          total\n          "
                     "filter {\n            id\n            name\n            display_title\n            is_list\n    "
                     "        is_main\n            text_filter\n            is_range\n            category_id\n       "
                     "     category_name\n            values {\n              slug\n              text\n              "
                     "total\n            }\n          }\n        }\n      }\n      total\n      prices {\n        "
                     "max\n        min\n      }\n      pricesFiltered {\n        max\n        min\n      }\n      "
                     "products(attributeFilters: $attributes, from: $from, size: $size, sort: $sort, fieldFilters: "
                     "$filters)  {\n        health_warning\n        limited_sale_qty\n        id\n        slug\n      "
                     "  name\n        name_highlight\n        article\n        is_target\n        category_id\n       "
                     " url\n        images\n        pick_up\n        icons {\n          id\n          "
                     "badge_bg_colors\n          caption\n          image\n          type\n          "
                     "is_only_for_sales\n          stores\n          caption_settings {\n            colors\n         "
                     "   text\n          }\n          stores\n          sort\n          image_png\n          "
                     "image_svg\n          description\n          end_date\n          start_date\n          status\n  "
                     "      }\n        manufacturer {\n          id\n          image\n          name\n        }\n     "
                     "   packing {\n          size\n          type\n          pack_factors {\n            instamart\n "
                     "         }\n        }\n        stocks {\n          value\n          text\n          "
                     "eshop_availability\n          scale\n          prices_per_unit {\n            old_price\n       "
                     "     offline {\n              price\n              old_price\n              type\n              "
                     "offline_discount\n              offline_promo\n            }\n            price\n            "
                     "is_promo\n            levels {\n              count\n              price\n            }\n       "
                     "     discount\n          }\n          prices {\n            price\n            is_promo\n       "
                     "     old_price\n            offline {\n              old_price\n              price\n           "
                     "   type\n              offline_discount\n              offline_promo\n            }\n           "
                     " levels {\n              count\n              price\n            }\n            discount\n      "
                     "    }\n        }\n      }\n    }\n  }",
            "variables": {
                "isShouldFetchOnlyProducts": True,
                "slug": "syry",
                "storeId": city_code,
                "sort": "default",
                "size": 1000,
                "from": 0,
                "in_stock": True,
                "eshop_order": None,
                "is_action": None,
                "price_levels": None
            }
        }

        if not self.cookie:
            self.cookie = "mindboxDeviceUUID=1a460ab8-1aab-47e4-90fb-955bba1c282d; fam_user=2 5; " \
                          "spid=1687240022619_929f189e8b8955241c0bfb02b1e33fe1_4wjpdn8bvgom4tgc; " \
                          "uxs_uid=e8b86e50-0f2d-11ee-b2f9-071d2c1e14de; _ym_visorc=b; _ym_d=1687240031; " \
                          "_ga_VHKD93V3FV=GS1.1.1687240033.1.0.1687240035.0.0.0; " \
                          "spsc=1687240035621_59b681aec19a1313e45555520fd78108_a5476469b72f558bb72e6aae99c6a060; " \
                          "flocktory-uuid=5d2fdf28-b1f6-4fa4-bbd9-ff16ec35312f-9; _ym_uid=1687240031134839430; " \
                          "tmr_lvid=f46767e3117bc29cd5973a800629b98f; tmr_lvidTS=1687240031058; " \
                          "_gcl_au=1.1.339806651.1687240027; " \
                          "directCrm-session=%7B%22deviceGuid%22%3A%221a460ab8-1aab-47e4-90fb-955bba1c282d%22%7D; " \
                          "popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C" \
                          "%7C1471519752605%3D1; _gid=GA1.2.849922522.1687240033; " \
                          "_slfreq=633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1687247227; " \
                          "_slsession=258E26C4-4F32-4919-92A0-4BA781D2B41B; metroStoreId=31; " \
                          "_slid=64913d5aacb6c75f640cf394; _ym_isad=2; exp_auth=3Rd5fv0vTUylyTasdzAcqA.1; " \
                          "_slfs=1687240025681; _ga=GA1.2.419238514.1687240033; is18Confirmed=false;"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,de;q=0.6',
            'Content-Type': 'application/json',
            'Referer': 'https://online.metro-cc.ru/',
            'Origin': 'https://online.metro-cc.ru',
            'Cookie': self.cookie,
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            products_list = []
            # Извлечение информации о продукте
            products = data['data']['category']['products']
            for product in products:
                # Извлечение необходимых данных о продукте
                product_id = product['id']
                product_name = product['name']
                product_url = product['url']
                product_price = product['stocks'][0]['prices']['price']
                product_promo = product['stocks'][0]['prices']['old_price']
                product_brand = product['manufacturer']['name']
                product = Product(product_id, product_name, product_url, product_price, product_promo, product_brand)
                products_list.append(product)
            return products_list
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
