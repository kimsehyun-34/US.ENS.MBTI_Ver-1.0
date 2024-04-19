import random
import time
import os
import pandas as pd
import keyboard
import pygame

pygame.mixer.init()
pygame.mixer.music.load("./Aperture.mp3")

for i in range(1,50):
	m="*"*i
	print(f"[{m}]")
	time.sleep(0.015)
	os.system('cls')

for i in range(1,5):
	print("[-]")
	time.sleep(0.08)
	os.system('cls')
	print("[\]")
	time.sleep(0.08)
	os.system('cls')
	print("[|]")
	time.sleep(0.08)
	os.system('cls')
	print("[/]")
	time.sleep(0.08)
	os.system('cls')

print("접속 완료")
time.sleep(0.3)
os.system('cls')

for i in range(1,31):
	m="[-]"
	if i==5:
		m="// NETWORK--------------------"
		print(m, end=' ')
		time.sleep(0.4)
		n="["'\033[32m'"OK"'\033[0m'"]"
		print(n)
	elif i==10:
		m="// DBMS-----------------------"
		print(m, end=' ')
		time.sleep(0.3)
		n="["'\033[32m'"OK"'\033[0m'"]"
		print(n)
	elif i==15:
		m="// APERTURE_BACKBONE----------"
		print(m, end=' ')
		time.sleep(0.4)
		n="["'\033[32m'"OK"'\033[0m'"]"
		print(n)
	elif i==15:
		m="// APERTURE_BACKBONE----------"
		print(m, end=' ')
		time.sleep(0.5)
		n="["'\033[32m'"OK"'\033[0m'"]"
		print(n)
	elif i==20:
		m="// RANDOM ---------------------"
		name_rank=random.randrange(1,101)
		print(m, end=' ')
		time.sleep(0.8)
		n="["'\033[32m'"OK"'\033[0m'"]"
		print(n)
	elif i==25:
		m="// T-60 ---------------------"
		print(m, end=' ')
		time.sleep(0.8)
		n="["'\033[31m'"FALL"'\033[0m'"]"
		print(n)
	elif i==30:
		m="// X-01 ---------------------"
		print(m, end=' ')
		time.sleep(0.9)
		n="["'\033[31m'"FALLOUT"'\033[0m'"]"
		print(n)
	else:
		print(m)
	time.sleep(0.13)
print(name_rank)
time.sleep(1)
pygame.mixer.music.play()
os.system('cls')

os.system('cls')
print('\033[96m')
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣴⣶⣶⣶⣦⣦⠀⡀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⢀⣴⣾⣷⣦⣈⠛⢿⣿⣿⣿⣿⡅⢸⣷⣦⡀⠀⠀")
print("⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣷⣤⠈⠛⢿⣿⣗⠈⣿⣿⣿⣦⡀⠀")
print("⠀⠀⢀⢾⠿⠿⠻⠛⠛⠉⠉⠈⠀⠀⠀⠀⠉⠻⠀⢿⣿⣿⣿⡷ ")
print("⠀⠀⣠⣤⣴⣴⣶⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⠀")
print("⠀⠠⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋")
print("⠀⠸⣿⣿⣿⠏⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠈⣿⣿⠃⣰⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠹⠁⣼⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⢺⣿⣿⣿⣿⠀⢷⣤⡀⠀⢀⢀⣠⣠⣤⣦⣶⣷⣷⣿⡟⠁⠀⠀")
print("⠀⠀⠀⠀⠛⣿⣿⣿⡅⢹⣿⣿⣷⣤⡙⠻⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠛⠿⣧⠨⣿⣿⣿⣿⣿⣶⣄⠙⠻⠿⠋⠁⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠛⠟⠟⠟⠛⠋⠋⠀⠀")

time.sleep(1.5)
os.system('cls')
print('')
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣴⣶⣶⣶⣦⣦⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⢀⣴⣾⣷⣦⣈⠛⢿⣿⣿⣿⣿⡅⢸⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣷⣤⠈⠛⢿⣿⣗⠈⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀         ⠀⠀⠀")
print("⠀⠀⢀⢾⠿⠿⠻⠛⠛⠉⠉⠈⠀⠀⠀⠀⠉⠻⠀⢿⣿⣿⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⣠⣤⣴⣴⣶⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠟⢀⣿⣿⣿⠀⠀⠀⠀⢰⣿⣿⢿⢿⣿⣶⡄⠀⠀⢼⣿⡿⡿⡿⡿⡿⠁⠀⠠⣿⣿⢿⢿⢿⣷⣦⠀⠀⢿⢿⢿⣿⣿⢿⢿⠇⠀⢸⣿⣟⠀⠀⢀⣿⣿⠁⠀⢀⣿⣿⢿⢿⢿⣿⣦⠀⠀⠀⣺⣿⡿⡿⡿⡿⡿⠁⠀⠀")
print("⠀⠠⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⢠⣿⡿⢻⣿⡂⠀⠀⠀⣼⣿⡇⠀⠀⣽⣿⡇⠀⢀⣿⣿⣅⣀⣀⣀⠀⠀⠀⢸⣿⡯⢀⢀⣸⣿⡿⠀⠀⠀⠀⣼⣿⡇⠀⠀⠀⠀⣽⣿⡇⠀⠀⣸⣿⡟⠀⠀⢰⣿⣟⢀⢀⣨⣿⡿⠀⠀⢀⣿⣿⣂⣀⣀⣀⠀⠀⠀  ⠀")
print("⠀⠸⣿⣿⣿⠏⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣀⣽⣿⡇⠀⠀⢀⣿⣿⢿⢿⢿⠿⠛⠀⠀⣸⣿⡿⠛⠟⠻⠛⠁⠀⠀⣿⣿⠿⠿⢿⣿⡭⠀⠀⠀⠀⠠⣿⣿⠁⠀⠀⠀⢐⣿⣿⠀⠀⠀⣾⣿⠃⠀⠀⣽⣿⡿⠿⢿⣿⣯⠁⠀⠀⢰⣿⡿⠛⠟⠟⠟⠀  ⠀⠀⠀")
print("⠀⠈⣿⣿⠃⣰⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡟⠛⠛⢛⣿⣯⠀⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠀⣾⣿⣇⣀⣀⣀⣀⠀⠀⢰⣿⣿⠀⠀⢨⣿⡿⠀⠀⠀⠀⢸⣿⡯⠀⠀⠀⠀⠸⣿⣷⣀⣀⣼⣿⡟⠀⠀⢠⣿⣿⠀⠀⢀⣿⣿⠀⠀⠀⣽⣿⣇⣀⣀⣀⣀⠀⠀   ⠀⠀")
print("⠀⠀⠹⠁⣼⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠀⡀⡀⠀⠛⠛⠀⠀⠙⠛⠃⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⠛⠛⠛⠋⠀⠀⠚⠛⠃⠀⠀⠈⠛⠛⠀⠀⠀⠀⠙⠛⠃⠀⠀⠀⠀⠀⠉⠛⠟⠟⠛⠑⠀⠀⠀⠘⠛⠋⠀⠀⠐⠛⠛⠀⠀⠐⠛⠛⠛⠛⠛⠛⠋⠀⠀⠀   ⠀")
print("⠀⠀⠀⢺⣿⣿⣿⣿⠀⢷⣤⡀⠀⢀⢀⣠⣠⣤⣦⣶⣷⣷⣿⡟⠁⠀⠀⢸⠀⠀⠀⠀⠀⠀⡎⡆⠀⠀⠀⢸⢘⢘⠄⠀⠀⢀⠎⠊⠲⡀⠀⠀⢸⢘⠘⣆⠀⠀⠀⢠⢣⡀⠀⠀⠘⢸⠊⠂⠀⠀⡰⠘⠘⢢⠀⠀⠀⡪⢊⢊⡆⠀⠀⢸⠀⠀⠀⢸⢘⢘⠀⠀⠀⡢⡃⠳⠀⠀⠀  ⠀")
print("⠀⠀⠀⠀⠛⣿⣿⣿⡅⢹⣿⣿⣷⣤⡙⠻⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⢸⣀⣀⠀⠀⠀⡎⠃⠳⡀⠀⠀⢸⣁⣑⠇⠀⠀⠘⢤⣀⣨⠂⠀⠀⢸⠈⠈⣇⠀⠀⢠⠇⠃⢧⠀⠀ ⢸⠀⠀⠀⠀⠪⣄⣀⠼⠀⠀⠀⡪⠁⠑⡆⠀⠀⢸⠀⠀⠀⢹⣈⣈⠀⠀⠀⢬⣈⡱⠅⠀ ⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠛⠿⣧⠨⣿⣿⣿⣿⣿⣶⣄⠙⠻⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠛⠟⠟⠟⠛⠋⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print('\033[0m')
time.sleep(4)
os.system('cls')

cun=1
v=['ISTP', 'ISFJ']
n=['ESFP', 'ENTJ', 'ESTP', 'ESTJ']
w=['ISFP', 'ESFJ']
t=['ESTJ', 'INTP']
c=['ENFP', 'ENFJ']
m=['INTJ', 'ISTJ']
o=['INFP', 'ENTP']

def selectOne(value = 1):
	os.system('cls')
	printOptions(value)
	while 1:
		if keyboard.is_pressed(72):
			value -= 1
			if value < 1:
				value = 2
			os.system('cls')
			printOptions(value)
			time.sleep(0.1)

		if keyboard.is_pressed(80):
			value += 1
			if value > 2:
				value = 1
			os.system('cls')
			printOptions(value)
			time.sleep(0.1)

		if keyboard.is_pressed('enter'):
			return value
		time.sleep(0.1)

def printOptions(selected):
    print('성별을 선택해 주세요!')
    if selected == 1:
        printWithBg("남자", "black", "bg_white")
    else:
        printWithBg("남자", "white", "bg_black")

    if selected == 2:
        printWithBg("여자", "black", "bg_white")
    else:
        printWithBg("여자", "white", "bg_black")

    changeColor('white')
    changeColor('bg_black')

def printWithBg(text, color, bgcolor):
	changeColor(color)
	changeColor(bgcolor)
	print(text)

def changeColor(code):
	colors = {
		'black' : 30,
		'white' : 37,
		'bg_black' : 40,
		'bg_white' :47
	}
	print('\033['+ str(colors[code]) +'m', end = '\r')

print('하나를 선택해 주세요!')
time.sleep(1)
j = selectOne()
p=input()

os.system('cls')
age=input("태어난 해를 입력해 주세요('년' 제외): ")
age=str(age)

os.system('cls')
mbti=input("MBTI입력해 주세요: ")
os.system('cls')

# data_v = pd.read_csv('/data/'+age+'/Vermont.csv')
# data_n = pd.read_csv('/data/'+age+'/Newyork.csv')
# data_w = pd.read_csv('/data/'+age+'/Westvirginia.csv')
# data_t = pd.read_csv('/data/'+age+'/Texas.csv')
# data_c = pd.read_csv('/data/'+age+'/California.csv')
# data_m = pd.read_csv('/data/'+age+'/Massachusetts.csv')
# data_o = pd.read_csv('/data/'+age+'/Oregon.csv')

if mbti in v:
	data_v = pd.read_csv('data/'+age+'/Vermont.csv')
	if j==1:
		main_data=data_v.loc[name_rank,"m_name"]
	else:
		main_data=data_v.loc[name_rank,"f_name"]
elif mbti in n:
	data_n = pd.read_csv('data/'+age+'/Newyork.csv')
	if j==1:
		main_data=data_n.loc[name_rank,"m_name"]
	else:
		main_data=data_n.loc[name_rank,"f_name"]
elif mbti in w:
	data_w = pd.read_csv('data/'+age+'/Westvirginia.csv')
	if j==1:
		main_data=data_w.loc[name_rank,"m_name"]
	else:
		main_data=data_w.loc[name_rank,"f_name"]
elif mbti in t:
	data_t = pd.read_csv('data/'+age+'/Texas.csv')
	if j==1:
		main_data=data_t.loc[name_rank,"m_name"]
	else:
		main_data=data_t.loc[name_rank,"f_name"]
elif mbti in c:
	data_c = pd.read_csv('data/'+age+'/California.csv')
	if j==1:
		main_data=data_c.loc[name_rank,"m_name"]
	else:
		main_data=data_c.loc[name_rank,"f_name"]
elif mbti in m:
	data_m = pd.read_csv('data/'+age+'/Massachusetts.csv')
	if j==1:
		main_data=data_m.loc[name_rank,"m_name"]
	else:
		main_data=data_m.loc[name_rank,"f_name"]
else:
	data_o = pd.read_csv('data/'+age+'/Oregon.csv')
	if j==1:
		main_data=data_o.loc[name_rank,"m_name"]
	else:
		main_data=data_o.loc[name_rank,"f_name"]

print("당신의 영어이름은 ",main_data, "입니다.")
print('\033[1m'  + '\033[92m'+ main_data +'\033[0m')

os.system('pause')