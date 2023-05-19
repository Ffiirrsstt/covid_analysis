# The file report_covid.csv is too large to upload.

def check(data,keys):
    _cases = list()
    _case = dict()
    for case in data:
        round = case.strip().split(',')
        for count in range(len(keys)):
            _case[keys[count]] = round[count]
        _cases.append(_case)
        _case = dict()
    return _cases

def time(start,mid,stop):
    start_check = start.split('/')
    mid_check = mid.split('/')
    stop_check = stop.split('/')
    if start_check[1]<=mid_check[1]==stop_check[1]: # 4 5 5
        if mid_check[0]<=stop_check[0]:
            answer = True
        else: answer = False
    elif start_check[1]==mid_check[1]<stop_check[1]: # 4 4 5
        if start_check[0]<=mid_check[0]:
            answer = True
        else: answer = False
    elif start_check[1]==mid_check[1]==stop_check[1]: # 5 5 5 and 4 4 4
        if start_check[0]<=mid_check[0]<=stop_check[0]:
            answer = True
        else: answer = False
    else: answer = False
    return answer

def count_people(case,start,stop,keys):
    if keys == 'count_day':
        people = 0
    elif keys == 'count_sex':
        people = [0]*3
    for count in case:
        true_or_false = time(start,count['announce_date'],stop)
        if keys == 'count_day':
            if true_or_false:
                people += 1
        elif keys == 'count_sex':
            if true_or_false:  
                if  count['sex'] == 'หญิง':
                    people[0] += 1
                elif  count['sex'] == 'ชาย':
                    people[1] += 1
                else:
                    people[2] += 1
            
    return people

with open('report_covid.csv',mode='r',encoding='utf-8-sig') as file:
    datacovid = file.readlines()

key = datacovid.pop(0).strip().split(',')
case = check(datacovid,key)
while True:
    print('\nสวัสดีค่ะ ยินดีให้บริการตอบคำถามเรื่องของ','\"รายงาน Covid-19 เริ่มต้นตั้งแต่วันที่ 12/4/2022 ถึง 1/5/2022 ค่ะ\"',sep='\n')
    print('\nกดหมายเลข 1 กรณีต้องการสอบถามจำนวนผู้ติดเชื้อ Covid-19 ทั้งหมด'
        ,'กดหมายเลข 2 กรณีต้องการสอบถามจำนวนผู้ติดเชื้อ Covid-19 ภายในช่วงระยะเวลาต่าง ๆ'
        ,'กดหมายเลข 3 กรณีต้องการทราบสถิติการติดเชื้อในเพศต่าง ๆ'
        ,'กดหมายเลข 0 กรณีไม่ต้องการสอบถามข้อมูลใด ๆ เพิ่มเติม',sep='\n') 
    question = input('กรุณากดหัวข้อที่คุณต้องการสอบถาม [ระบุเพียงหมายเลขเท่านั้น] : ')
    if question == '1':
        people = count_people(case,'12/4/2022','1/5/2022','count_day')
        print(f'\nมีผู้ติดเชื้อ covid-19 ตั้งแต่วันที่ 12/4/2022 ถึงวันที่ 1/5/2022 ทั้งหมดจำนวน {people} คนค่ะ')
    
    elif question == '2':
        start = input('คุณต้องการทราบจำนวนผู้ติดเชื้อ Covid-19 เริ่มต้นตั้งแต่วันที่เท่าใด [ตัวอย่าง 12/4/2022] : ')
        stop = input('คุณต้องการทราบจำนวนผู้ติดเชื้อ Covid-19 ถึงวันที่เท่าใด [ตัวอย่าง 1/5/2022] : ')
        people = count_people(case,start,stop,'count_day')
        if people != 0: 
            print(f'\nมีผู้ติดเชื้อ covid-19 ตั้งแต่วันที่ {start} ถึงวันที่ {stop} ทั้งหมดจำนวน {people} คนค่ะ')
        else: 
            print('\nรายงาน Covid-19 นี้ มีเพียงข้อมูลของตั้งแต่วันที่ 12/4/2022 ถึงวันที่ 1/5/2022 เท่านั้นค่ะ'
            ,'กรุณาสอบถามข้อมูลภายในช่วงวันที่ดังกล่าวและระบุข้อมูลในรูปแบบ วันที่/เดือน/ปีค.ศ. [เช่น 12/4/2022] เท่านั้นค่ะ',sep='\n')
    
    elif question == '3':
        print('คุณต้องการทราบสถิติการติดเชื้อในเพศต่าง ๆ เป็นช่วงระยะวันที่ หรือ ต้องการทราบเป็นสถิติทั้งหมด(ตั้งแต่วันที่ 12/4/2022 ถึงวันที่ 1/5/2022)'
        ,'[หมายเหตุ : ระบุคำตอบเป็นคำว่า "ช่วงระยะเวลา" หรือ "ทั้งหมด" เท่านั้น]',sep='\n')
        answer = input(': ')

        if answer == 'ทั้งหมด':
            people = count_people(case,'12/4/2022','1/5/2022','count_sex')
            print('\n\n\nมีผู้ติดเชื้อ covid-19 ตั้งแต่วันที่ 12/4/2022 ถึงวันที่ 1/5/2022'
            ,f'เพศหญิงทั้งหมดจำนวน {people[0]} คน'
            ,f'เพศชายทั้งหมดจำนวน {people[1]} คน'
            ,f'ไม่มีระบุเพศภายในรายงานทั้งหมดจำนวน {people[2]} คน',sep='\n')
        
        elif answer == 'ช่วงระยะเวลา':
            start = input('คุณต้องการทราบจำนวนผู้ติดเชื้อ Covid-19 เริ่มต้นตั้งแต่วันที่เท่าใด [ตัวอย่าง 12/4/2022] : ')
            stop = input('คุณต้องการทราบจำนวนผู้ติดเชื้อ Covid-19 ถึงวันที่เท่าใด [ตัวอย่าง 1/5/2022] : ')
            people = count_people(case,start,stop,'count_sex')
            print(f'\n\n\nมีผู้ติดเชื้อ covid-19 ตั้งแต่วันที่ {start} ถึงวันที่ {stop}'
            ,f'เพศหญิงทั้งหมดจำนวน {people[0]} คน'
            ,f'เพศชายทั้งหมดจำนวน {people[1]} คน'
            ,f'ไม่มีระบุเพศภายในรายงานทั้งหมดจำนวน {people[2]} คน',sep='\n')                    
        
        else:
            print('\n\nกรุณาพิมพ์คำตอบเป็น "ช่วงระยะเวลา" หรือ "ทั้งหมด" เท่านั้น\n\n')
            
    elif question == '0':
        break
    
    else:
        print('\n\nกรุณากดหมายเลขที่คุณประสงค์จะสอบถามใหม่อีกครั้งค่ะ [กรุณากดเพียงหมายเลขเท่านั้น]\n\n')
 
print('ขอบคุณที่ใช้บริการสอบถามกับทางเราค่ะ หวังอย่างยิ่งว่าคุณจะกลับมาใช้บริการใหม่อีกครั้งค่ะ')