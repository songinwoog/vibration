#진동측정값 읽어 오기
import os
import sys

#엑셀 저장 임포트


#모드버스 호출 임포트
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import *
from pymodbus.payload import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadDecoder
from datetime import datetime
import time

#호기 배열 생성
line_list = ['V151 수평존 RC팬','V151 수직상 RC팬'
             ]


now = datetime.now()
os.system("cls")
client = ModbusTcpClient('172.16.3.158',502)

client.connect
#   time.sleep(0.3)
print('진동센서 관리서버 연결중...')
#배열 초기화
result = client.read_holding_registers(0,25)
first_result = result
while True:    
        result = client.read_holding_registers(0,25)
        arr_result = result.registers

#print(arr_result)      

        if(arr_result.index(1)!=24):
                if(first_result != arr_result):
                    first_result = arr_result

                #print(arr_result.index(1))
                    print(arr_result , now.strftime('%Y-%m-%d %H:%M:%S'))

        else:
               first_result = arr_result

        # for n in range(0,24):
        #     if(arr_result[n]==1):
        #         print ('True 발생 : '+str(n))
        #         sys.exit()
time.sleep(0.2)
        #print('True 발견 : ${n}')
# for i in range(0,17):
#     print(result.bits)
    
#result1 = client.read_holding_registers(0,4)

#print(result1(0))
#decode = BinaryPayloadDecoder.fromRegisters(result1.registers,Endian.BIG)
#value = str(round(decode.decode_32bit_float(),1))
#print (value)
#print(result.registers)