
for a in range(0, 1000, 17):
    numbers = '0123456789'
    string_number = str(a)
    print(string_number)

    for c in range(10):
        if str(c) in string_number:
            continue
        elif int(str(c) + string_number[:-1]) % 13 != 0:
            continue
        else:
            string_number1 = str(c) + string_number
            print(string_number1)
            for d in range(10):
                if str(d) in string_number1:
                    continue
                elif int(str(d) + string_number1[:-2]) % 11 != 0:
                    continue
                else:
                    string_number2 = str(d) + string_number1

                    for e in range(10):
                        if str(e) in string_number2:
                            continue
                        elif int(str(e) + string_number2[:-3]) % 7 != 0:
                            continue
                        else:
                            string_number3 = str(e) + string_number2

                            for f in range(10):
                                if str(f) in string_number3:
                                    continue
                                elif int(str(f) + string_number3[:-4]) % 5 != 0:
                                    continue
                                else:
                                    string_number4 = str(d) + string_number3

                                    for g in range(10):
                                        if str(g) in string_number4:
                                            continue
                                        elif int(str(g) + string_number4[:-5]) % 3 != 0:
                                            continue
                                        else:
                                            string_number5 = str(g) + string_number4
                                            for h in range(10):
                                                if str(h) in string_number5:
                                                    continue
                                                elif int(str(h) + string_number5[:-6]) % 2 != 0:
                                                    continue
                                                else:
                                                    string_number6 = str(d) + string_number5
                                                    print(string_number6)
