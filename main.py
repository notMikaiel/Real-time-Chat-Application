import bottle
import json
import chat

################################################################
#       Functions needed to allow clients to access files      #
################################################################

@bottle.route('/')
def index():
  html_file = bottle.static_file("index.html", root=".")
  return html_file

@bottle.route('/chat.js')
def chat_file():
  chat_js_file = bottle.static_file("chat.js", root=".")
  return chat_js_file

@bottle.route('/ajax.js')
def ajax_file():
  ajax_js_file = bottle.static_file("ajax.js", root=".")
  return ajax_js_file  

################################################################
#             Functions handling AJAX interactions             #
################################################################

@bottle.get('/chat')
def respond_with_chat():
  messages = chat.get_chat()
  ret_val = json.dumps(messages)
  return ret_val

@bottle.post('/send')
def do_chat():
  json_receive = bottle.request.body.read().decode()
  message_dic = json.loads(json_receive)
  # Pauses are NOT needed; I am adding this to emphasize that
  # the server and client are completely different machines
  add_pause()
  chat.add_message(message_dic['message'])
  response = chat.get_chat()
  ret_val = json.dumps(response)
  return ret_val

################################################################
#      Support functions to help make the demo interesting     #
################################################################

# This function is not needed, but is used to add more realism
# to the application by forcing short pauses
def add_pause() :
  import random
  import time
  # Pauses for 0 - 5 seconds
  pause = random.choice([0, 1, 2, 3, 4, 5])
  if pause != 0 :
    time.sleep(pause)

################################################################
#      Start the webserver                                     #
################################################################

bottle.run(host="0.0.0.0", port=8080)