# task 5

price_list = [57.8, 46.51, 97, 73, 11, 72, 98.1, 73.4, 96, 68, 40, 133, 145, 155, 120, 200.5, 500.2, 23, 19, 20.5]
price_list.sort()
new_string = ''
max_5_elem = ''
for i in range(len(price_list)):
    rub = float(price_list[i])
    kop = round(rub * 100)
    rub, kop = divmod(kop, 100)
    new_string += '%d руб %02d коп ' % (rub, kop)
for v in price_list[-5:]:
    rub = float(v)
    kop = round(rub * 100)
    rub, kop = divmod(kop, 100)
    max_5_elem += '%d руб %02d коп ' % (rub, kop)
reversed_price_list = price_list[::-1]
print(reversed_price_list)
print(new_string)
print(max_5_elem)