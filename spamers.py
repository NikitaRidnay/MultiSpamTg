from telethon import TelegramClient
import time, telethon
import sys

from getpass import getpass
from time import sleep
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerChat, InputPeerChannel
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import ChannelParticipantsSearch, InputChannel
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import configparser
import json
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import Channel, InputChannel
from random import randrange

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime


# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

from colorama import init, Fore, Back, Style 




# Присваиваем значения внутренним переменным
api_id =111111
api_hash = 'kefwifn329nf32f'
limit = 100
idm = 1 
fromChannel=-1001974470617
source_channel =-1001974470617#отсюда

Sent_count=0
total_count=0

delay=1 #задержка в 1 сек перед отравкой след сообщения



# ...






text1 = '''
сообщения
'''
ti = 360

client = TelegramClient('slivmenss', api_id, api_hash)
client.start()
source_entity = client.get_entity(source_channel)
#target_entity = client.get_entity(target_channel)

async def dump_all_participants(channel):
	offset_user = 0
	limit_user = 100

	all_participants = []
	filter_user = ChannelParticipantsSearch('')

	while True:
		participants = await client(GetParticipantsRequest(channel,
			filter_user, offset_user, limit_user, hash=0))

		if not participants.users:
			break
		all_participants.extend(participants.users)
		offset_user += len(participants.users)

	all_users_details = []
	lst = []
	name = []
	for participant in all_participants:
		lst.insert(1, participant.id)
		name.insert(1, participant.first_name)

	win = int('0')
	block = int('0')
	for i in range(len(lst)):
		try:
			#i += 51
			await client.send_messages(lst[i], fromChannel)
			#await client_spam.send_message(lst[i], text1)
			win += 1
			print(Fore.BLUE, name[i] + " Успешно получил сообщение  |  Всего: " + str(win))
			time.sleep(5)
		except Exception as e:
			print(name[i] + "Не удалось отправить сообщение")
			print("Error:(",e)
			block += 1
	print(Fore.GREEN, f"\nУспешно отправлено: {win}\n\nНе удалось отправить: {block}")




async def start():
	url = input("Введите ссылку на канал или чат: ")
	channel = await client.get_entity(url)
	await dump_all_participants(channel)


async def main():
	while True:
		win = int('0')
		block = int('0')
		if idm == 1:
			base = []
			async for dialog in client.iter_dialogs():
				base.append(int(dialog.id))
			for i in base:
				try:
					await client.send_messages(i, fromChannel)
					win += 1
				except:
					block += 1
						
		else:
			try:
				#await client.forward_messages(i,from_peer=InputPeerChannel(channel_id=fromChannel['id'], access_hash=fromChannel['access_hash']))
				win += 1
			except:
				block += 1
		print(f"\nУспешно отправлено: {win}\n\nНе удалось отправить: {block}")
		time.sleep(ti)


async def check(amount):
	# Getting information about yourself
	me = await client.get_me()
	# You can print all the dialogs/conversations that you are part of:
	i = 1
	print("\n\n\nСписок диалогов:\n")
	async for dialog in client.iter_dialogs():
		print('Диалог', dialog.name, 'имеет айди', dialog.id)
		i += 1
		if i > amount and amount != int('0'):
			break



while True:
	print('''


Выберите действие:

1)Список чатов
2)Начать спам рассылку по группам
3)Выйти


''')
	change = input()
	if change.isdigit() == False:
		print('''Ошибка? Пиши нормально.
 
1)Список чатов
2)Начать спам рассылку по группам
3)Выйти

''')
	elif int(change) == 0000:
		with client:
			client.loop.run_until_complete(main())
	elif int(change) == 1:
		new_change = input("Введите сколько последних диалогов отобразить (введите 0, если отобразить все): ")
		if new_change.isdigit() == False:
			print('''

1)Список чатов
2)Начать спам рассылку по группам
3)Выйти

''')
		else:
			with client:
				client.loop.run_until_complete(check(int(new_change)))
	elif int(change) == 3:
		print("Пока...\nСозданно @antiniks")
		exit(':)')

	elif int(change) == 2:


		print('Если имеются проблемы с софтом пишите прогеру: @antiniks')
		# Get all the channels the client is a member of
		target_entities = [dialog.entity for dialog in client.iter_dialogs()if dialog.is_group and dialog.entity != source_entity and client.get_participants(dialog.entity)]
		# Iterate through the target channels and forward messages from the source channel
		messages = client.iter_messages(source_channel)
		total_count = len(list(messages))*len(list(target_entities))



		for message in messages:
			for entity in target_entities:
				if total_count > Sent_count:
					try:
						client.send_messages(entity, message)

						#total_count += 1
					except Exception as e:
						print(f"Ошибка отправки: {e}")
					Sent_count += 1
				else:

					print(Fore.CYAN,'все сообщения отправлены')
					exit()
			print(Fore.BLUE, f"Успешно отправленных: {Sent_count} Из {total_count}")
			time.sleep(delay)  # Add a delay before sending the next batch of messages

	elif int(change) == 200:
		with client:
			client.loop.run_until_complete(start())
	
