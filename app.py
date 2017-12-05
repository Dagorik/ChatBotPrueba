#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import json
#from pymessenger.bot import Bot
from replies_bot import RepliesBot

app = Flask(__name__)

ACCESS_TOKEN = ""
VERIFY_TOKEN = ""

#bot = Bot(ACCESS_TOKEN)
#replies_bot = RepliesBot(bot)


@app.route('/')
def home():
	return 'Incio del server del servidor'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		output = request.json
		print("--------------------------------")
		print(output)
		print("--------------------------------")
		for event in output['entry']:
			messaging = event['messaging']
			for eventMessage in messaging:
				sender_id = eventMessage['sender']['id']
				try:
					message = eventMessage['message']['text']
				except:
					message = "HOLA"
				#print("****************************************")
				action = eventMessage['message']['nlp']['entities']['intent'][0]['value']

				print(message + ' by '+ sender_id + ' action '+ str(action))
				#print("****************************************")
				respuestas = RepliesBot()
				if message.upper() == 'HOLA':
					respuestas.saluda(sender_id)
				if message.upper() == 'QUICK':	
					respuestas.quick(sender_id)
				if message.upper() == 'GENERIC':
					respuestas.generic(sender_id)
				if action.upper() == 'QUIERO':
					respuestas.quiero(sender_id)

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return "Verificar el token"

	return "Chatbot de Prueba"

if __name__ == '__main__':
	app.run(port=5000, debug=True)