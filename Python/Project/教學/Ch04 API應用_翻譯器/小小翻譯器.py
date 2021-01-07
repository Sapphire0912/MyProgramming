# Link: https://clay-atlas.com/blog/2020/05/05/python-cn-note-package-googletrans-google-translate/

import googletrans
from pprint import pprint

translator = googletrans.Translator() # 建立一個翻譯器

results = translator.translate('我覺得今天天氣不好') # translate(), 輸入要被翻譯的句子
# print(results)
# print(results.text)
# Translated(src=zh-CN, dest=en, text=I think the weather is bad today, pronunciation=None, extra_data="{'translat...")
# I think the weather is bad today

# 在沒有設定的情況下, 輸入的字串會自動偵測最有可能的語言, 而輸出的語言則預設為英文
# 自行設定翻譯的語言(透過 dest 參數設定)
# print("English: ", translator.translate("我覺得今天天氣不好", dest = 'en').text)
# print("Japanese: ", translator.translate("我覺得今天天氣不好", dest = 'ja').text)
# print("Korean: ", translator.translate("我覺得今天天氣不好", dest = 'ko').text)
# English:  I think the weather is bad today
# Japanese:  今日は天気が悪いと思います
# Korean:  오늘 날씨가 안 좋은 것 같아요

# 偵測語言
unknown = 'おはよう'
det = translator.detect(unknown)
# print(det) # Detected(lang=ja, confidence=1.0)
# print(det.lang) # ja

# 取得語言編碼
pprint(googletrans.LANGCODES) # 輸出由字典組成的語言及對應的編碼