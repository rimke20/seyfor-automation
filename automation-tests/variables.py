minimax_url = 'https://moj.minimax.si/'
user = 'klemendrobnic23@gmail.com'
password = 'Minimax'
company_name = 'Test'
company_address = 'Test22'
postal_code = '1000'
id_number = '123213231232'
items_type = "Storitve"
items_ddv = "Splošna stopnja"
item_one_name = "Ura programiranja"
item_one_price = "80"
item_two_name = "Ura svetovanja"
item_two_price = "100"
item_three_name = "Uvodna ura"
item_three_price = "40"
sum = float(item_one_price) + float(item_two_price) + float(item_three_price)
total_price_str = f"{sum:.2f}"
formatted_total_price = total_price_str.replace(".", ",") + ' EUR'
formatted_total_price_no_eur = total_price_str.replace(".", ",")
item_names = [item_one_name, item_two_name, item_three_name]
new_items = [
    (item_one_name, items_type, items_ddv, item_one_price),
    (item_two_name, items_type, items_ddv, item_two_price),
    (item_three_name, items_type, items_ddv, item_three_price)
]
