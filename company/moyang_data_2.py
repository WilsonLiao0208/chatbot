
#!/usr/bin/python3
import pyperclip
import csv
import struct
import binascii
file_path = "C:/Users/user/Desktop/python/test.bin"
with open(file_path, "rb") as file:
    src = file.read()

file.close()

# src_str = src.decode('utf-8', errors='ignore')  # 将二进制数据解码为字符串
src_hex = binascii.hexlify(src).decode('utf-8')  # 将二进制数据转换为十六进制字符串
formatted_str = ' '.join(src_hex[i:i+2].upper()
                         for i in range(0, len(src_hex), 2))  # 格式化为"AA BB CC DD"的形式

strs0 = formatted_str.split('AA BB CC DD')
strs = ""
str_time = ""
actWear = "TIMESTAMP\tTIMEZONE\tPPG1\tPPG2\tACC_X\tACC_Y\tACC_Z\tppgNumChannels\tppgLength\taccLength\taltitude\thrRef\tspeedRef\tstepCountOut\tkcalOut\tactiveTypeOut\tsleepStageOut\tsleepStageStatusOut\tsleepStagePpgOnOffOut\tsleepPeriodStartTSOut\tsleepPeriodEndTSOut\tsleepPeriodNumMinutesOut\tsleepPeriodStatusOut\tWEAR\tMONTION\n"


last_flag = 0
endSucceed = 1
# print("src= ", src)
# print("src_str= ", formatted_str)
for str1 in strs0:
    # print("str1= ", str1)
    acts2 = str1.split(' ')
    if (len(acts2) == 1):
        continue

    # print("acts2= ", acts2)
    flag = int(acts2[1], 16)
    # print("flag= ", flag)
    # print("len(acts2)", len(acts2))
    if (flag > 6):
        continue
    if (flag < 0):
        continue
    # print("abs(last_flag - flag):", abs(last_flag - flag))
    if abs(last_flag - flag) == 6:
        endSucceed = 1

    if (abs(last_flag - flag) != 1 and abs(last_flag - flag) != 6):
        if (endSucceed == 1):
            actWear += "\n"
            last_flag = 0
            # print("test-+--------------------")
            for i in range(abs(last_flag - flag)):
                actWear += "\t"

    last_flag = flag
    # print("flag= ", flag)
    if (flag == 0x00):
        if (len(acts2) != 9):
            actWear += "\t"
            continue
        num = int(acts2[2], 16) + (int(acts2[3], 16) << 8) + \
            (int(acts2[4], 16) << 16) + (int(acts2[5], 16) << 24)
        # print("num0= ", num)
        actWear += str(num) + "\t"
        num = int(acts2[6], 16) + (int(acts2[7], 16) << 8)
        # print("num1= ", num)
        actWear += str(num) + "\t"

    if (flag == 0x01 or flag == 0x02):
        MaxLen = len(acts2) - 3
        if (MaxLen == 0):
            actWear += "\t"
            continue
        MaxIndex = MaxLen / 4
        for i in range(int(MaxIndex)):
            num = int(acts2[2 + i * 4], 16) + (int(acts2[3 + i * 4], 16) << 8) + \
                (int(acts2[4 + i * 4], 16) << 16) + \
                (int(acts2[5 + i * 4], 16) << 24)
            num = struct.unpack('f', struct.pack('I', num))[0]
            actWear += str(num) + ','
        actWear += "\t"
    if (flag == 0x03 or flag == 0x04 or flag == 0x05):
        MaxLen = len(acts2) - 3
        if (MaxLen == 0):
            actWear += "\t"
            continue
        MaxIndex = MaxLen / 2
        for i in range(int(MaxIndex)):
            num = int(acts2[2 + i * 2], 16) + \
                (int(acts2[3 + i * 2], 16) << 8)
            if num & 0x8000:
                num -= 0x10000
            num = (num >> 4) * 3.904
            actWear += str(num) + ','
        actWear += "\t"
    if (flag == 0x06):
        if (len(acts2) < 43):
            actWear += "\t\n"
            continue

        num = int(acts2[2], 16)
        actWear += str(num) + "\t"

        num = int(acts2[3], 16)
        actWear += str(num) + "\t"

        num = int(acts2[4], 16)
        actWear += str(num) + "\t"

        num = int(acts2[5], 16) + (int(acts2[6], 16) << 8) + \
            (int(acts2[7], 16) << 16) + (int(acts2[8], 16) << 24)
        num = struct.unpack('f', struct.pack('I', num))[0]
        actWear += str(num) + "\t"

        num = int(acts2[9], 16) + (int(acts2[10], 16) << 8) + \
            (int(acts2[11], 16) << 16) + (int(acts2[12], 16) << 24)
        num = struct.unpack('f', struct.pack('I', num))[0]
        actWear += str(num) + "\t"

        num = int(acts2[13], 16) + (int(acts2[14], 16) << 8) + \
            (int(acts2[15], 16) << 16) + (int(acts2[16], 16) << 24)
        num = struct.unpack('f', struct.pack('I', num))[0]
        actWear += str(num) + "\t"

        num = int(acts2[17], 16) + (int(acts2[18], 16) << 8) + \
            (int(acts2[19], 16) << 16) + \
            (int(acts2[20], 16) << 24)
        num = struct.unpack('f', struct.pack('I', num))[0]
        actWear += str(num) + "\t"

        num = int(acts2[21], 16) + (int(acts2[22], 16) << 8) + \
            (int(acts2[23], 16) << 16) + \
            (int(acts2[24], 16) << 24)
        num = struct.unpack('f', struct.pack('I', num))[0]
        actWear += str(num) + "\t"

        num = int(acts2[25], 16)
        actWear += str(num) + "\t"

        num = int(acts2[26], 16)
        actWear += str(num) + "\t"

        num = int(acts2[27], 16)
        actWear += str(num) + "\t"

        num = int(acts2[28], 16)
        actWear += str(num) + "\t"

        num = int(acts2[29], 16) + (int(acts2[30], 16) << 8) + \
            (int(acts2[31], 16) << 16) + \
            (int(acts2[32], 16) << 24)
        actWear += str(num) + "\t"

        num = int(acts2[33], 16) + (int(acts2[34], 16) << 8) + \
            (int(acts2[35], 16) << 16) + \
            (int(acts2[36], 16) << 24)
        actWear += str(num) + "\t"

        num = int(acts2[37], 16) + (int(acts2[38], 16) << 8)
        actWear += str(num) + "\t"
        num = int(acts2[39], 16)
        actWear += str(num) + "\t"

        num = int(acts2[40], 16)
        actWear += str(num) + "\t"

        num = int(acts2[41], 16)
        actWear += str(num) + "\t\n"
        endSucceed = 2

with open('test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    rows = actWear.split('\n')
    for row in rows:
        data = row.split('\t')
        writer.writerow(data)














