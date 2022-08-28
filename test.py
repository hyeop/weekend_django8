import googletrans
from gtts import gTTS
from googletrans import Translator

di = googletrans.LANGUAGES
print(di)
text3 ="""26일 효연은 자신의 인스타그램에 스토리에 "지갑을 찾습니다. 제일 아끼는 지갑인데 어디갔니, 지갑아. 안에 돈은 가져도 되니 지갑만 돌려주세요"라고 적었다.

그러면서 그는 분실한 지갑을 주인에게 돌려주는 방법을 설명했다. 지갑에 있는 신용카드의 고객센터에 전화를 걸면 상담사가 확인한 다음 지갑 주인에게 연락처를 알려주고, 주인에게서 연락이 오면 돌려주는 것이다.

한편 효연이 속한 소녀시대는 정규 7집 앨범을 발매하고 완전체로 컴백했다."""
translator = Translator()


trans3 = translator.translate(text3, src='ko', dest="zh-cn")
g = gTTS(trans3.text, lang="zh-cn")
g.save("sosi.mp3")

from googletrans import Translator
translator = Translator()
trans3 = translator.translate(text3, src='ko', dest="zh-cn")
