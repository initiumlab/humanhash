# -*- coding: utf-8 -*-
"""
humanhash: Human-readable representations of digests.

The simplest ways to use this module are the :func:`humanize` and :func:`uuid`
functions. For tighter control over the output, see :class:`HumanHasher`.
"""

import operator
import uuid as uuidlib

DEFAULT_WORDLIST = [
    u"中新關係",
    u"簡明憲政",
    u"台媒觀察",
    u"中國因素",
    u"丁屋政策",
    u"偷情網站",
    u"讀者來函",
    u"香港前途",
    u"變動中國",
    u"大學教育",
    u"社運叢談",
    u"工業展望",
    u"閱後即焚",
    u"特約轉載",
    u"都市脈搏",
    u"新界東北",
    u"城市小說",
    u"一國兩制",
    u"港大風波",
    u"繁花之地",
    u"論壇精華",
    u"中國經濟",
    u"白宮之路",
    u"生死愛欲",
    u"港獨爭議",
    u"讀書時間",
    u"文化研究",
    u"攝影人語",
    u"SPOT",
    u"中港足球",
    u"金融市場",
    u"全球政經",
    u"玩轉繪本",
    u"兩岸博弈",
    u"霧中風景",
    u"節氣好食",
    u"週日翻書",
    u"干政風波",
    u"版權條例",
    u"冰山之下",
    u"人物專訪",
    u"穹頂之上",
    u"港台互文",
    u"北京切除",
    u"讀者來稿",
    u"特約企劃",
    u"特首選舉",
    u"廣編企劃",
    u"文青時代",
    u"六七暴動",
    u"天大下勢",
    u"周日讀書",
    u"前途自決",
    u"柏林影展",
    u"街道書寫",
    u"雄安手記",
    u"斬樹爭議",
    u"觀看之道",
    u"財經角度",
    u"平權之路",
    u"聶樹斌案",
    u"編劇談戲",
    u"探索教育",
    u"產業評論",
    u"性別平權",
    u"華人參政",
    u"香港法治",
    u"島嶼深論",
    u"書商失蹤",
    u"宣誓風波",
    u"公共討論",
    u"特別企劃",
    u"泛民前路",
    u"所謂教育",
    u"疫苗之殤",
    u"小端選書",
    u"談情說愛",
    u"天下大勢",
    u"川震十年",
    u"城市對看",
    u"新聞自由",
    u"2047",
    u"政經人文",
    u"小端信箱",
    u"香港書展",
    u"共享經濟",
    u"施政報告",
    u"本土思潮",
    u"台日線上",
    u"文青過年",
    u"動物公民",
    u"朝陽群眾",
    u"歷史學人",
    u"暗黑賀歲",
    u"聖誕特輯",
    u"紀實攝影",
    u"主題書單",
    u"女性主義",
    u"逝者如斯",
    u"難民故事",
    u"韓流動向",
    u"乜乜物物",
    u"多元世代",
    u"惡性傷醫",
    u"國際焦點",
    u"視頻新聞",
    u"城市放題",
    u"城市觀察",
    u"日本視野",
    u"授權轉載",
    u"里約奧運",
    u"產業訊息",
    u"雨傘運動",
    u"油街寫作",
    u"獨立出版",
    u"空間政治",
    u"易怒體質",
    u"行山筆記",
    u"南美觀察",
    u"歷史教育",
    u"性感中國",
    u"女權主義",
    u"台灣視野",
    u"深入中東",
    u"洞背之見",
    u"花言峭語",
    u"世代觀點",
    u"數據世界",
    u"產業報導",
    u"港式文化",
    u"中港關係",
    u"消費升級",
    u"女權運動",
    u"電影評論",
    u"中梵協議",
    u"軍事解構",
    u"雙十講話",
    u"團年滋味",
    u"廣告企劃",
    u"城市筆記",
    u"教育平權",
    u"多元故事",
    u"一孩政策",
    u"印尼爆炸",
    u"想像吾城",
    u"跨界日記",
    u"媒體觀察",
    u"會員專屬",
    u"學人新知",
    u"卡乎專欄",
    u"持續更新",
    u"哲學思辨",
    u"法律通識",
    u"週末讀書",
    u"端三週年",
    u"朝陽羣眾",
    u"華人觀察",
    u"格物致知",
    u"中東局勢",
    u"親密關係",
    u"導演手記",
    u"諾貝爾獎",
    u"開放數據",
    u"城市散步",
    u"政經論衡",
    u"文青電影",
    u"旺角騷亂",
    u"文化觀察",
    u"人工智能",
    u"攝影展覽",
    u"媒體素養",
    u"創新科技",
    u"對話時間",
    u"大師身影",
    u"中港矛盾",
    u"圖片故事",
    u"英國大選",
    u"毅行總結",
    u"影像故事",
    u"東京物語",
    u"資訊分享",
    u"歷史敘事",
    u"寰宇經濟",
    u"台中生活",
    u"哲學教育",
    u"歐洲觀察",
    u"香港研究",
    u"週末翻書",
    u"藝術抗爭",
    u"對沖心道",
    u"讀者來信",
    u"彼鄰動態",
    u"特首選戰",
    u"探索學院",
    u"拆十字架",
    u"中國反腐",
    u"總編周記",
    u"生死無盡",
    u"演講節錄",
    u"香港政局",
    u"公共空間",
    u"雨傘週年",
    u"影像評論",
    u"旗艦論壇",
    u"魔幻旺角",
    u"教育現場",
    u"網絡觀察",
    u"安樂茶飯",
    u"解讀地產",
    u"周日電影",
    u"耳朵借你",
    u"繼續報導",
    u"陸生健保",
    u"新東補選",
    u"評論專欄",
    u"深度遊記",
    u"思想學人",
    u"獨立時代",
    u"吸金聖誕",
    u"國際關係",
    u"斯人已逝",
    u"到訪古巴",
    u"遊戲時間",
    u"影像遊記",
    u"思想寰宇",
    u"流行文化",
    u"攝影評論",
    u"公民社會",
    u"待友之道",
    u"週末文學",
    u"沒島戀曲",
    u"揭開紅幕",
    u"計劃生育",
    u"同志平權",
    u"轉型正義",
    u"對號入座",
    u"編讀手記",
    u"兩岸觀察",
    u"另類職人",
    u"創科前景",
    u"法國大選",
    u"世代對話",
    u"社運反思",
    u"新界問題",
    u"風格邊界",
    u"社會運動",
    u"科創觀察",
    u"佳士工運",
    u"六四週年",
    u"香港安老",
    u"兩韓峯會",
    u"中國修憲",
    u"同婚法案",
    u"難民危機",
    u"世界公民",
    u"哲學來了",
]


class HumanHasher(object):
    """
    Transforms hex digests to human-readable strings.

    The format of these strings will look something like:
    `victor-bacon-zulu-lima`. The output is obtained by compressing the input
    digest to a fixed number of bytes, then mapping those bytes to one of 256
    words. A default wordlist is provided, but you can override this if you
    prefer.

    As long as you use the same wordlist, the output will be consistent (i.e.
    the same digest will always render the same representation).
    """

    def __init__(self, wordlist=DEFAULT_WORDLIST):
        if len(wordlist) != 256:
            raise ArgumentError("Wordlist must have exactly 256 items")
        self.wordlist = wordlist

    def humanize(self, hexdigest, words=4, separator='-'):
        """
        Humanize a given hexadecimal digest.

        Change the number of words output by specifying `words`. Change the
        word separator with `separator`.

            >>> digest = '60ad8d0d871b6095808297'
            >>> HumanHasher().humanize(digest)
            'sodium-magnesium-nineteen-hydrogen'
        """

        # Gets a list of byte values between 0-255.
        bytes = map(lambda x: int(x, 16),
                    map(''.join, zip(hexdigest[::2], hexdigest[1::2])))
        # Compress an arbitrary number of bytes to `words`.
        compressed = self.compress(bytes, words)
        # Map the compressed byte values through the word list.
        return separator.join(self.wordlist[byte] for byte in compressed)

    @staticmethod
    def compress(bytes, target):
        """
        Compress a list of byte values to a fixed target length.

            >>> bytes = [96, 173, 141, 13, 135, 27, 96, 149, 128, 130, 151]
            >>> HumanHasher.compress(bytes, 4)
            [205, 128, 156, 96]

        Attempting to compress a smaller number of bytes to a larger number is
        an error:

            >>> HumanHasher.compress(bytes, 15)  # doctest: +ELLIPSIS
            Traceback (most recent call last):
            ...
            ValueError: Fewer input bytes than requested output
        """

        length = len(bytes)
        if target > length:
            raise ValueError("Fewer input bytes than requested output")

        # Split `bytes` into `target` segments.
        seg_size = length // target
        segments = [
            bytes[i * seg_size:(i + 1) * seg_size] for i in xrange(target)
        ]
        # Catch any left-over bytes in the last segment.
        segments[-1].extend(bytes[target * seg_size:])

        # Use a simple XOR checksum-like function for compression.
        def checksum(bytes):
            return reduce(operator.xor, bytes, 0)

        checksums = map(checksum, segments)
        return checksums

    def uuid(self, **params):
        """
        Generate a UUID with a human-readable representation.

        Returns `(human_repr, full_digest)`. Accepts the same keyword arguments
        as :meth:`humanize` (they'll be passed straight through).
        """

        uuid = str(uuidlib.uuid4())
        digest = uuid.replace('-', '')
        return self.humanize(digest, **params), uuid


DEFAULT_HASHER = HumanHasher()
uuid = DEFAULT_HASHER.uuid
humanize = DEFAULT_HASHER.humanize
