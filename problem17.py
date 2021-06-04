def spell_number(n):
    word = ''
    dict_words = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5':'five', '6': 'six', '7':'seven', '8': 'eight', '9':'nine'}
    dict_teens = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    dict_tens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
    x = str(n)
    if len(x) == 4:
        word = dict_words[x[0]] + 'thousand'
        return 'onethousand'
    if len(x) >= 3:
        word += dict_words[x[-3]] + 'hundred'
    if len(x) == 1:
        return dict_words[x]
    elif len(x) == 2:
        if x[-2:] == '00':
            return word
        elif x[-2:] == '10':
            word += 'ten'
            return word
        elif x[-2] == '1':
            word += '' + dict_teens[x[-2:]]
            return word
        elif x[-2] == '0':
            word += '' + dict_words[x[-1]]
            return word
        elif x[-1] == '0':
            word += '' + dict_tens[x[-2]]
            return word
        else:
            word += '' + dict_tens[x[-2]] + dict_words[x[-1]]
            return word


    if x[-2:] == '00':
        return word
    elif x[-2:] == '10':
        word += 'andten'
        return word
    elif x[-2] == '1':
        word += 'and' + dict_teens[x[-2:]]
        return word
    elif x[-2] == '0':
        word += 'and' + dict_words[x[-1]]
        return word
    elif x[-1] == '0':
        word += 'and' + dict_tens[x[-2]]
        return word
    else:
        word += 'and' + dict_tens[x[-2]] + dict_words[x[-1]]
        return word


sum = 0
for i in range(1, 1001):
    print(i, spell_number(i))
    sum += len(spell_number(i))
print(sum)
