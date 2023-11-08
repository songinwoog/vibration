import os
import socket
import pandas as pd


host = "127.0.0.1"
port = 502

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 host와 prot를 통해 서버에 접속합니다.
try:
 accept = client_socket.connect((host, port))
 print ('서버 연결 성공')
 pass
except:
 print ("접속 거부")

#os.system('cls')
def menu():
  print ("------------------------------------------------")
  print ("경보설비 컨트롤러 앱 ")
  print ("1. 모니터링 시작")
  print ("2. 알람발생시 엑셀 저장")
  print ("3. 알람발생시 카톡메시지 보내기")
  print ("4. 종료")
  print("선택하여 주세요 : ",end='')
  choise = input()



menu()
