import math
total = 0
count = 0
none_total = 0
white_total = 0
green_total = 0
blue_total = 0
none_per = 0
white_per = 0
green_per = 0
blue_per = 0
drop_count = 0
while True:
    count += 1
    print(str(count) + "回目")
    print("なし:0　白:1　緑:2　青:3")
    get = input("何出た？")
    get = int(get)
    if get == 0:
        none_total += 1
    elif get == 1:
        white_total += 1
        total += 1
        drop_count += 1
    elif get == 2:
        green_total += 1
        total += 3
        drop_count += 1
    elif get == 3:
        blue_total += 1
        total += 9
        drop_count += 1
    # 確率
    # none_per = none_total /count * 100
    if drop_count != 0:
        white_per = white_total / drop_count * 100
    if drop_count != 0:
        green_per = green_total / drop_count * 100
    if drop_count != 0:
        blue_per = blue_total / drop_count * 100 
    drop_per = drop_count / count * 100
    print("------------------------------------------")
    # print("無:" + str(none_total) + "  " + str(math.floor((none_per))) + "%")
    print("無:" + str(none_total))
    print("白:" + str(white_total) + "  " + str(math.floor(white_per)) + "%")
    print("緑:" + str(green_total) + "  " + str(math.floor(green_per)) + "%")
    print("青:" + str(blue_total) + "  " + str(math.floor(blue_per)) + "%")
    print("ドロップ率:" + str(math.floor(drop_per)) + "%")
    print("白換算:" + str(total))
    print("==========================================")