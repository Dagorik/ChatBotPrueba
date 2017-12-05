import requests

class RepliesBot():
	def saluda(self,sender_id):
		JSON = {
						"messaging_type": "RESPONSE",
						"recipient":{
  						"id":sender_id
										},
						"message":{
  						"text":"hello, world!"
							}
						}					
		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAKZAgZBXnvBkBAL7pW2STDGuHkxGME2H9qqHBtORj1K9jRYtwXnM0Igv5rP8TWSsTSJtgFyuiTypn8u9fFP5zPVT2LJNdeN4YZAEiQ2XZCWPsuCDhUe1FhAv5EI7pfc7IZA563C4NiaZAUxLJAr9Qqs0x2Dz2KU1HVkfeRqyubAZDZD"
		send = requests.post(URL,json = JSON)
		return True	

	def quiero(self,sender_id):
		JSON = {
						"messaging_type": "RESPONSE",
						"recipient":{
  						"id":sender_id
										},
						"message":{
  						"text":"Dime que quieres morro!"
							}
						}					
		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAKZAgZBXnvBkBAL7pW2STDGuHkxGME2H9qqHBtORj1K9jRYtwXnM0Igv5rP8TWSsTSJtgFyuiTypn8u9fFP5zPVT2LJNdeN4YZAEiQ2XZCWPsuCDhUe1FhAv5EI7pfc7IZA563C4NiaZAUxLJAr9Qqs0x2Dz2KU1HVkfeRqyubAZDZD"
		send = requests.post(URL,json = JSON)
		return True	


	def quick(self,sender_id):
		JSON = {
  "recipient":{
    "id":sender_id
  },
  "message":{
    "text": "Here's a quick reply!",
    "quick_replies":[
      {
        "content_type":"text",
        "title":"Search",
        "payload":"POSTBACK_IMAGE",
        "image_url":"https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg"
      },
      {
        "content_type":"location"
      },
      {
        "content_type":"text",
        "title":"Something Else",
        "payload":"POSTBACK_TEXT"
      }
    ]
  }
}


		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAKZAgZBXnvBkBAL7pW2STDGuHkxGME2H9qqHBtORj1K9jRYtwXnM0Igv5rP8TWSsTSJtgFyuiTypn8u9fFP5zPVT2LJNdeN4YZAEiQ2XZCWPsuCDhUe1FhAv5EI7pfc7IZA563C4NiaZAUxLJAr9Qqs0x2Dz2KU1HVkfeRqyubAZDZD"
		send = requests.post(URL,json = JSON)
		return True	


	def generic(self,sender_id):
		JSON = {
  "recipient":{
    "id":sender_id
  },
  "message":{
    "attachment":{
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[

        	{'title': 'Cotizar',
						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
						  'subtitle': 'Cotiza tu envío',
						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
						  },
						  {'title': 'Cotizar',
						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
						  'subtitle': 'Cotiza tu envío',
						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
						  }
        ]
      }
    }
  }
}
		URL = "https://graph.facebook.com/v2.6/me/messages?access_token=EAAKZAgZBXnvBkBAL7pW2STDGuHkxGME2H9qqHBtORj1K9jRYtwXnM0Igv5rP8TWSsTSJtgFyuiTypn8u9fFP5zPVT2LJNdeN4YZAEiQ2XZCWPsuCDhUe1FhAv5EI7pfc7IZA563C4NiaZAUxLJAr9Qqs0x2Dz2KU1HVkfeRqyubAZDZD"
		send = requests.post(URL,json = JSON)
		print(send.text)
		return True
		