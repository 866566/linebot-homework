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
    elif user_message.find('轉接真人客服') != -1:  # 判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。

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
        #user_message='影片訊息'
    elif user_message.find('影片訊息') != -1:         #判斷用戶使否傳來"影片訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = VideoSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=6LcWIDtZWbxjYUXS1Dod_vIF&ratebypass=yes&dur=328.423&lmt=1572331630804319&fvip=5&c=WEB&txp=2216222&n=fRjt_f_oTJeD95i&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMXkWqUW9UIIMrcCJZ8dh_xZ7nWpUlNVWd4sdw2JHME4AiAKGxqLL5z6kL30RkfuW-mCUVIwWmqG1nPPOo0_PbecxA%3D%3D&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=3b1b213d3dba3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858827&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgXT3f533nuXNJnQlehCh9ePDKFQtHpmkoWKAN1IzsJsgCIBtOmjBzv9DrdIWDtPjsHRSZXLCFcjAZN1zQSqWOHGEM',
            preview_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fmvQXV2wh96fqQjSJ5KZXRUjprXHH9zG2EVFLuExV-Uxl1sN2AQ76RIN8Cy6A0COCT4FvQg9YRzqNujWkrxwA3kgGLcAOtsupqBi0JCqx4HUQuMqR8KMJ6CRQ7FBSJ3JLHfYv04V_BFmQAMFQIrWgvsg=w958-h539'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='音訊訊息'
    elif user_message.find('音訊訊息') != -1:         #判斷用戶使否傳來"音訊訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = message = AudioSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=140&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fmp4&ns=vL6EbYMqRar6wkILnGFdM6sF&gir=yes&clen=5315836&otfp=1&dur=328.423&lmt=1572331593044296&fvip=5&keepalive=yes&c=WEB&txp=2211222&n=jinyYfcO0NUsfzO&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cotfp%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL1zzZOOX4qwpMs5f8cTrPvw7OLcoFlrx7IoNt4qKE_jAiA7W2Xce4BnGqfOPsuzNGEVGudGIMhqHBb5d40qsKMjdQ%3D%3D&ratebypass=yes&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=a0e283de1a31a3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858105&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhANHX1USrlIJC8IXts4LcHkOClswgQoSKtfv-bBU76R7VAiB8SAfZxTgonssKfxUs6FL8O8Q5wn5cnL2r_OSUuKtjRQ%3D%3D',
            duration=328000
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='位置訊息'
    elif user_message.find('位置訊息') != -1:         #判斷用戶使否傳來"位置訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = LocationSendMessage(
            title='文藻外語大學',
            address='80793高雄市三民區民族一路900號',
            latitude=22.6704067,
            longitude=120.3191348
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='貼圖訊息'
    elif user_message.find('貼圖訊息') != -1:         #判斷用戶使否傳來"貼圖訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114116'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0

###############################################################################
        #user_message='按鈕介面訊息'
    elif user_message.find('按鈕介面訊息') != -1:         #判斷用戶使否傳來"按鈕介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='按鈕介面訊息',
            template=ButtonsTemplate(
                thumbnail_image_url='https://imgs.gvm.com.tw/upload/gallery/20210126/77456_01.png',
                title='按鈕介面訊息',
                text='此種訊息可以設定1~4個按鈕選項，並可以設定一張1.51:1尺寸的圖片。',
                actions=[
                    MessageTemplateAction(
                        label='測試訊息',
                        text='您剛剛點擊了【測試訊息】'
                    ),
                    URITemplateAction(
                        label='文藻首頁',
                        uri='https://a001.wzu.edu.tw/'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='確認介面訊息'
    elif user_message.find('確認介面訊息') != -1:         #判斷用戶使否傳來"確認介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【確認介面訊息】',
            template=ConfirmTemplate(
                text='您是否確認要離開本次對話？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='我要離開對話'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='圖文訊息'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='輪播模板訊息'
    elif user_message.find('有什麼熱賣的商品推薦嗎？') != -1:         #判斷用戶使否傳來"輪播模板訊息"關鍵字，若為是則觸發本區段。
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【有什麼熱賣的商品推薦嗎？】',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/1t99JeL.jpeg',
                        title='這裡是我們的潮流熱賣商品🔥 \n每一件都是當下最受歡迎的，趕快來看看吧！ \n⚠️備註: 本店皆採取預購制 \n預購完的商品會在3~5個工作日通知寄送',
                        text='🔥熱賣商品🔥 \n包括寬鬆舒適的Oversized T-shirt👕 \n個性十足的Ripped Jeans👖 \n經典實用的Bomber Jacket🧥 \n這些時尚單品讓你輕鬆走在潮流前端！✨',
                        actions=[
                            MessageTemplateAction(
                                label='Oversized T-shirt 預購',
                                text='預購當季Oversized T-shirt'
                            ),
                            MessageTemplateAction(
                                label='Ripped Jeans 預購',
                                text='預購當季Ripped Jeans'
                            ),
                            MessageTemplateAction(
                                label='Bomber Jacket 預購',
                                text='預購當季Bomber Jacket'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/9JgO0oZ.jpeg',
                        title='我們的潮流熱賣配件都在這裡🔥 \n每一件都是現在最受歡迎的，快來看看吧！ \n⚠️備註: 本店皆採取預購制 \n預購完的商品會在3~5個工作日通知寄送',
                        text='🔥熱賣配件🔥 \n包括時尚精緻的Statement Necklaces💎 \n實用百搭的Leather Belts👖 \n潮流必備的Trendy Sunglasses🕶️ \n這些配件讓你的穿搭更具個性和風格！✨',
                        actions=[
                            MessageTemplateAction(
                                label='Statement Necklaces 預購',
                                text='預購當季Statement Necklaces'
                            ),
                            MessageTemplateAction(
                                label='Leather Belts 預購',
                                text='預購當季 Leather Belts'
                            ),
                            MessageTemplateAction(
                                label='Trendy Sunglasses 預購',
                                text='預購當季 Trendy Sunglasses'
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
        response='我不太了解您的意思，建議您透過選單與我互動唷！'
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