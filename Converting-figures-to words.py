def reverse(String):
    S = ''
    c = 1
    for k in range(len(String)):
      S += String[k-c]
      c +=2
    return S


n = '745907780040750'#700050000000'
dic = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven',
'8':'eight', '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14': 'fourteen',
'15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty',
'21':'twenty-one', '22':'twenty-two', '23':'twenty-three', '24':'twenty-four', '25':'twenty-five',
'26':'twenty-six', '27':'twenty-seven', '28':'twenty-eight', '29':'twenty-nine', '30':'thirty',
'31':'thirty-one', '32':'thirty-two', '33':'thirty-three', '34':'thirty-four', '35':'thirty-five',
'36':'thirty-six', '37':'thirty-seven', '38':'thirty-eight', '39':'thirty-nine', '40':'forty',
'41':'forty-one', '42':'forty-two', '43':'forty-three', '44':'forty-four', '45':'forty-five',
'46':'forty-six', '47':'forty-seven', '48':'forty-eight', '49':'forty-nine', '50':'fifty', '51':'fifty-one',
'52':'fifty-two', '53':'fifty-three', '54':'fifty-four', '55':'fifty-five','56':'fifty-six', '57':'fifty-seven',
'58':'fifty-eight', '59':'fifty-nine', '60':'sixty', '61':'sixty-one','62':'sixty-two', '63':'sixty-three',
'64':'sixty-four', '65':'sixty-five', '66':'sixty-six', '67':'sixty-seven', '68':'sixty-eight',
'69':'sixty-nine', '70':'seventy', '71':'seventy-one', '72':'seventy-two', '73':'seventy-three',
'74':'seventy-four', '75':'seventy-five', '76':'seventy-six', '77':'seventy-seven', '78':'seventy-eight',
'79':'seventy-nine', '80':'eighty', '81':'eighty-one', '82':'eighty-two', '83':'eighty-three',
'84':'eighty-four','85':'eighty-five', '86':'eighty-six', '87':'eighty-seven','88':'eighty-eight',
'89':'eighty-nine', '90':'ninety', '91':'ninety-one','92':'ninety-two','93':'ninety-three', '94':'ninety-four',
'95':'ninety-five','96':'ninety-six', '97':'ninety-seven','98':'ninety-eight', '99':'ninety-nine'}

def S_num2Wor(l):
    if l[0] == '0' and l[1] == '0' and l[2] == '0':
        return ''
    elif l[0] == '0' and l[1] != '0':
        return  dic[l[1] + l[2]]
    elif l[0] == '0' and l[1] == '0':
        return  dic[l[2]]
    if len(l) != 3:
        return dic[l]
    else:
        s = dic[l[0][0]] + ' hundred'
        if l[1] == '0' and l[2] != '0':
            return s + ' and ' + dic[l[2]]
        elif l[1] != '0':
            return s + ' and ' + dic[l[1] + l[2]]
    return s
    
def Fig2Words():
        """
        Note : This function does not take any argument
        This functions converts numbers in figures ranging from 1 - 999999999999999
        to words.
        It returns None. It prints out the value in words 
        """
        
        n = input('kindly enter a number you want to convert to  words: ')
        if len(n) == 1 and n[0] == '0':
             print(dic['0'])
        else:
               empty = ''
               for tsp in n:
                   if tsp != ' ':
                       empty +=tsp
               n = empty
               while not n.isdigit() or len(n) > 15:
                   if not n.isdigit():
                       print('Bad input! Your input must be in digits(0 - 9)')
                       n = input('kindly enter a number you want to convert to  words: ')
                   elif len(n) > 15:
                       print("Bad news! I am sorry I cant convert numbers that are more than '999999999999999' to words ")
                       n = input('kindly enter a number you want to convert to  words: ')
               l, s, c = [], '', 1
               for i in range(len(n)):
                   s +=n[i-c]
                   c = c + 2
                   if len(s) == 3:
                       l.append(reverse(s))
                       s = ''
               if s != '':
                    l.append(reverse(s))
               print('Step1: Rearrange the number')
               k = 1
               for m in range(len(l)):
                   print(l[m-k] + ' ', end = '')
                   k = k + 2
               print('')
               print('Step2: write the number in words')
               if len(l) == 1:
                   print(S_num2Wor(l[0]))
               elif len(l) == 2:
                   print(S_num2Wor(l[1]) + ' thousand ', end = '')
                   if (l[0][0] == '0' and (l[0][1] and l[0][2]) !='0') or (l[0][0] != '0' and l[0][1] == '0' and l[0][2] == '0'):
                       print(' and ' + S_num2Wor(l[0]))
                   else:
                       print(S_num2Wor(l[0]))
               elif len(l) == 3:
                   print(S_num2Wor(l[2]) + ' million ', end = '')
                   if l[1][0] == '0' and (l[1][1] or l[1][2]) !='0' and S_num2Wor(l[0]) == '' :
                       print(' and ' + S_num2Wor(l[1]) + ' thousand ', end = '')
                   elif S_num2Wor(l[1]) != '':
                       print(S_num2Wor(l[1]) + ' thousand ', end = '')
                   if (l[0][0] == '0' and (l[0][1] and l[0][2]) !='0') or (l[0][0] != '0' and l[0][1] == '0' and l[0][2] == '0'):
                       print(' and ' + S_num2Wor(l[0]))
                   else:
                       print(S_num2Wor(l[0]))
               elif len(l) == 4:
                  print(S_num2Wor(l[3]) + ' billion ', end = '')
                  if l[2][0] == '0' and (l[2][1] or l[2][2]) !='0' and S_num2Wor(l[1]) == '' and S_num2Wor(l[0]) == '':
                      print(' and ' + S_num2Wor(l[2]) + ' million ', end = '')
                  elif S_num2Wor(l[2]) != '':
                      print(S_num2Wor(l[2]) + ' million ', end = '')
                  if l[1][0] == '0' and (l[1][1] or l[1][2]) !='0' and S_num2Wor(l[0]) == '' :
                      print(' and ' + S_num2Wor(l[1]) + ' thousand ', end = '')
                  elif S_num2Wor(l[1]) != '':
                      print(S_num2Wor(l[1]) + ' thousand ', end = '')
                  if (l[0][0] == '0' and (l[0][1] and l[0][2]) !='0') or (l[0][0] != '0' and l[0][1] == '0' and l[0][2] == '0'):
                      print(' and ' + S_num2Wor(l[0]))
                  else:
                      if S_num2Wor(l[0]) != '':
                          print(S_num2Wor(l[0]))  
               elif len(l) == 5:
                 print(S_num2Wor(l[4]) + ' trillion ', end = '')
                 if l[3][0] == '0' and (l[3][1] or l[3][2]) !='0' and S_num2Wor(l[1]) == '' and S_num2Wor(l[0]) == '' and S_num2Wor(l[2]) == '':
                     print(' and ' + S_num2Wor(l[2]) + ' billion ', end = '')
                 elif S_num2Wor(l[3]) != '':
                    print(S_num2Wor(l[3]) + ' billion ', end = '')
                 if l[2][0] == '0' and (l[2][1] or l[2][2]) !='0' and S_num2Wor(l[1]) == '' and S_num2Wor(l[0]) == '':
                    print(' and ' + S_num2Wor(l[2]) + ' million ', end = '')
                 elif S_num2Wor(l[2]) != '':
                     print(S_num2Wor(l[2]) + ' million ', end = '')
                 if l[1][0] == '0' and (l[1][1] or l[1][2]) !='0' and S_num2Wor(l[0]) == '' :
                     print(' and ' + S_num2Wor(l[1]) + ' thousand ', end = '')
                 elif S_num2Wor(l[1]) != '':
                     print(S_num2Wor(l[1]) + ' thousand ', end = '')
                 if (l[0][0] == '0' and (l[0][1] and l[0][2]) !='0') or (l[0][0] != '0' and l[0][1] == '0' and l[0][2] == '0'):
                     print(' and ' + S_num2Wor(l[0]))
                 else:
                     if S_num2Wor(l[0]) != '':
                         print(S_num2Wor(l[0]))
