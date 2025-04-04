import os
import base64
from flask import Flask, jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
import json

app = Flask(__name__)

def encrypt_data(key, data):
    key_bytes = base64.b64decode(key)
    iv = os.urandom(32)

    cipher = Cipher(algorithms.AES(key_bytes), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode('utf-8')) + encryptor.finalize()
    tag = encryptor.tag

    encrypted_data = iv + ciphertext + tag
    return encrypted_data

@app.route('/api/encrypted_data', methods=['GET'])
def get_encrypted_data():
    key = os.environ.get("ENCRYPTION_KEY")
    data =  [
      {
        "_id": "67ef8853b4aed6346c24d80f",
        "index": 0,
        "guid": "0f4f62f7-85de-4f7d-818f-733c6a846e07",
        "isActive": False,
        "balance": "$3,882.01",
        "picture": "http://placehold.it/32x32",
        "age": 37,
        "eyeColor": "brown",
        "name": "Marisol Duran",
        "gender": "female",
        "company": "TELPOD",
        "email": "marisolduran@telpod.com",
        "phone": "+1 (896) 483-3601",
        "address": "260 Louis Place, Hegins, Mississippi, 1723",
        "about": "Pariatur est ut amet non labore. Minim incididunt voluptate occaecat fugiat nostrud eiusmod est. Elit anim aliquip culpa consequat. Ad ipsum quis pariatur id id dolore dolor veniam in.\r\n",
        "registered": "2020-09-20T08:31:16 -06:-30",
        "latitude": -25.291338,
        "longitude": 12.67566,
        "tags": [
          "ea",
          "ut",
          "adipisicing",
          "qui",
          "in",
          "exercitation",
          "proident"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Irwin Spears"
          },
          {
            "id": 1,
            "name": "Walter Lynn"
          },
          {
            "id": 2,
            "name": "Diaz Goodman"
          }
        ],
        "greeting": "Hello, Marisol Duran! You have 4 unread messages.",
        "favoriteFruit": "banana"
      },
      {
        "_id": "67ef8853501c12b36af675a9",
        "index": 1,
        "guid": "621a0101-b1b2-43c9-938d-934895431214",
        "isActive": True,
        "balance": "$2,609.88",
        "picture": "http://placehold.it/32x32",
        "age": 31,
        "eyeColor": "blue",
        "name": "Sonya Kline",
        "gender": "female",
        "company": "MALATHION",
        "email": "sonyakline@malathion.com",
        "phone": "+1 (968) 425-3554",
        "address": "992 Girard Street, Walker, West Virginia, 2011",
        "about": "Do officia sit fugiat culpa adipisicing ad exercitation sit eu cupidatat. Incididunt enim laboris sunt aliquip dolor deserunt adipisicing non Lorem nisi voluptate id ad in. Fugiat non elit aliquip ea elit fugiat nulla dolore laborum ullamco. Amet dolor id et aute dolor et ea id velit proident eiusmod in. Elit id cillum ipsum elit. Do eiusmod occaecat occaecat fugiat. Et proident amet occaecat reprehenderit ex labore Lorem commodo.\r\n",
        "registered": "2023-03-01T04:04:04 -06:-30",
        "latitude": 49.856949,
        "longitude": 155.043568,
        "tags": [
          "proident",
          "irure",
          "in",
          "mollit",
          "laboris",
          "tempor",
          "amet"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Delia Gregory"
          },
          {
            "id": 1,
            "name": "Lucia Bruce"
          },
          {
            "id": 2,
            "name": "Constance Meyer"
          }
        ],
        "greeting": "Hello, Sonya Kline! You have 5 unread messages.",
        "favoriteFruit": "apple"
      },
      {
        "_id": "67ef885308ced9768f81f9ec",
        "index": 2,
        "guid": "84386839-f8eb-4835-84eb-6a173d02a3f9",
        "isActive": False,
        "balance": "$2,756.91",
        "picture": "http://placehold.it/32x32",
        "age": 40,
        "eyeColor": "blue",
        "name": "Langley Kennedy",
        "gender": "male",
        "company": "EARTHMARK",
        "email": "langleykennedy@earthmark.com",
        "phone": "+1 (988) 432-3821",
        "address": "161 Porter Avenue, Edgewater, Nevada, 1667",
        "about": "Occaecat sit sint irure nisi qui duis officia excepteur consectetur aliqua. Quis eu reprehenderit do aute fugiat laborum cillum do Lorem laboris do elit excepteur laboris. Aliquip culpa non incididunt adipisicing. Velit aliqua occaecat pariatur consequat mollit voluptate magna consequat eiusmod non ipsum. Eiusmod occaecat excepteur ut eu voluptate sunt eiusmod et id deserunt. Sunt eiusmod officia nulla cillum nisi est eu ex. Labore velit non irure id dolore ipsum cillum.\r\n",
        "registered": "2022-02-22T11:11:50 -06:-30",
        "latitude": 7.401913,
        "longitude": 155.520696,
        "tags": [
          "do",
          "laboris",
          "magna",
          "deserunt",
          "Lorem",
          "exercitation",
          "ad"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Christi Cobb"
          },
          {
            "id": 1,
            "name": "Anna Tran"
          },
          {
            "id": 2,
            "name": "Mattie Jordan"
          }
        ],
        "greeting": "Hello, Langley Kennedy! You have 10 unread messages.",
        "favoriteFruit": "apple"
      },
      {
        "_id": "67ef8853ef66b861a4612f71",
        "index": 3,
        "guid": "2a0718ea-ae72-4455-bd93-1642a48175f9",
        "isActive": True,
        "balance": "$1,785.20",
        "picture": "http://placehold.it/32x32",
        "age": 20,
        "eyeColor": "blue",
        "name": "Janie Blankenship",
        "gender": "female",
        "company": "HOTCAKES",
        "email": "janieblankenship@hotcakes.com",
        "phone": "+1 (940) 438-2038",
        "address": "311 Himrod Street, Torboy, Minnesota, 7150",
        "about": "Dolor enim deserunt consequat deserunt minim irure pariatur commodo commodo pariatur. Reprehenderit anim magna veniam fugiat labore. Ex aliquip velit laborum laboris culpa tempor. Ea incididunt est quis in qui. Voluptate nostrud ex amet ex nostrud non deserunt commodo. Nulla nostrud duis aute nostrud magna mollit excepteur.\r\n",
        "registered": "2023-02-04T05:55:43 -06:-30",
        "latitude": -78.009633,
        "longitude": -5.018579,
        "tags": [
          "commodo",
          "in",
          "sunt",
          "mollit",
          "est",
          "Lorem",
          "occaecat"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Buchanan Horne"
          },
          {
            "id": 1,
            "name": "Horn Carpenter"
          },
          {
            "id": 2,
            "name": "Marie Wilkins"
          }
        ],
        "greeting": "Hello, Janie Blankenship! You have 2 unread messages.",
        "favoriteFruit": "banana"
      },
      {
        "_id": "67ef8853ece01fe0ec18f0f9",
        "index": 4,
        "guid": "84a3b573-623f-4d58-bbd1-5465ec15d2c0",
        "isActive": False,
        "balance": "$2,296.27",
        "picture": "http://placehold.it/32x32",
        "age": 35,
        "eyeColor": "blue",
        "name": "Brandie Justice",
        "gender": "female",
        "company": "OPTICOM",
        "email": "brandiejustice@opticom.com",
        "phone": "+1 (932) 530-3672",
        "address": "495 Bay Avenue, Clay, Palau, 3633",
        "about": "Incididunt eiusmod tempor proident est irure laborum. Qui cupidatat voluptate elit irure proident cillum sunt culpa tempor minim deserunt. Dolor pariatur nisi enim sunt fugiat laborum. Qui voluptate enim deserunt magna.\r\n",
        "registered": "2019-12-31T10:40:02 -06:-30",
        "latitude": -76.374031,
        "longitude": -105.147758,
        "tags": [
          "commodo",
          "ut",
          "sit",
          "excepteur",
          "incididunt",
          "sint",
          "elit"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Melba Church"
          },
          {
            "id": 1,
            "name": "Justine Hansen"
          },
          {
            "id": 2,
            "name": "Walker Dunlap"
          }
        ],
        "greeting": "Hello, Brandie Justice! You have 5 unread messages.",
        "favoriteFruit": "apple"
      },
      {
        "_id": "67ef8853b4b0c75286f6b251",
        "index": 5,
        "guid": "06a72d60-52c1-45a3-82fb-7cbcaeb2f215",
        "isActive": True,
        "balance": "$2,781.15",
        "picture": "http://placehold.it/32x32",
        "age": 22,
        "eyeColor": "blue",
        "name": "Suzanne Jarvis",
        "gender": "female",
        "company": "NIQUENT",
        "email": "suzannejarvis@niquent.com",
        "phone": "+1 (883) 491-3766",
        "address": "836 Havens Place, Ogema, District Of Columbia, 3202",
        "about": "Nostrud quis labore voluptate laboris duis est minim est enim irure proident voluptate ipsum duis. Aliquip elit sunt reprehenderit fugiat aliquip consequat aute nisi. Eu consequat ipsum dolor deserunt commodo irure. Do nulla eu labore dolor amet ea consequat exercitation proident. Ut do nisi ipsum labore occaecat.\r\n",
        "registered": "2016-06-10T06:37:31 -06:-30",
        "latitude": 56.164453,
        "longitude": -168.724598,
        "tags": [
          "pariatur",
          "pariatur",
          "esse",
          "officia",
          "velit",
          "nostrud",
          "ipsum"
        ],
        "friends": [
          {
            "id": 0,
            "name": "Richards Freeman"
          },
          {
            "id": 1,
            "name": "Ashlee Davis"
          },
          {
            "id": 2,
            "name": "Joy Ball"
          }
        ],
        "greeting": "Hello, Suzanne Jarvis! You have 3 unread messages.",
        "favoriteFruit": "apple"
      }
    ]
    data_string = json.dumps(data)

    encrypted_value = encrypt_data(key, data_string)
    encrypted_value_b64 = base64.b64encode(encrypted_value).decode('utf-8')

    return jsonify({"success": True, "data": encrypted_value_b64})

if __name__ == '__main__':
    app.run(debug=True)
