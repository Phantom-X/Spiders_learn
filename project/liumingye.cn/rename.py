# -*-coding:utf-8-*-
"""
@project:Spiders
@Author: Phantom
@Time:2023/1/13 1:39
@开发环境：windows 10 + python3.8
@IDE：PyCharm2021.3.1
@Email: 2909981736@qq.com
"""
import os

over = '''若生命等候
刀剑若梦
连锁反应
浪子心声
不装饰你的梦
顺流逆流
难得有情人
堆积情感
痴心换情深
上海滩
等你等到我心痛
千千阕歌
最爱
英雄泪
我是一只小小鸟
童年
山丘
飞鸟与鱼
爱，很简单
有时候
想和你去吹吹风
Last
Dance
友情岁月
浮躁
Lemon
Tree
有心人
如果云知道
没有人知的故事
夏夜晚风
忘记你我做不到
天下有情人
当爱已成往事
暧昧
一千个伤心的理由
为情所困
恋曲2000
爱江山更爱美人
讲不出再见
难得有情人(国)
问
现在以后
爱你十分泪七分
梦中人
矜持
别怕我伤心
偷心
我期待
刀剑如梦
爱的故事(上)
执迷不悔(粤语版)
用心良苦
爱多一次痛多一次
爱如潮水
长路漫漫伴你闯
谢谢你的爱
明天我要嫁给你
来生缘
老情歌
如风往事
夏日倾情
飘雪
旧朋友
容易受伤的女人
孤单背影
雨季不再来
弯弯的月亮
雨中的恋人们
光辉岁月
钟爱一生
问情
忘情森巴舞
我悄悄蒙上你的眼睛
满分情人
一世情缘
今夜你会不会来
我用自己的方式爱你
漂洋过海来看你
明天你是否依然爱我
谁伴我闯荡
男儿当自强(国语)
凡人歌
是不是每一个恋爱的人都像我
让我欢喜让我忧
如没有你
一颗不变心
我是不是该安静的走开
疯了
每天爱你多一些
人在黎明
两个偶然
难舍难分
他
心的旅途
亲亲我的宝贝
芳华绝代乱世佳人(Lego
Version)
可否抱紧我
给您留念
谁明白爱
其实我还是有些在乎
共同渡过
夜未央
醉人的一晚
伤心的话留到明天再说
雨夜倾情
无名份的浪漫
伤尽我心的说话
冬季来的女人
卡拉永远OK
可不可以
季候风
我和我追逐的梦
爱恨缠绵
光辉岁月
敢爱敢做
堆积情感
滚滚红尘
失恋阵线联盟
最后的季节
珍重
一千零一夜
相逢在雨中
李香兰
如果你是我的传说
风再起时(粤)
月半小夜曲
你怎么舍得我难过
灰色轨迹
情人的眼泪
我和春天有个约会
心太软
你的眼睛背叛你的心
女人何苦为难女人
傻瓜
独角戏
珍重
情网
痴心换情深
当爱已成往事
倩女幽魂
玻璃之情
你看你看月亮的脸
原来只要共你活一天
回家
只要为我爱一天
多少柔情多少泪
黄色月亮
雪候鸟
广岛之恋
都是夜归人
那么爱你为什么
DEAR
JOHN
三万英尺
爱江山更爱美人
春夏秋冬
李香兰
半点心
我
红豆
吻别
朋友
伤痕
领悟
值得
友情岁月
爱与哀愁
对你爱不完
宝贝对不起
谁的眼泪在飞
我的未来不是梦
风中有朵雨做的云
最爱
忘记他
护花使者
海阔天空
一言难尽
别问我是谁
你把我灌醉
再回到从前
大约在冬季
我想有个家
新鸳鸯蝴蝶梦
每天爱你多一些
人生何处不相逢
冬季到台北来看雨
爱我的人和我爱的人
大地
情人
情书
慢慢
祈祷
胆小鬼
铿锵玫瑰
不再犹豫
沉默是金
男人的好
爱的代价
孤枕难眠(Live)
愚人码头
阳光总在风雨后
恋曲1990
怪你过份美丽
为你我受冷风吹
独家记忆
你最珍贵
囚鸟(国)
我有我天地
天才白痴梦
来生缘
友谊之光
爱如潮水
天下有情人
人生如此
滚滚红尘
初恋情人
梦醒时分
归来吧
亲密爱人(Live)
容易受伤的女人
天若有情
为你我受冷风吹
再见亦是泪
灰色轨迹
忘情冷雨夜
堆积情感
恋曲1980
情深海更深
爱就一个字
冬天里的一把火
故乡的云
胆小鬼
滚滚红尘
你怎么舍得我难过
让我欢喜让我忧
追梦人
人生何处不相逢
失恋
爱的传说
'''
overlist = over.split('\n')
overlist.remove('')
namelist = ['若生命等候', '刀剑若梦', '连锁反应', '真的爱你', '浪子心声', '不装饰你的梦', '顺流逆流', '难得有情人', '堆积情感', '痴心换情深', '谁明浪子心', '上海滩',
            '等你等到我心痛', '千千阕歌', '最爱', '英雄泪', '我是一只小小鸟', '童年', '山丘', '飞鸟与鱼', '跟着感觉走', '爱，很简单', '有时候', '爱的呼唤', '铁血丹心',
            '想和你去吹吹风', '你快乐所以我快乐', 'Last Dance', '友情岁月', '浮躁', 'Lemon Tree', '掌心', '哭个痛快', '有心人', '如果云知道', '囚鸟',
            '没有人知的故事', '挪威的森林', '曲终人散', '夏夜晚风', '夜太黑', '忘记你我做不到', '为爱痴狂', '恋恋风尘', '红颜知己', '天下有情人', '当爱已成往事', '爱一回伤一回',
            '暧昧', '一千个伤心的理由', '十七岁的雨季', '为情所困', '恋曲2000', '爱江山更爱美人', '讲不出再见', '难得有情人(国)', '我不该看你的眼神', '问', '现在以后',
            '浪人情歌', '爱你十分泪七分', '太傻', '梦中人', '游戏人间', '味道', '矜持', '别怕我伤心', '偷心', '我期待', '刀剑如梦', '爱的故事(上)', '执迷不悔 (粤语版)',
            '用心良苦', '爱多一次痛多一次', '爱如潮水', '长路漫漫伴你闯', '谢谢你的爱', '明天我要嫁给你', '来生缘', '牵手', '老情歌', '如风往事', '夏日倾情', '飘雪', '旧朋友',
            '遥望', '容易受伤的女人', '孤单背影', '雨季不再来', '弯弯的月亮', '雨中的恋人们', '光辉岁月', '钟爱一生', '问情', '忘情森巴舞', '我悄悄蒙上你的眼睛', '满分情人',
            '一世情缘', '今夜你会不会来', '我用自己的方式爱你', '潇洒走一回', '漂洋过海来看你', '明天你是否依然爱我', '谁伴我闯荡', '一无所有', '男儿当自强 (国语)', '凡人歌',
            '一生心碎', '是不是每一个恋爱的人都像我', '让我欢喜让我忧', '如没有你', '一颗不变心', '为了爱 梦一生', '我是不是该安静的走开', '疯了', '每天爱你多一些', '人在黎明',
            '两个偶然', '别让明天的太阳离开我', '难舍难分', '他', '心的旅途', '似曾相识', '亲亲我的宝贝', '芳华绝代乱世佳人 (Lego Version)', '可否抱紧我', '给您留念',
            '谁明白爱', '其实我还是有些在乎', '共同渡过', '让爱自由', '夜未央', '醉人的一晚', '伤心的话留到明天再说', '雨夜倾情', '无名份的浪漫', '世外桃源', '伤尽我心的说话',
            '冬季来的女人', '卡拉永远OK', '可不可以', '季候风', '我和我追逐的梦', '爱恨缠绵', '光辉岁月', '敢爱敢做', '一生守候', '堆积情感', '滚滚红尘', '失恋阵线联盟',
            '最后的季节', '真的汉子', '珍重', '一千零一夜', '相逢在雨中', '李香兰', '如果你是我的传说', '风再起时(粤)', '月半小夜曲', '你怎么舍得我难过', '灰色轨迹', '哭砂',
            '情人的眼泪', '流浪的心', '我和春天有个约会', '相思无用', '心太软', '你的眼睛背叛你的心', '女人何苦为难女人', '傻瓜', '独角戏', '珍重', '情网', '痴心换情深',
            '当爱已成往事', '倩女幽魂', '玻璃之情', '一天到晚游泳的鱼', '你看你看月亮的脸', '约定', '女人花', '原来只要共你活一天', '短发', '回家', '只要为我爱一天',
            '多少柔情多少泪', '黄色月亮', '雪候鸟', '广岛之恋', '都是夜归人', '一生爱你千百回', '电台情歌', '那么爱你为什么', '白鸽', 'DEAR JOHN', '三万英尺', '中意他',
            '百年孤寂', '爱江山更爱美人', '春夏秋冬', '李香兰', '半点心', '我', '渡口', '大海', '红豆', '吻别', '水手', '朋友', '太傻', '伤痕', '领悟', '值得',
            '友情岁月', '爱与哀愁', '对你爱不完', '宝贝对不起', '谁的眼泪在飞', '我的未来不是梦', '风中有朵雨做的云', '最爱', '忘记他', '护花使者', '朋友别哭', '新不了情',
            '海阔天空', '一言难尽', '别问我是谁', '你把我灌醉', '再回到从前', '大约在冬季', '我想有个家', '新鸳鸯蝴蝶梦', '每天爱你多一些', '人生何处不相逢', '冬季到台北来看雨',
            '只要你过得比我好', '爱我的人和我爱的人', '大地', '情人', '情书', '慢慢', '祈祷', '胆小鬼', '铿锵玫瑰', '不再犹豫', '沉默是金', '他不爱我', '男人的好',
            '爱的代价', '孤枕难眠 (Live)', '愚人码头', '阳光总在风雨后', '恋曲1990', '怪你过份美丽', '新不了情', '为你我受冷风吹', '爱上一个不回家的人', '独家记忆',
            '你最珍贵', '囚鸟(国)', '一生所爱', '你是我胸口永远的痛', '我有我天地', '天才白痴梦', '来生缘', '星星点灯', '单身情歌', '友谊之光', '爱如潮水',
            "春夏秋冬 A Balloon's Journey", '天下有情人', '当我眼前只有你', '人生如此', '滚滚红尘', '初恋情人', '梦醒时分', '归来吧', '亲密爱人(Live)',
            '容易受伤的女人', '天若有情', '为你我受冷风吹', '再见亦是泪', '灰色轨迹', '忘情冷雨夜', '堆积情感', '恋曲1980', '情深海更深', '爱就一个字', '冬天里的一把火',
            '故乡的云', '爱我别走', '胆小鬼', '雨一直下', '秋去秋来', '祝你一路顺风', '滚滚红尘', '你怎么舍得我难过', '最浪漫的事', '神话·情话', '让我欢喜让我忧', '伤心太平洋',
            '追梦人', '漫步人生路', '人生何处不相逢', '失恋', '爱的传说']

notoverlist = list(set(namelist) - set(overlist))
notoverlist.remove("春夏秋冬 A Balloon's Journey")
print(len(notoverlist))

sortlist = [''] * 307
for n in notoverlist:
    sortlist[namelist.index(n)] = n

sl = []
for s in sortlist:
    if s != '':
        sl.append(s)
print(sl)
path = './华语金曲千禧年前'
for i in range(74):
    os.renames(os.path.join(path, f'{i+1}.mp3'), os.path.join(path, f'{sl[i]}.mp3'))



# ['https://m704.music.126.net/20230113030527/cad5782b140e6a05120973c0f4b55e81/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/19616652038/03f6/f765/c083/63e4e676d7a4aa8c84cc1f13c2ac3f9c.mp3?_authSecret=00000185a7488c6f1ea70aaba3af23ee', 'https://m804.music.126.net/20230113030533/b846b41325b0342cb31d86f90da1edc8/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17283468785/30ec/7b12/7041/2f562b601ae874bdd2d5d4cecf61d826.mp3?_authSecret=00000185a748a4540ead0aaba5431095', 'https://m804.music.126.net/20230113030540/f54d3fa0827516e4a891030a69ab5f02/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/23846502165/7922/ea9d/e152/62876d4a7a9bef204af2f3c470d2688e.mp3?_authSecret=00000185a748bceb12c60aa463691e9b', 'https://m704.music.126.net/20230113030546/a5449e90932e5daccb3947cded5f3c3d/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17169859479/266c/1adb/7d77/edc7517f0b03a1af280112f267687599.mp3?_authSecret=00000185a748d5aa12750aa4637480dd', 'https://m10.music.126.net/20230113030552/0957a7ed2a6e4574b181339b64e36a50/ymusic/9872/6e9c/952b/0f0f80c6f69ff2075db2e6d37d3bba70.mp3', 'https://m10.music.126.net/20230113030559/ea48286f769c6bd72a039b28c81b8271/ymusic/5506/bd45/84ac/179851d7d370c4b0f0b080790ce772eb.mp3', 'https://m10.music.126.net/20230113030605/6aa5a17a2b237b4bd21965e878ce253d/ymusic/555b/045c/050e/b1d43894ee36db9882f22d08ffb907c6.mp3', 'https://m10.music.126.net/20230113030611/28d72c1e1584c1ca31ccb6d336c66705/ymusic/27c4/2499/9531/1fe8e669025814281c96a431236c9175.mp3', 'https://m10.music.126.net/20230113030618/104940075ba62dd01d55d84e686462a8/ymusic/555e/025c/555a/b4be9b171f564e8d5d97b01961c3d069.mp3', 'https://m10.music.126.net/20230113030624/3ecc592b5b71db1767459a9066740592/ymusic/308e/fa22/b88f/f70490f17f6b8eeaf37be7d1c7b32b36.mp3', 'https://m704.music.126.net/20230113030631/43d3b70a662b29e887837fcf5123da35/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17316277076/aee9/0295/6a66/4005297e97857efbe436077eee47683d.mp3?_authSecret=00000185a74983951e150aaba39bd046', 'https://m10.music.126.net/20230113030635/e98118e659a8c5092f044dd574b1891f/ymusic/525b/525e/0e58/e14ac6b79fe4436c5b4192b58cc720bc.mp3', 'https://m10.music.126.net/20230113030643/77beb2526c2eb5696b9139aa2e1c0c78/ymusic/e776/fa7c/062c/e8e2f284623a926ee17daea430ea16e4.mp3', 'https://m10.music.126.net/20230113030650/c681000353e881ebf43946d19033887f/ymusic/515f/0553/070f/f523f3aad8296bfbf3de0e369bb51d45.mp3', 'https://m10.music.126.net/20230113030656/9026400d6443166729a7740e91f51405/ymusic/1f30/fe7d/fcab/43af52e4cb880e04143b5450843592b3.mp3', 'https://m804.music.126.net/20230113030702/b0d77abd257513d5ecddcbd12871646b/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/12786994645/3e13/6618/0483/96602014da35342690f6ca8a2cc4a8fc.mp3?_authSecret=00000185a749ff9115ef0aaba0a00a3a', 'https://m10.music.126.net/20230113030709/8bfb46a67bff4dd2532b60741f96487a/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3061282878/7ad7/286e/d050/afd80b773eb0afc2c6248e56f142b5bf.mp3', 'https://m704.music.126.net/20230113030715/58ebfa197640b0add85c3017b7bb5476/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17287932604/d38c/287c/c7a9/c1e954b9a3d112b6c512dc3482de8767.mp3?_authSecret=00000185a74a3125101a0aaba51d15b9', 'https://m704.music.126.net/20230113030721/410e0ce732bbfad5e8d9e9f36d1d7d81/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/11839860077/ca27/7d4a/7be0/4457c55884388249743ae7eed23d072f.mp3?_authSecret=00000185a74a49fc031e0aaba0852184', 'https://m804.music.126.net/20230113030728/513d535195f68105eb99255775014d3e/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18758510032/01da/6356/e347/f61764b55460682b1bbf6d0b6206539a.mp3?_authSecret=00000185a74a62af0b9a0aaba0d74561', 'https://m10.music.126.net/20230113030734/87a6f9baeb199c847657e5a20ba307b7/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3036134625/9857/9655/3eb6/8c6360998025caf8e20010615d22a118.mp3', 'https://m704.music.126.net/20230113030740/d707f1d71dfc952d4ee7192c07d5bda8/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18737168557/c195/3227/007f/7290c0061116b7f2b42ddbeb9fc145b8.mp3?_authSecret=00000185a74a94571e430aaba04491b2', 'https://m704.music.126.net/20230113030747/70ee78e983c60fe82f20127f10d45309/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14798404224/cfc6/8e0f/1b67/bbd7cb3ffe4cb89ffec06dc19089f49b.mp3?_authSecret=00000185a74aad231b770aaba51602c1', 'https://m10.music.126.net/20230113030753/66781cf2da91b3fbb561ce8f7ab4408a/ymusic/d3d5/07bf/a5c3/f002133594a260a9cc77c89efeddd58e.mp3', 'https://m10.music.126.net/20230113030759/75569182ceeedb62f24c3800f9f1e0f7/ymusic/ed97/62f7/a71e/9eae2b6850c6ec4f0ee25531642e0056.mp3', 'https://m704.music.126.net/20230113030806/b87dd091738194dc4900a362aca463b1/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/19117824577/dc91/77d2/968b/43f6412729fcd8e444d988d27a92618f.mp3?_authSecret=00000185a74af78910660aaba3b61f48', 'https://m10.music.126.net/20230113030812/a8e5b43d21825c042902933076f6fbf0/ymusic/555c/0559/0658/b6f01d5dd123fbb0a70d12678afd3b9e.mp3', 'https://m704.music.126.net/20230113030818/36bcacbf9629055bfc2c4f34ae3a6aff/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17202167367/0411/5cb7/5262/f1c8ea7f442a60457ae737a52a82e3b5.mp3?_authSecret=00000185a74b293e17390aaba54c1049', 'https://m704.music.126.net/20230113030825/375322baf736ed74bfc11e68808c9cef/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8677441683/cf01/1b17/56ad/5f05c8c17997eca7ed9af5ff63294362.mp3?_authSecret=00000185a74b42400c8f0aaba02afd25', 'https://m704.music.126.net/20230113030831/51ec3b83f9ece991a4f37a5c9298f55a/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/10741155383/db2f/84bd/3c54/e8f2feb1bb1455b09659727ca1c17dbd.mp3?_authSecret=00000185a74b5aae03a70aaba0452433', 'https://m704.music.126.net/20230113030838/b569ab4cb5ce05820e7bcbeda4765c37/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17311525412/65ae/387b/d07b/895eb4cdb4dab93bf406432b4191c1f4.mp3?_authSecret=00000185a74b739703cd0aaba39336cd', 'https://m704.music.126.net/20230113030844/100deebfca9eefbcecd6d2f719e7a91f/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18725030957/c6e5/db1d/b36b/a3fc313d8dc6aca854fdc6f8e808e631.mp3?_authSecret=00000185a74b8c4c1cd70aa460a5d833', 'https://m804.music.126.net/20230113030850/b42d8430ee04d5bda2fcc8e2d0dca1ec/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18712603866/f0d9/4656/3ff7/ceeb8418118f8d109c12f63787f1d1ab.mp3?_authSecret=00000185a74ba51909410aaba04b1526', 'https://m10.music.126.net/20230113030857/f7f93713009394723c24f48e3034c8ca/ymusic/df13/a6d9/d479/e47943179aaa145b1b9fe3c6b609ed5d.mp3', 'https://m704.music.126.net/20230113030903/66f9859b0fe3e90c023d7434f052025f/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/19892173702/8b28/b76e/975f/4dffbca86a6d246ea8453d785bd5c0d5.mp3?_authSecret=00000185a74bd75809760aaba08ae736', 'https://m704.music.126.net/20230113030909/310237e99e6388e08da90b4895b30397/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17229530483/837b/06fc/c509/03330fb84a03c4effbcfcd6c9435697d.mp3?_authSecret=00000185a74befd81c6f0ac9de4416d7', 'https://m10.music.126.net/20230113030916/7734f054fda569a4f4d5eca65474ff48/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3066945171/6f85/b110/719e/3bb192e5146aebb9651b5cbf03ff98d7.mp3', 'https://m10.music.126.net/20230113030922/b6da7d313db909f652d3d59d9f344be3/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3066419155/c2e0/b9a6/5736/fd94cfbfd886ad2d187c640b7d6611a9.mp3', 'https://m804.music.126.net/20230113030928/8f86805204adf745daeddeda4ff5c23d/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17202234501/a2eb/b83d/c78d/75bc3b39d62fe115650b1be0b910a46d.mp3?_authSecret=00000185a74c3a190a550aaba5fe188a', 'https://m704.music.126.net/20230113030935/cb1863019b2d5b77dead698caeae54c0/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17229428547/d04c/a890/8269/471292962e77af6bbd8b66ea5264fd15.mp3?_authSecret=00000185a74c52b809c20aa4636514f5', 'https://m704.music.126.net/20230113030941/3e1f8905db5279491045d13d16e80842/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18753569212/5515/5da9/e638/f6e13a113b22dd1cbacdcd675415810e.mp3?_authSecret=00000185a74c6ba61f1b0aaba60d4c40', 'https://m704.music.126.net/20230113030947/53cc64f87c22dee3c90da9a02a1172fc/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17174812126/61b6/5a2f/db70/60161f09f59360b2a6e869cece15c55d.mp3?_authSecret=00000185a74c84480ab60aa460b41964', 'https://m10.music.126.net/20230113030954/6ff329af09f88126bbce46c816e74f91/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3036119614/c76e/93ff/2c08/02c176cf171b64208873e177a9b27d6e.mp3', 'https://m10.music.126.net/20230113031000/251e6bfd259a399fb5713d5e8e4ba6aa/ymusic/da89/3828/22e7/366128eb09a402d1f446634a73edc1ea.mp3', 'https://m10.music.126.net/20230113031006/aa3e15c0b45f054fef0cbee94ce1bc22/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3035955061/d7b6/e4cc/b3f7/b3702e249648b8a33c03793c6575d576.mp3', 'https://m10.music.126.net/20230113031013/15504ab7f35e3b4dc88417fd0cea27b9/ymusic/290a/b2fd/c42f/0e7c353ad717249158f3eccbabce28d2.mp3', 'https://m10.music.126.net/20230113030849/a5be33832e64b50ea13b3b9c2bb218e6/ymusic/c2bc/48d6/9d33/68be595e81d2c0ec52a8afec4f0f1f00.mp3', 'https://m10.music.126.net/20230113031032/e5dead1aed9bff09b8322b9a349cbec0/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3036087023/5709/03c1/ce39/c6a3199884995548b4f1f0a086a746c1.mp3', 'https://m804.music.126.net/20230113031038/fce87c776bd6ed884f08e30a53095b32/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096468467/d944/d51b/af6f/e8568808075dddbdef79707f2d8d67d1.mp3?_authSecret=00000185a74d4a811ae80aaba24623ef', 'https://m10.music.126.net/20230113031044/0af7b81f19448422ebc531733d37656c/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3058605824/1f79/55ca/9c80/b70fed664552414ec29456ea8e93963c.mp3', 'https://m10.music.126.net/20230113031051/d062724c9d7e1b54e9eca4be8bc4be82/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/13270168804/52e6/91a4/99f4/c381bed386f872e1e0d1abde18db3228.mp3', 'https://m804.music.126.net/20230113031057/20f466bdaa95999774dbe5a14b04151a/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18210636209/a7af/6950/834d/e2799befe91c814576f1a3ccf081f92c.mp3?_authSecret=00000185a74d94de0aad0aaba0d74561', 'https://m704.music.126.net/20230113031103/fa146f92990e5f10a9ce76a5f5a15fbd/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18742261055/6034/b7c5/f383/cab62734e20441b56cc8825f8939848b.mp3?_authSecret=00000185a74dad9810b80aaba06a3263', 'https://m10.music.126.net/20230113030649/48911862e3b62cc464e92fdacf657d61/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/2976572409/0708/4ef6/2e53/d552990a46a08e26dd035b04eebf5735.mp3', 'https://m804.music.126.net/20230113031116/040e2b87b2a565e38a7a7178ca932d68/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/22260004391/d109/3dbc/8cbc/b61c50eb5170e4a3276f3e6e5981629f.mp3?_authSecret=00000185a74ddf79011f0aaba02ce3d4', 'https://m704.music.126.net/20230113031123/904418214f15b48fbe08d230edf77069/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/17288363845/29f6/2f37/88c9/da3a386ef2192c93f36cce0e67dbdfe8.mp3?_authSecret=00000185a74df85717b00aaba3980913', 'https://m10.music.126.net/20230113031129/466626f7d2b6af53db4abd5945672988/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3066077335/9399/38b6/2c39/60c6bd186221d0fb14a531da1bbb3768.mp3', 'https://m10.music.126.net/20230113031135/57bf3675c53e1fbbeafb1f3eb49d216f/ymusic/6a3d/6a52/72b6/5c864559b979cf69c97a348e2d0951b5.mp3', 'https://m10.music.126.net/20230113031142/9976fe5da75da0530bdb7c40d2c17076/ymusic/ea90/8d8d/d05c/c7d1f9995e2e89b8d52759d1f256ba96.mp3', 'https://m10.music.126.net/20230113031148/37f3c6ed07299c2d38d75ebd38b5b79c/ymusic/020f/0f5e/010b/5eb3485f6d8418f99c2f6a43e462601f.mp3', 'https://m10.music.126.net/20230113030820/a14c8e473bb40532db16e1e392440577/ymusic/f3ff/c986/b8d0/d1fa6434c538c951bc55057b30bfbc48.mp3', 'https://m704.music.126.net/20230113031201/c3be23bf311f93df8457e39ac29b23ce/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14322078568/535f/d994/bf40/d096b962ca38c40884f6468b6be0f43a.mp3?_authSecret=00000185a74e8d6407a30aaba361daf6', 'https://m804.music.126.net/20230113031207/9762f0a45ed094670589c54497f355ae/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096586393/4a1f/ec2a/778e/2400139667369d50b60b79bd0cd95fd0.mp3?_authSecret=00000185a74ea6250fda0aa46362264a', 'https://m704.music.126.net/20230113031213/b034e27f0512346b60190fd500d52294/jdymusic/obj/w5zDlMODwrDDiGjCn8Ky/1559600209/2c76/d2f3/dace/06b67241b897d898d7881dff57a24a80.mp3?_authSecret=00000185a74ebec21dc60aaba04a24db', 'https://m704.music.126.net/20230113031220/260bdd8db399dafeebab73823606f8bd/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/18742268944/1074/80b2/a8d3/c5aa5adac820a64814fd24ef16a6b8d1.mp3?_authSecret=00000185a74ed7a819670aaba0cb107d', 'https://m804.music.126.net/20230113031226/b4e47f7c30c456996e0da3113b4ec1de/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/11839848562/61a6/036f/99e2/07ce85eb5c1bf4dcd01d6f97f8468c8b.mp3?_authSecret=00000185a74ef05c18c80aaba55a1a6b', 'https://m10.music.126.net/20230113031232/54a2c4e359626e0f2da8f7b290dfba57/ymusic/045b/5358/0609/3169e4db1fd275ecb2c81c52a000700d.mp3', 'https://m10.music.126.net/20230113031239/5d23e543de96ee5faabd611c5e088c38/ymusic/d9d9/f30a/76ed/673c763cf6c61d272a9c1bdc29c09a6b.mp3', 'https://m10.music.126.net/20230113031245/ab1a67ed585e6380f5cfbbbf7b07be1a/ymusic/e814/b921/1559/03409720f9ca3f7da89b85f7151eff5a.mp3', 'https://m10.music.126.net/20230113031257/c285d4e5dab7c0adef36b338dc9e61c9/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3178907702/3fe7/d9b7/8e3e/c34add8d7e6b62b7bac287294d0a9738.mp3', 'https://m10.music.126.net/20230113031304/57e7b9df28a628d28a6a9a6c19dfe78d/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3057180350/88cd/36ee/fc2a/b68d31372f636acc1dd3b68f983df746.mp3', 'https://m10.music.126.net/20230113031311/6b6f16c2b9760920020768632d0a56ef/ymusic/0c00/8787/8311/755e688f0252f69779db5b83d3bba599.mp3', 'https://m10.music.126.net/20230113031317/2821c0e5b9e72b2a5de6c7d5384ac561/ymusic/df5b/c80b/f372/89527f05cf117e343dde8eb9796fa301.mp3', 'https://m804.music.126.net/20230113031323/3bc416b7abd2fc4ad99def621a2be663/jdymusic/obj/w5zDlMODwrDDiGjCn8Ky/1918459522/17d2/7b32/48d2/43c1b2b4688275d85d800ab1e4921b49.mp3?_authSecret=00000185a74fcf84150e0aaba43c10b9']