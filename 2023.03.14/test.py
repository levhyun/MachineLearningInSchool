# 주문
save = []
menu = {'1':['짜장면',5000], '2':['짬뽕',6000], '3':['군만두',8000], '4':['탕수육',10000]}
maxCounter = 3
cnt = 1

def list():
    print('1.짜장면 - 5,000원          2.짬뽕 - 6,000원\n3.군만두 - 8,000원          4.탕수육 - 10,000원\n')

def result(name, quantity, price):
    res = f'주문하신 메뉴는 {name}이고 주문 수량은 {quantity} 그릇이며 주문금액은 {price*quantity} 원 입니다'
    save.append(f'[1]{res}')
    print(f'\n{res}\n')

def set(number):
    return menu[number][0], menu[number][1]

def loop():
    while True:
        add = input('3.추가 주문을 하시겠습니까? (Y / N) :')
        if add == 'Y' or add == 'y':
            return 1
        elif add == 'N' or add == 'n':
            return 0
        else:
            pass

def check():
    select = loop()
    if select == 0:
        print('[주문현황]')
        for str in save:
            print(str)
        return -1
    elif select == 1:
        if maxCounter == cnt:
            print('더이상 추가 주문을 할 수 없습니다!')
            return 0
        else:
            print('추가주문\n')
            return 1

while True:
    list()

    number = input('1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요:  ')
    quantity = int(input('2. 위 메뉴의 주문 수량을 쓰세요: '))
    name, price = set(number)

    result(name, quantity, price)

    while True:
        chk = check()
        if chk == -1:
            exit(1)
        elif chk == 1:
            cnt += 1
            break
        elif chk == 0:
            pass