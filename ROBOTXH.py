from flask_ngrok import run_with_ngrok   # colab 使用，本機環境請刪除
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage
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
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        img_url = reply_img(msg)   # 取得對應的圖片，如果沒有取得，會是 False
        location_dict = reply_location(msg)   # 取得對應的地址，如果沒有取得，會是 False
        if img_url:
            # 如果有圖片網址，回傳圖片
            img_message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
            line_bot_api.reply_message(tk,img_message)
        elif location_dict:
            # 如果有地點資訊，回傳地點
            location_message = LocationSendMessage(
                title=location_dict['name'],
                address=location_dict['address'],
                latitude=location_dict['latitude'],
                longitude=location_dict['longitude']
            )
            line_bot_api.reply_message(tk, location_message)
        else:
            # 如果找不到對應的回應，回傳文字
            text_message = TextSendMessage(text='找不到相關資訊')
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

# 建立回覆地址的函式
def reply_location(text):
    # 文字對應地址資訊的字典
    location = {
        '台北101':{
            'name':'台北101',
            'address':'台灣台北市信義區信義路五段7號',
            'latitude':25.0339639,
            'longitude':121.5644722
        },
        '中正紀念堂':{
            'name':'中正紀念堂',
            'address':'台灣台北市
