import helper
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
   return 'Hello World!'


@app.route('/tasks', methods=['POST'])
def add_item():
   #Get item from the POST body
   req_data = request.get_json()

   content = req_data['content']

   # Add item to the list
   res_data = helper.add_to_list(content)

   #Return error if item not added
   if res_data is None:
      response = Response("{'error': 'Item not added - '}" +
                          content, status=400, mimetype='application/json')
      return response

   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')

   return response


@app.route('/tasks')
def get_all_items():
   # Get items from the helper
   res_data = helper.get_all_items()
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   return response

