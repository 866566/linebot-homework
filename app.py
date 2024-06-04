# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: peishuo
"""

import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi('GLWMNmF1zyP+UW2LOXeIn6NOexscmsg3GOsYUMINyajUIaE1ClTafjqyKU+Rswo9N5xpXK5Rd+WgVUF30Qrr1TDPEY0B8Yz2kbGZ5G1RL+5UfG+muf2jKFgwx4E3VJ9Mu7r0K++C1zd+pvkTjIYReQdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('78772481a1296c6a3e30ff3709be34c7')

line_bot_api.push_message('U8877a80277890b64ec63a93f9e0265e7', TextSendMessage(text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name     #使用者名稱
    uid = profile.user_id             #使用者ID  
    user_message=str(event.message.text) 
    

        #user_message='圖文訊息'
    if user_message.find('圖文訊息') != -1:    
        
        res_message = TemplateSendMessage(
            alt_text='圖文訊息',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息',
                                text='文字訊息'
                            ),
                            MessageTemplateAction(
                                label='圖片訊息',
                                text='圖片訊息'
                            ),
                            MessageTemplateAction(
                                label='影片訊息',
                                text='影片訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='音訊訊息',
                                text='音訊訊息'
                            ),
                            MessageTemplateAction(
                                label='位置訊息',
                                text='位置訊息'
                            ),
                            MessageTemplateAction(
                                label='貼圖訊息',
                                text='貼圖訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='按鈕介面訊息',
                                text='按鈕介面訊息'
                            ),
                            MessageTemplateAction(
                                label='確認介面訊息',
                                text='確認介面訊息'
                            ),
                            MessageTemplateAction(
                                label='輪播模板訊息',
                                text='輪播模板訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='輪播圖模板訊息',
                                text='輪播圖模板訊息'
                            ),
                            URITemplateAction(
                                label='Line官方說明文件',
                                uri='https://developers.line.biz/zh-hant/docs/messaging-api/message-types/#common-features'
                            ),
                            MessageTemplateAction(
                                label='其他',
                                text='教材尚在開發中'
                            ),
                        ]
                    ),                                          
# =============================================================================        
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='文字訊息'
    elif user_message.find('我想查看所有商品的清單') != -1:         #判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。
        
        res_message = TextSendMessage(text='當然，這裡是我們的商品清單📜，請隨意瀏覽！ \n店家網址: \nhttp://www.charmshoppingfashionstore.com \n如果有任何問題或需要幫助，隨時告訴我哦！')
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0
###############################################################################
        # user_message='文字訊息'
    elif user_message.find('現在有什麼特惠活動嗎？') != -1:  # 判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。

        res_message = TextSendMessage(
            text='太棒了！我們目前的特惠活動正在火熱進行中🔥！ \n這裡是近期的特惠商品列表🎁，超多優惠，等你來搶購💸！ \n我們的特惠活動包括： \n全場滿千折百💯： \n只要消費滿1000元，就能享受100元的折扣！ \n指定商品五折優惠🛍️： \n多款熱門商品限時五折，讓你買到賺到！ \n會員專屬優惠👑： \n加入我們的會員，即可享受額外折扣和專屬禮品🎉！ \n此外，還有一些注意事項需要提醒您📝： \n活動期限⏳：\n 本次特惠活動僅限於2024年6月1日至6月30日，請在活動期間內完成購買。\n 庫存有限⚠️：\n部分特惠商品數量有限，售完即止，建議您儘早購買！ \n不與其他優惠同享🚫： \n本次特惠活動的折扣不可與其他優惠活動同時使用。 \n會員優惠條件📋： \n若要享受會員專屬優惠，請確保您的會員帳號狀態有效，並在結帳時登入。  \n別錯過這些超值好物，快點看看吧👇！ \n還有更多驚喜等著你發現哦🎊！ \n祝您購物愉快🛒！')
        line_bot_api.reply_message(event.reply_token, res_message)
        return 0
###############################################################################
        # user_message='文字訊息'
    elif user_message.find('聯絡客服') != -1:  # 判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。

        res_message = TextSendMessage(
            text='💁客服在線時間:周一~周日 10:00 A.M~19:00 P.m \n若沒有及時回復代表真人客服忙線中，煩請耐心等待回復。 \n您也可以透過以下聯絡方式聯絡本店 \n📞電話：123-456-789 \n📪Email：charmshoppingstore@gmail.com \n🏚️本店地址：高雄市 中華路 00號 \n如有任何問題，請隨時與我們聯繫。')
        line_bot_api.reply_message(event.reply_token, res_message)
        return 0
###############################################################################
    elif user_message.find('限時秒殺活動開始啦') != -1 :         #判斷用戶使否傳來"圖片訊息"關鍵字，若為是則觸發本區段。
        
        res_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/cT1I2jD.jpeg',
            preview_image_url='https://i.imgur.com/cT1I2jD.jpeg'
        )
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
        #user_message='輪播模板訊息'
    elif user_message.find('有什麼熱賣的商品推薦嗎？') != -1:         #判斷用戶使否傳來"輪播模板訊息"關鍵字，若為是則觸發本區段。
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【輪播模板訊息】',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/iPXgw5X.jpeg',
                        title='這裡是我們的潮流熱賣商品🔥 \n每一件都是當下最受歡迎的，趕快來看看吧！',
                        text='🔥熱賣商品🔥',
                        actions=[
                            MessageTemplateAction(
                                label='T袖預購',
                                text='預購當季T-shirt'
                            ),
                            MessageTemplateAction(
                                label='牛仔褲預購',
                                text='預購當季Jeans'
                            ),
                            MessageTemplateAction(
                                label='夾克預購',
                                text='預購當季Jacket'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/iPXgw5X.jpeg',
                        title='我們的潮流熱賣配件都在這裡🔥 \n每一件都是現在最受歡迎的，快來看看吧！',
                        text='🔥熱賣配件🔥',
                        actions=[
                            MessageTemplateAction(
                                label='項鍊預購',
                                text='預購當季Necklace'
                            ),
                            MessageTemplateAction(
                                label='腰帶預購',
                                text='預購當季Belts'
                            ),
                            MessageTemplateAction(
                                label='太陽眼鏡預購',
                                text='預購當季Sunglasses'
                            )
                        ]
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='輪播圖模板訊息'
    elif user_message.find('有什麼最新上架套餐的商品嗎？') != -1:         #判斷用戶使否傳來"輪播圖模板訊息"關鍵字，若為是則觸發本區段。
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【有什麼最新上架的商品嗎？】',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/iPXgw5X.jpeg',
                        action=PostbackTemplateAction(
                            label='預購',
                            text='預購此套燦商品',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/bPN1qEN.jpeg',
                        action=PostbackTemplateAction(
                            label='預購',
                            text='預購此套餐商品',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='相關網頁->學術單位'
    elif user_message.find('相關網頁->學術單位') != -1:         #判斷用戶使否傳來"相關網頁->學術單位"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->學術單位',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='英國語文系',
                                uri='http://c021.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='翻譯系',
                                uri='http://c033.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際事務系',
                                uri='http://c030.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='國際企業管理系',
                                uri='http://c031.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='英語教學中心',
                                uri='http://c043.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='法國語文系',
                                uri='http://c022.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='德國語文系',
                                uri='http://c023.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='西班牙語文系',
                                uri='http://c024.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='日本語文系',
                                uri='http://c025.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='外語教學系',
                                uri='http://c036.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='應用華語文系',
                                uri='http://c026.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='傳播藝術系',
                                uri='http://c032.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='數位內容應用與管理系',
                                uri='http://c028.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='師資培育中心',
                                uri='http://c035.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='通識教育中心',
                                uri='http://c034.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================    
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁->行政單位'
    elif user_message.find('相關網頁->行政單位') != -1:         #判斷用戶使否傳來"相關網頁->行政單位"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->行政單位',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校長室',
                                uri='https://c001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='副校長室',
                                uri='https://c002.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='秘書室',
                                uri='https://c008.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='教務處',
                                uri='https://c003.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='學生事務處',
                                uri='https://c004.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='研究發展處',
                                uri='https://c016.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='總務處',
                                uri='https://c005.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際暨兩岸合作處',
                                uri='https://c015.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='進修部',
                                uri='https://c007.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='推廣部',
                                uri='https://c049.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='會計室',
                                uri='https://c010.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='人事室',
                                uri='https://c009.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊與教學科技中心',
                                uri='https://c013.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='教師發展中心',
                                uri='https://c014.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁->常用網頁'
    elif user_message.find('相關網頁->常用網頁') != -1:         #判斷用戶使否傳來"相關網頁->常用網頁"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->常用網頁',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校網首頁',
                                uri='https://a001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊服務入口網',
                                uri='https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='雲端學園',
                                uri='http://elearning2.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='網路選課系統',
                                uri='https://info.wzu.edu.tw/choice/'
                            ),
                            URITemplateAction(
                                label='活動管理系統',
                                uri='http://ma.wzu.edu.tw/bin/home.php'
                            ),
                        ]
                    ),                                          
# =============================================================================   
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁'
    elif user_message.find('相關網頁') != -1:         #判斷用戶使否傳來"相關網頁"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='請選擇您想查找的頁面',
                        text='請由下方選項中選出子分類！',
                        actions=[
                            MessageTemplateAction(
                                label='學術單位',
                                text='相關網頁->學術單位'
                            ),
                            MessageTemplateAction(
                                label='行政單位',
                                text='相關網頁->行政單位'
                            ),
                            MessageTemplateAction(
                                label='常用網頁',
                                text='相關網頁->常用網頁'
                            )
                        ]
                    ),                                          
# =============================================================================
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
    elif user_message.find('輪播圖') != -1:
        
        return 0
###############################################################################
    elif user_message.find('您剛剛點擊了') != -1:
        
        return 0
###############################################################################
    elif user_message.find('教材尚在開發中') != -1:
        
        return 0
###############################################################################
    elif user_message.find('我要離開對話') != -1:
        response='好的，期待您下次的呼喚，再見！'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        
        return 0
###############################################################################
    else:
        response='感謝您的耐心等待！我們的小編已經指派專人來處理您的要求啦~ 😊🙌🎉'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        return 0
        
    
    # user_id = event.source.user_id
    # print("user_id =", user_id)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))



###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
