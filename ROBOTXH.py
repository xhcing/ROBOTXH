from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        msg = json_data['events'][0]['message']['text']   # 取得使用者發送的訊息
        text_message = TextSendMessage(text=msg)          # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,text_message)       # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()
app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']      # 取得 reply token
        stickerId = json_data['events'][0]['message']['stickerId'] # 取得 stickerId
        packageId = json_data['events'][0]['message']['packageId'] # 取得 packageId
        sticker_message = StickerSendMessage(sticker_id=stickerId, package_id=packageId) # 設定要回傳的表情貼圖
        line_bot_api.reply_message(tk,sticker_message)  # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()
app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        img_url = reply_img(msg)   # 取得對應的圖片，如果沒有取得，會是 False
        if img_url:
            # 如果有圖片網址，回傳圖片
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(tk,img_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text='找不到相關圖片')
            line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'
# 建立回覆圖片的函式
def reply_img(text):
    # 文字對應圖片網址的字典
    img = {
        '皮卡丘':'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png',
        '傑尼龜':'https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png'
    }
    if text in img:
      return img[text]
    else:
      # 如果找不到對應的圖片，回傳 False
      return False

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('你的 Channel access token')
        handler = WebhookHandler('你的 LINE Channel secret')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        location_dect = reply_location(msg)     # 取得對應的地址，如果沒有取得，會是 False
        if location_dect:
            # 如果有地點資訊，回傳地點
            location_message = LocationSendMessage(title=location_dect['title'],
                                                  address=location_dect['address'],
                                                  latitude=location_dect['latitude'],
                                                  longitude=location_dect['longitude'])
            line_bot_api.reply_message(tk,location_message)
        else:
            # 如果是 False，回傳文字
            text_message = TextSendMessage(text='找不到相關地點')
            line_bot_api.reply_message(tk,text_message)
    except:
        print('error')
    return 'OK'
# 建立回覆地點的函式
def reply_location(text):
    # 建立地點與文字對應的字典
    location = {
        '101':{
            'title':'台北 101',
            'address':'110台北市信義區信義路五段7號',
            'latitude':'25.034095712145003',
            'longitude':'121.56489941996108'
        },
        '總統府':{
            'title':'總統府',
            'address':'100台北市中正區重慶南路一段122號',
            'latitude':'25.040319874750914',
            'longitude':'121.51162883484746'
        }
    }
    if text in location:
      return location[text]
    else:
      # 如果找不到對應的地點，回傳 False
      return False

if __name__ == "__main__":
    run_with_ngrok(app)         # colab 使用，本機環境請刪除
    app.run()
heroku create myapp --buildpack https://github.com/some/buildpack.git
