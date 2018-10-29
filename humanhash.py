# -*- coding: utf-8 -*-
"""
humanhash: Human-readable representations of digests.

The simplest ways to use this module are the :func:`humanize` and :func:`uuid`
functions. For tighter control over the output, see :class:`HumanHasher`.
"""

import operator
import uuid as uuidlib

DEFAULT_WORDLIST = [
    u"中國經濟大變局",
    u"深度",
    u"少數族羣",
    u"廣場",
    u"傘運週年",
    u"中梵協議",
    u"圓桌",
    u"旅行",
    u"LGBT",
    u"香港高鐵通車",
    u"公司新聞",
    u"深圳佳士工運",
    u"毒奶粉十年",
    u"談情說愛",
    u"疫苗之殤",
    u"中美貿易戰",
    u"直播",
    u"異鄉人",
    u"影像",
    u"親子",
    u"探索學院",
    u"端聞",
    u"愛慾錄",
    u"觀點",
    u"國際",
    u"電影",
    u"生死觀",
    u"香港",
    u"大陸",
    u"GameON",
    u"六四週年",
    u"臺灣",
    u"風物",
    u"香港安老",
    u"兩韓峯會",
    u"城市",
    u"STYLE",
    u"中國修憲",
    u"北京切除",
    u"互聯網審查",
    u"讀書時間",
    u"互聯網政治",
    u"小粉紅學",
    u"臺灣同婚法案",
    u"歐洲難民危機",
    u"網媒採訪權",
    u"世界公民在香港",
    u"特朗普來了",
    u"編讀手記",
    u"玩新聞",
    u"雨傘反思與前瞻",
    u"銅鑼灣書店",
    u"華航罷工",
    u"新界風雲",
    u"文革50年",
    u"巴拿馬文件",
    u"哲學來了",
    u"兒童新聞",
    u"創業青年",
    u"迷你倉火災",
    u"公民黑客",
    u"薩德事件",
    u"遊覽車起火",
    u"ChangeMaker",
    u"給家長的信",
    u"英國脫歐",
    u"母語專題",
    u"香港2047",
    u"藝術新星空",
    u"蔡英文新政",
    u"轉型正義",
    u"旺角騷亂",
    u"南海爭議",
    u"南臺大地震",
    u"小說連載",
    u"裏約奧運",
    u"華人參政",
    u"廢青系列",
    u"數洞",
    u"天津爆炸",
    u"習馬會",
    u"七十年代來時路",
    u"臺灣反課綱",
    u"起訴曾蔭權",
    u"緬甸大選",
    u"曼谷爆炸",
    u"習近平訪美",
    u"金馬獎",
    u"香港區議會選舉",
    u"施政報告",
    u"古巴系列",
    u"臺北書展",
    u"強人杜特地",
    u"奧蘭多槍擊",
    u"六中全會",
    u"伊斯蘭國",
    u"特首你好",
    u"彈劾朴槿惠",
    u"2016臺灣大選",
    u"特首參選人直播",
    u"明報風波",
    u"二戰70年",
    u"香港故宮風波",
    u"港珠澳大橋",
    u"共產主義爭論",
    u"家庭照相館",
    u"特首選戰",
    u"泰王逝世",
    u"蔡英文就職",
    u"2017奧斯卡",
    u"河套科技園",
    u"直播立法會",
    u"誰選立法會",
    u"2016美國大選",
    u"菲律賓大選",
    u"北韓時間",
    u"2016中國兩會",
    u"詩歌與衝突",
    u"運動創傷",
    u"綠茵場上",
    u"雄安手記",
    u"SOPA獲獎報導",
    u"劉霞獲釋",
    u"花蓮強震",
    u"民主牆風波",
    u"宣誓風波",
    u"川震十年",
    u"香港電影金像獎",
    u"年度專題",
    u"開放政府",
    u"十九大",
    u"加泰隆尼亞獨立",
    u"北京虐童案",
    u"劉曉波病逝",
    u"解嚴三十年",
    u"九七20年",
    u"一週精選",
    u"評論",
    u"記者手記",
    u"超執筆",
    u"疾病王國",
    u"生死無盡",
    u"總編周記",
    u"書評",
    u"影評",
    u"特約",
    u"科技",
    u"LifeStyle",
    u"澳門",
    u"黑鏡",
    u"朋丁藝廊",
    u"唱反調",
    u"職場觀察",
    u"懷疑一切",
    u"國際前線",
    u"唔該埋單",
    u"福爾摩沙",
    u"教育",
    u"動物公民",
    u"職業",
    u"社會",
    u"經濟",
    u"中國因素",
    u"圓桌禮儀",
    u"夜歸人",
    u"香江霧語",
    u"黑啤來聊聊",
    u"俄羅斯",
    u"五月風暴",
    u"土地大辯論",
    u"長春長生",
    u"疫苗",
    u"習氏修憲",
    u"浸大",
    u"兩湖遊記",
    u"金門賭場",
    u"諾貝爾文學獎",
    u"兩岸交流",
    u"金澤散步",
    u"揭開紅幕",
    u"讀者十論",
    u"中印對峙",
    u"療癒時代",
    u"週日讀書",
    u"金曲獎",
    u"一例一休",
    u"民主牆",
    u"六七暴動",
    u"假新聞",
    u"移民",
    u"緬甸轉型",
    u"澳門風災",
    u"文白之爭",
    u"德國大選",
    u"余光中逝世",
    u"一帶一路",
    u"女權主義",
    u"故事",
    u"計劃生育",
    u"香港研究",
    u"女權運動",
    u"伊朗",
    u"漩渦",
    u"斜槓青年",
    u"新冷戰",
    u"盧旺達",
    u"宜蘭列車",
    u"廣東話",
    u"難民",
    u"脫歐",
    u"中國",
    u"瑞典",
    u"改革",
    u"長榮班機",
    u"維冠大樓",
    u"奧巴馬",
    u"踏血尋梅",
    u"高雄",
    u"藝術",
    u"同性婚姻",
    u"香港黑幫",
    u"馬來西亞",
    u"全面審查",
    u"填海計劃",
    u"天鴿",
    u"時鐘酒店",
    u"躁鬱症",
    u"赫爾辛基",
    u"特內里費島",
    u"民主",
    u"天安門",
    u"空城",
    u"陸生共諜",
    u"禁書",
    u"地下鐵事件",
    u"即時新聞",
    u"體制外",
    u"翻牆",
    u"電影十年",
    u"珠穆朗瑪",
    u"ISIS",
    u"余光中難題",
    u"平壤",
    u"臺南震災",
    u"金融難民",
    u"旺角小龍女",
    u"基隆",
    u"柏林",
    u"同志",
    u"斯里蘭卡",
    u"極右",
    u"讀者來函",
    u"洪都拉斯",
    u"學術造假",
    u"北方的深圳",
    u"非正常死亡",
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
