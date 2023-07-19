import random


def deal():
    card = ['A', 'A', 'A', 'A', 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9,
            9, 9, 9, 10, 10, 10, 10, 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', ]  # 把所有牌用数字存在一起
    random.shuffle(card)  # 打乱数组
    print(card[0])
    del card[0]  # 发过的牌就不要了，避免总数超了
    print('你的到的牌是 %s' % card)
    return card[0]


def gameer(x):
    player = input = ('你是第几个玩家，按顺序输入数字')
    player.append(x)
    print('你有这些牌：%s' % player)


deal()
