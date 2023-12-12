import re
import math

input_str = input()

ans = 0
right_ans = 0
left_ans = 0
ans_1 = ''
ans_1_add = ''
array = []
minus_array = []
left_array = []
right_array = []
sostav1 = []
sostav2 = []
left_part = []
right_part = []
step_left_array = []
step_right_array = []
sin_left_array = []
sin_right_array = []
sin_array = []
cos_left_array = []
cos_right_array = []
cos_array = []
rez_array = []
upper_array = []
lower_array = []
numbers = {}
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
sin_ans_rez_1 = ''
sin_ans_rez_2 = ''
cos_ans_rez_1 = ''
cos_ans_rez_2 = ''
ans_rez_1 = ''
ans_rez_2 = ''
ans_total = ''
rez_ans = ''


numbers['плюс'], numbers['минус'], numbers['умножить'] = 0, 0, 1
numbers['ноль'],numbers['0'] = 0, 'ноль'
numbers['и'] = ','
numbers['пи'] = math.pi
numbers['один'],numbers['1'] = 1, 'один'
numbers['два'], numbers['2'] = 2, 'два'
numbers['одна'],numbers['1'] = 1, 'одна'
numbers['две'], numbers['2'] = 2, 'две'
numbers['три'], numbers['3'] = 3, 'три'
numbers['четыре'], numbers['4'] = 4, 'четыре'
numbers['пять'], numbers['5'] = 5, 'пять'
numbers['шесть'], numbers['6'] = 6, 'шесть'
numbers['семь'], numbers['7'] = 7, 'семь'
numbers['восемь'], numbers['8'] = 8, 'восемь'
numbers['девять'], numbers['9'] = 9, 'девять'
numbers['десять'], numbers['10'] = 10, 'десять'
numbers['одиннадцать'], numbers['11'] = 11, 'одиннадцать'
numbers['двенадцать'], numbers['12'] = 12, 'двенадцать'
numbers['тринадцать'], numbers['13'] = 13, 'тринадцать'
numbers['четырнадцать'], numbers['14'] = 14, 'четырнадцать'
numbers['пятнадцать'], numbers['15'] = 15, 'пятнадцать'
numbers['шестнадцать'], numbers['16'] = 16, 'шестнадцать'
numbers['семнадцать'], numbers['17'] = 17, 'семнадцать'
numbers['восемнадцать'], numbers['18'] = 18, 'восемнадцать'
numbers['девятнадцать'], numbers['19'] = 19, 'девятнадцать'
numbers['двадцать'], numbers['20'] = 20, 'двадцать'
numbers['тридцать'], numbers['30'] = 30, 'тридцать'
numbers['сорок'], numbers['40'] = 40, 'сорок'
numbers['пятьдесят'], numbers['50'] = 50, 'пятьдесят'
numbers['шестьдесят'], numbers['60'] = 60, 'шестьдесят'
numbers['семьдесят'], numbers['70'] = 70, 'семьдесят'
numbers['восемьдесят'], numbers['80'] = 80, 'восемьдесят'
numbers['девяносто'], numbers['90'] = 90, 'девяносто'
numbers['сто'], numbers['100'] = 100, 'сто'
numbers['двести'], numbers['200'] = 200, 'двести'
numbers['триста'], numbers['300'] = 300, 'триста'
numbers['четыреста'], numbers['400'] = 400, 'четыреста'
numbers['пятьсот'], numbers['500'] = 500, 'пятьсот'
numbers['шестьсот'], numbers['600'] = 600, 'шестьсот'
numbers['семьсот'], numbers['700'] = 700, 'семьсот'
numbers['восемьсот'], numbers['800'] = 800, 'восемьсот'
numbers['девятьсот'], numbers['900'] = 900, 'девятьсот'

operands=re.findall(r'\b\w+\b',input_str)

if 'плюс' in operands: #done
    for i in range(len(operands)):
        if numbers[operands[i]]:
            ans += numbers[operands[i]]
    
    if 0 <= ans <= 19:
        print(numbers[str(ans)])
    elif ans > 19 and ans%100 == 0:
        print(numbers[str(ans)])
    else:
        for i in range(len(str(ans))):
            array.append(int(str(ans)[i]) * (10 ** (len(str(ans))-i-1)))
        if array[-1] == 0:
            array = array[:-1]
        if array[-2] == 0:
            array = array[0:-2] + array[-1:]
        for el in array:
            ans_1 += numbers[str(el)] + ' '
        print(ans_1)

if 'умножить' in operands and 'синус' not in operands and 'косинус' not in operands and 'тангенс' not in operands: #done
    l1 = operands.index('умножить')
    r1 = operands.index('на')
    left_array = operands[:l1]
    right_array= operands[r1+1:]
    for i in range(len(left_array)):
        if left_array[i] in numbers:
            left_ans+=numbers[left_array[i]]
    for i in range(len(right_array)):
        if right_array[i] in numbers:
            right_ans+=numbers[right_array[i]]
    total_ans_mul = left_ans * right_ans
        
    if 0 <= total_ans_mul <= 19:
        print(numbers[str(total_ans_mul)])
    elif total_ans_mul > 19 and total_ans_mul%10 == 0:
        print(numbers[str(total_ans_mul)])
    elif len(str(total_ans_mul)) == 2:
        for i in range(len(str(total_ans_mul))):
            array.append(int(str(total_ans_mul)[i]) * (10 ** (len(str(total_ans_mul))-i-1)))
        for el in array:
            ans_1_add += numbers[str(el)] + ' '
        print(ans_1_add)
    elif len(str(total_ans_mul)) == 3:
        for i in range(len(str(total_ans_mul))):
            array.append(int(str(total_ans_mul)[i]) * (10 ** (len(str(total_ans_mul))-i-1)))
        for el in array:
            ans_1_add += numbers[str(el)] + ' '
        print(ans_1_add)

if 'минус' in operands: #done
    for i in range(len(operands)):
        if numbers[operands[i]]:
            if str(numbers[operands[i]]).isdigit():
                minus_array.append(numbers[operands[i]])
            ans = minus_array[0] - minus_array[-1]

    if 0 <= ans <= 19:
        print(numbers[str(ans)])
    elif ans > 19 and ans%10 == 0:
        print(numbers[str(ans)])
    else:
        for i in range(len(str(ans))):
            array.append(int(str(ans)[i]) * (10 ** (len(str(ans))-i-1)))
        for el in array:
            ans_1 += numbers[str(el)] + ' '
        print(ans_1)


    #print(41.31/17, 13.45/7, 11/10)
    for i in range(0,operands.index('делить')):
        if operands[i] in numbers:
            left_part.append(numbers[operands[i]])
    for i in range(operands.index('делить')+1,len(operands)):
        if operands[i] in numbers:
            right_part.append(numbers[operands[i]])

    if ',' in left_part:
        num_1 = sum(left_part[:left_part.index(',')])
        num_2 = sum(left_part[left_part.index(',')+1:])
        if len(str(num_2)) == 2:
            num_2 = num_2 / 100
        if len(str(num_2)) == 1:
            num_2 = num_2 / 10
        ans_del_1 = num_1 + num_2
    else:
        ans_del_1 = sum(left_part)

    if ',' in right_part:
        num_3 = sum(right_part[:right_part.index(',')])
        num_4 = sum(right_part[right_part.index(',')+1:])
        if len(str(num_4)) == 2:
            num_4 = num_4 / 100
        if len(str(num_4)) == 1:
            num_4 = num_4 / 10
        ans_del_2 = num_3 + num_4
    else:
        ans_del_2 = sum(right_part)

    rez = round(ans_del_1/ans_del_2,3)

    if '.' in str(rez):
        left_rez, right_rez = str(rez).split('.')
        left_rez = int(left_rez)
        right_rez = int(right_rez)
        if 0 <= left_rez <= 19:
            total = numbers[str(left_rez)]
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        elif left_rez > 19 and left_rez%10 == 0:
            total = numbers[str(left_rez)]
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        else:
            for i in range(len(str(left_rez))):
                array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
            for el in array:
                ans_rez_1 += numbers[str(el)] + ' '
            total = ans_rez_1
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        
        if 0 <= right_rez <= 19:
            total_2 = numbers[str(right_rez)]
        elif right_rez > 19 and right_rez%10 == 0:
            total_2 = numbers[str(right_rez)]
        else:
            for i in range(len(str(right_rez))):
                array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
            for el in array:
                ans_rez_2 += numbers[str(el)] + ' '
            total_2 = ans_rez_2
    if total_2.count(' ') == 0 and ('одна' in total_2):
        ans = total + ' и ' + total_2 + ' десятая'
    elif total_2.count(' ') == 0 and ('одна' not in total_2):
        ans = total + ' и ' + total_2 + ' десятых'

    if total_2.count(' ') == 2 and ('одна' in total_2):
        ans = total + ' и ' + total_2 + 'сотая'
    elif total_2.count(' ') == 0 and ('одна' not in total_2):
        ans = total + ' и ' + total_2 + 'сотых'

    if total_2.count(' ') == 3 and ('одна' in total_2):
        ans = total + ' и ' + total_2 + 'тысячная'
    elif total_2.count(' ') == 0 and ('одна' not in total_2):
        ans = total + ' и ' + total_2 + 'тысячных'
    print(ans)

if 'степени' in operands: #done
    #2**4 23**2
    step_left_part = operands[:operands.index('в')]
    step_right_part = operands[operands.index('степени')+1:]

    for i in range(len(step_left_part)):
        step_left_array.append(numbers[step_left_part[i]])
    step_left_rez = sum(step_left_array)

    for i in range(len(step_right_part)):
        step_right_array.append(numbers[step_right_part[i]])
    step_right_rez = sum(step_right_array)
    
    step_rez = step_left_rez ** step_right_rez

    if 0 <= step_rez <= 19:
        print(numbers[str(step_rez)])
    elif step_rez > 19 and step_rez%10 == 0:
        print(numbers[str(step_rez)])
    else:
        for i in range(len(str(step_rez))):
            array.append(int(str(step_rez)[i]) * (10 ** (len(str(step_rez))-i-1)))
        for el in array:
            ans_1 += numbers[str(el)] + ' '
        print(ans_1)
    
if 'делить' in operands and 'синус' not in operands and 'косинус' not in operands and 'тангенс' not in operands: #done
    #print(41.31/17, 41.31/5.28, 11/10, 41/17.28)
    for i in range(0,operands.index('делить')):
        if operands[i] in numbers:
            left_part.append(numbers[operands[i]])
    for i in range(operands.index('делить')+1,len(operands)):
        if operands[i] in numbers:
            right_part.append(numbers[operands[i]])

    if ',' in left_part:
        num_1 = sum(left_part[:left_part.index(',')])
        num_2 = sum(left_part[left_part.index(',')+1:])
        if len(str(num_2)) == 2:
            num_2 = num_2 / 100
        if len(str(num_2)) == 1:
            num_2 = num_2 / 10
        ans_del_1 = num_1 + num_2
    else:
        ans_del_1 = sum(left_part)

    if ',' in right_part:
        num_3 = sum(right_part[:right_part.index(',')])
        num_4 = sum(right_part[right_part.index(',')+1:])
        if len(str(num_4)) == 2:
            num_4 = num_4 / 100
        if len(str(num_4)) == 1:
            num_4 = num_4 / 10
        ans_del_2 = num_3 + num_4
    else:
        ans_del_2 = sum(right_part)

    rez = round(ans_del_1/ans_del_2,3)

    if '.' in str(rez):
        left_rez, right_rez = str(rez).split('.')
        left_rez = int(left_rez)
        right_rez = int(right_rez)
        
        if 0 <= left_rez <= 19:
            total = numbers[str(left_rez)]
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        elif left_rez > 19 and left_rez%10 == 0:
            total = numbers[str(left_rez)]
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        else:
            for i in range(len(str(left_rez))):
                array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
            for el in array:
                ans_rez_1 += numbers[str(el)] + ' '
            total = ans_rez_1
            if total == 'две':
                total = 'два'
            if total == 'одна':
                total = 'один'
        
        if 0 <= right_rez <= 19:
            total_2 = numbers[str(right_rez)]
        elif right_rez > 19 and right_rez%10 == 0:
            total_2 = numbers[str(right_rez)]
        else:
            for i in range(len(str(right_rez))):
                array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
            for el in array:
                ans_rez_2 += numbers[str(el)] + ' '
            total_2 = ans_rez_2

    if total_2.count(' ') == 0 and ('одна' in total_2):
        ans_total = total + ' и ' + total_2 + ' десятая'
    elif total_2.count(' ') == 0:
        ans_total =  total + ' и ' + total_2 + ' десятых'
    elif total_2.count(' ') == 2 and ('одна' in total_2):
        ans_total =  total + ' и ' + total_2 + 'сотая'
    elif total_2.count(' ') == 2:
        ans_total = total + ' и ' + total_2 + 'сотых'

    elif total_2.count(' ') == 3 and ('одна' in total_2):
        ans_total = total + ' и ' + total_2 + 'тысячная'
    elif total_2.count(' ') == 3:
        ans_total = total + ' и ' + total_2 + 'тысячных'
    
    print(ans_total)

if 'синус' in operands: #done
    if 'делить' in operands:#синус от пи делить на четыре
        left_part = operands[operands.index('от')+1:operands.index('делить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.sin(total_left/total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2

            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]

            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)
    
    if 'умножить' in operands:#синус от двадцать пять умножить на двадцать девять
        left_part = operands[operands.index('от')+1:operands.index('умножить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.sin(total_left * total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2

            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]

            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)

if 'косинус' in operands: #done
    if 'делить' in operands:#косинус от пятнадцать делить на двадцать три
        left_part = operands[operands.index('от')+1:operands.index('делить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.cos(total_left/total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2
            
            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]
            
            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)

    if 'умножить' in operands:#косинус от пятнадцать умножить на три
        left_part = operands[operands.index('от')+1:operands.index('умножить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.cos(total_left * total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2

            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]

            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)

if 'тангенс' in operands: #done
    if 'делить' in operands:#тангенс от пятнадцать делить на двадцать три
        left_part = operands[operands.index('от')+1:operands.index('делить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.tan(total_left/total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2
            
            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]
            
            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)

    if 'умножить' in operands:#тангенс от пятнадцать умножить на тридцать
        left_part = operands[operands.index('от')+1:operands.index('умножить')]
        right_part = operands[operands.index('на')+1:]

        for i in range(len(left_part)):
            left_array.append(numbers[left_part[i]])
        total_left = sum(left_array)

        for i in range(len(right_part)):
            right_array.append(numbers[right_part[i]])
        total_right = sum(right_array)

        rez = round(math.tan(total_left * total_right),3)

        if '.' in str(rez):
            left_rez, right_rez = str(rez).split('.')
            left_rez = int(left_rez)
            right_rez = int(right_rez)
            
            if 0 <= left_rez <= 19:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'

            elif left_rez > 19 and left_rez%10 == 0:
                total = numbers[str(left_rez)]
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            else:
                for i in range(len(str(left_rez))):
                    array.append(int(str(left_rez)[i]) * (10 ** (len(str(left_rez))-i-1)))
                for el in array:
                    ans_rez_1 += numbers[str(el)] + ' '
                total = ans_rez_1
                if total == 'две':
                    total = 'два'
                if total == 'одна':
                    total = 'один'
            
            if 0 <= right_rez <= 19:
                total_2 = numbers[str(right_rez)]
            
            elif right_rez > 19 and right_rez%10 == 0:
                total_2 = numbers[str(right_rez)]
            
            else:
                for i in range(len(str(right_rez))):
                    array.append(int(str(right_rez)[i]) * (10 ** (len(str(right_rez))-i-1)))
                for el in array:
                    ans_rez_2 += numbers[str(el)] + ' '
                total_2 = ans_rez_2

            if 'ноль' in total_2:
                total_2 = total_2[:total_2.index('ноль')] + total_2[total_2.index('ноль')+4:]

            if total_2.count(' ') == 0 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + ' десятая'
            
            elif total_2.count(' ') == 0:
                ans_total =  total + ' и ' + total_2 + ' десятых'
            
            elif total_2.count(' ') == 2 and ('одна' in total_2):
                ans_total =  total + ' и ' + total_2 + 'сотая'
            
            elif total_2.count(' ') == 2:
                ans_total = total + ' и ' + total_2 + 'сотых'
            
            elif total_2.count(' ') == 3 and ('одна' in total_2):
                ans_total = total + ' и ' + total_2 + 'тысячная'
            
            elif total_2.count(' ') == 3:
                ans_total = total + ' и ' + total_2 + 'тысячных'
            
            print(ans_total)

if 'перестановка' in operands: #перестановка с числом шесть
    part = operands[operands.index('числом')+1:]
    for i in range(len(part)):
            array.append(numbers[part[i]])
    total= sum(array)
    rez = math.factorial(total)

    if 0 <= rez <= 19:
        print(numbers[str(rez)])
    elif rez > 19 and rez%100 == 0:
        print(numbers[str(rez)])
    else:
        for i in range(len(str(rez))):
            rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez))-i-1)))
        if rez_array[-1] == 0:
            rez_array = rez_array[:-1]
        if rez_array[-2] == 0:
            rez_array = rez_array[:-2] + rez_array[-1:]
        for el in rez_array:
            rez_ans += numbers[str(el)] + ' '
        print(rez_ans)

if 'размещений' in operands:#размещений из три по два
    upper_part = operands[operands.index('из')+1:operands.index('по')]
    lower_part = operands[operands.index('по')+1:]

    for i in range(len(upper_part)):
        upper_array.append(numbers[upper_part[i]])
    total_upper = sum(upper_array)

    for i in range(len(lower_part)):
        lower_array.append(numbers[lower_part[i]])
    total_lower = sum(lower_array)
    rez = round((math.factorial(total_upper)) / (math.factorial(total_upper - total_lower)))

    if 0 <= rez <= 19:
        print(numbers[str(rez)])
    elif rez > 19 and rez%100 == 0:
        print(numbers[str(rez)])
    else:
        for i in range(len(str(rez))):
            rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez))-i-1)))
        if rez_array[-1] == 0:
            rez_array = rez_array[:-1]
        if rez_array[-2] == 0:
            rez_array = rez_array[:-2] + rez_array[-1:]
        for el in rez_array:
            rez_ans += numbers[str(el)] + ' '
        print(rez_ans)

if 'сочетаний' in operands:#сочетаний из три по пять
    upper_part = operands[operands.index('из')+1:operands.index('по')]
    lower_part = operands[operands.index('по')+1:]

    for i in range(len(upper_part)):
        upper_array.append(numbers[upper_part[i]])
    total_upper = sum(upper_array)

    for i in range(len(lower_part)):
        lower_array.append(numbers[lower_part[i]])
    total_lower = sum(lower_array)
    rez = round((math.factorial(total_lower)) / ((math.factorial(total_lower - total_upper)) * (math.factorial(total_upper))))

    if 0 <= rez <= 19:
        print(numbers[str(rez)])
    elif rez > 19 and rez%100 == 0:
        print(numbers[str(rez)])
    else:
        for i in range(len(str(rez))):
            rez_array.append(int(str(rez)[i]) * (10 ** (len(str(rez))-i-1)))
        if rez_array[-1] == 0:
            rez_array = rez_array[:-1]
        if rez_array[-2] == 0:
            rez_array = rez_array[:-2] + rez_array[-1:]
        for el in rez_array:
            rez_ans += numbers[str(el)] + ' '
        print(rez_ans)
