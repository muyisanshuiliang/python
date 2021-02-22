#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Test.py    
@Contact :   muyisanshuiliang@hotmail.com

@Modify Time      @Author               @Version    
------------      -------               --------    
2021/2/6 14:05   muyisanshuiliang      3.9   
@Desciption:
---------------------------------------------------------------     
'''

# import lib
import json

data = """653022100000	阿克陶镇
653022101000	奥依塔克镇
653022200000	玉麦乡
653022201000	皮拉勒乡
653022202000	巴仁乡
653022203000	喀热开其克乡
653022204000	加马铁热克乡
653022205000	木吉乡
653022206000	布伦口乡
653022207000	克孜勒陶乡
653022208000	恰尔隆乡
653022210000	塔尔塔吉克民族乡
653022400000	托尔塔依农场
653022401000	阿克达拉牧场
653022402000	原种场
653022403000	克孜勒苏柯尔克孜自治州林场
653022404000	苗圃
653023100000	阿合奇镇
653023200000	库兰萨日克乡
653023201000	色帕巴依乡
653023202000	苏木塔什乡
653023203000	哈拉奇乡
653023204000	哈拉布拉克乡
653024100000	乌恰镇
653024101000	康苏镇
653024200000	乌鲁克恰提乡
653024201000	吾合沙鲁乡
653024202000	膘尔托阔依乡
653024203000	黑孜苇乡
653024204000	托云乡
653024205000	铁列克乡
653024206000	巴音库鲁提乡
653024207000	波斯坦铁列克乡
653024208000	吉根乡
653024501000	兵团托云牧场
653101001000	恰萨街道
653101002000	亚瓦格街道
653101003000	吾斯塘博依街道
653101004000	库木代尔瓦扎街道
653101005000	西域大道街道
653101006000	东湖街道
653101007000	迎宾大道街道
653101008000	西公园街道
653101100000	乃则尔巴格镇
653101101000	夏马勒巴格镇
653101202000	多来特巴格乡
653101203000	浩罕乡
653101204000	色满乡
653101205000	荒地乡
653101206000	帕哈太克里乡
653101207000	伯什克然木乡
653101208000	阿瓦提乡
653101209000	英吾斯坦乡
653101210000	阿克喀什乡
653121100000	托克扎克镇
653121101000	兰干镇
653121102000	吾库萨克镇
653121103000	乌帕尔镇
653121201000	塔什米里克乡
653121202000	铁日木乡
653121203000	布拉克苏乡
653121204000	萨依巴格乡
653121205000	站敏乡
653121211000	木什乡
653121400000	县种畜场
653121401000	县园艺场
653121402000	县林场
653121403000	县良种场
653121406000	疏附广州工业城
653122100000	疏勒镇
653122101000	罕南力克镇
653122102000	牙甫泉镇
653122200000	巴仁乡
653122201000	洋大曼乡
653122202000	亚曼牙乡
653122203000	巴合齐乡
653122204000	塔孜洪乡
653122205000	英尔力克乡
653122206000	库木西力克乡
653122207000	塔尕尔其乡
653122208000	艾尔木东乡
653122209000	阿拉力乡
653122210000	阿拉甫乡
653122211000	英阿瓦提乡
653122400000	高新技术产业孵化园区管委会
653123100000	英吉沙镇
653123101000	乌恰镇
653123102000	芒辛镇
653123103000	萨罕镇
653123200000	城关乡
653123201000	乔勒潘乡
653123202000	龙甫乡
653123204000	色提力乡
653123206000	英也尔乡
653123207000	克孜勒乡
653123208000	托普鲁克乡
653123209000	苏盖提乡
653123211000	艾古斯乡
653123212000	依格孜也尔乡
653123401000	英吉沙工业园区
653123500000	兵团东风农场
653124100000	泽普镇
653124101000	奎依巴格镇
653124200000	波斯喀木乡
653124201000	泽普县依玛乡
653124202000	古勒巴格乡
653124203000	赛力乡
653124204000	依肯苏乡
653124205000	图呼其乡
653124206000	奎依巴格乡
653124207000	阿克塔木乡
653124208000	阿依库勒乡
653124209000	布依鲁克塔吉克族乡
653124210000	桐安乡
653124401000	泽普县良种场
653124403000	国营林场
653125001000	叶尓羌街道
653125002000	城中街道
653125003000	城东街道
653125004000	城西街道
653125005000	城北街道
653125100000	莎车镇
653125101000	恰热克镇
653125102000	艾力西湖镇
653125103000	荒地镇
653125104000	阿瓦提镇
653125105000	白什坎特镇
653125106000	依盖尔其镇
653125107000	古勒巴格镇
653125108000	米夏镇
653125109000	托木吾斯塘镇
653125110000	塔尕尔其镇
653125111000	乌达力克镇
653125112000	阿拉买提镇
653125113000	阿扎特巴格镇
653125201000	阿热勒乡
653125202000	恰尔巴格乡
653125204000	英吾斯塘乡
653125206000	阿尔斯兰巴格乡
653125207000	孜热甫夏提塔吉克族乡
653125208000	亚喀艾日克乡
653125209000	喀群乡
653125210000	霍什拉甫乡
653125211000	达木斯乡
653125213000	伊什库力乡
653125214000	拍克其乡
653125216000	阔什艾日克乡
653125217000	墩巴格乡
653125220000	巴格阿瓦提乡
653125221000	喀拉苏乡
653125401000	喀什监狱
653125402000	莎车县良种繁育场
653125403000	莎车县第一林场（国营苗圃）
653125404000	莎车县国营二林场
653125405000	莎车县园艺场
653125406000	莎车县蚕种场
653125407000	莎车县鱼苗场
653125408000	农科院莎车农业试验站
653125409000	工业园区管委会
653125410000	英阿瓦提管理委员会
653125411000	永安管理委员会
653126100000	喀格勒克镇
653126101000	恰尔巴格镇
653126102000	乌夏巴什镇
653126103000	阿克塔什镇
653126200000	洛克乡
653126201000	伯西热克乡
653126202000	铁提乡
653126203000	恰萨美其特乡
653126204000	吐古其乡
653126205000	江格勒斯乡
653126206000	加依提勒克乡
653126207000	巴仁乡
653126208000	乌吉热克乡
653126209000	夏合甫乡
653126210000	依力克其乡
653126211000	依提木孔乡
653126212000	宗朗乡
653126213000	柯克亚乡
653126214000	西合休乡
653126215000	棋盘乡
653126216000	萨依巴格乡
653126402000	阿克塔什农场
653126403000	良种场
653126405000	林场
653126409000	叶城工业园区
653126500000	兵团叶城牧场
653127100000	麦盖提镇
653127101000	巴扎结米镇
653127201000	希依提墩乡
653127202000	央塔克乡
653127203000	吐曼塔勒乡
653127204000	尕孜库勒乡
653127205000	克孜勒阿瓦提乡
653127206000	库木库萨尔乡
653127207000	昂格特勒克乡
653127208000	库尔玛乡
653127400000	胡杨林场
653127401000	园艺场
653127402000	五一林场
653128100000	岳普湖镇
653128101000	艾西曼镇
653128102000	铁热木镇
653128103000	也克先拜巴扎镇
653128200000	岳普湖乡
653128203000	阿其克乡
653128204000	色也克乡
653128206000	巴依阿瓦提乡
653128207000	阿洪鲁库木乡
653128402000	岳普湖县奶牛场
653129100000	巴仁镇
653129101000	西克尔库勒镇
653129102000	夏普吐勒镇
653129103000	卧里托格拉克镇
653129104000	克孜勒博依镇
653129107000	和夏阿瓦提镇
653129200000	铁日木乡
653129201000	英买里乡
653129202000	江巴孜乡
653129205000	米夏乡
653129208000	克孜勒苏乡
653129209000	古勒鲁克乡
653129210000	玉代克力克乡
653130100000	巴楚镇
653130101000	色力布亚镇
653130102000	阿瓦提镇
653130103000	三岔口镇
653130200000	恰尔巴格乡
653130201000	多来提巴格乡
653130202000	阿纳库勒乡
653130203000	夏马勒乡
653130204000	阿克萨克玛热勒乡
653130205000	阿拉根乡
653130206000	琼库恰克乡
653130207000	英吾斯坦乡
653131100000	塔什库尔干镇
653131101000	塔吉克阿巴提镇
653131200000	塔什库尔干乡
653131201000	塔合曼乡
653131202000	科克亚尔柯尔克孜族乡
653131203000	提孜那甫乡
653131204000	达布达尔乡
653131205000	马尔洋乡
653131206000	瓦恰乡
653131207000	班迪尔乡
653131208000	库科西鲁格乡
653131210000	大同乡
653201001000	努尔巴格街道
653201002000	古江巴格街道
653201003000	古勒巴格街道
653201004000	纳尔巴格街道
653201100000	拉斯奎镇
653201101000	玉龙喀什镇
653201102000	吐沙拉镇
653201200000	肖尔巴格乡
653201201000	伊里其乡
653201202000	古江巴格乡
653201204000	吉亚乡
653201205000	阿克恰勒乡
653201401000	北京工业园区
653201402000	和田市京和物流园区
653221100000	巴格其镇
653221102000	罕艾日克镇
653221202000	英阿瓦提乡
653221203000	英艾日克乡
653221204000	布扎克乡
653221205000	拉依喀乡
653221206000	朗如乡
653221207000	塔瓦库勒乡
653221208000	伊斯拉木阿瓦提乡
653221209000	色格孜库勒乡
653221210000	喀什塔什乡
653221211000	吾宗肖乡
653221401000	和田县经济新区
653222100000	喀拉喀什镇
653222101000	扎瓦镇
653222102000	奎牙镇
653222103000	喀尔赛镇
653222104000	普恰克其镇
653222203000	阿克萨拉依乡
653222204000	乌尔其乡
653222205000	托胡拉乡
653222206000	萨依巴格乡
653222207000	加汗巴格乡
653222209000	芒来乡
653222210000	阔依其乡
653222211000	雅瓦乡
653222212000	吐外特乡
653222213000	英也尔乡
653222214000	喀瓦克乡
653223001000	街道
653223100000	固玛镇
653223101000	杜瓦镇
653223102000	赛图拉镇
653223103000	木吉镇
653223104000	阔什塔格镇
653223105000	桑株镇
653223201000	克里阳乡
653223202000	科克铁热克乡
653223205000	乔达乡
653223206000	木奎拉乡
653223207000	藏桂乡
653223208000	皮亚勒玛乡
653223209000	皮西那乡
653223210000	巴什兰干乡
653223211000	垴阿巴提塔吉克民族乡
653223212000	康克尔柯尔克孜民族乡
653223401000	皮山三峡工业园区
653224001000	城区街道
653224100000	洛浦镇
653224101000	山普鲁镇
653224102000	杭桂镇
653224201000	布亚乡
653224203000	恰尔巴格乡
653224205000	多鲁乡
653224206000	纳瓦乡
653224207000	拜什托格拉克乡
653224208000	阿其克乡
653224403000	洛浦县北京工业园区
653225100000	策勒镇
653225101000	固拉合玛镇
653225200000	策勒乡
653225202000	达玛沟乡
653225203000	恰哈乡
653225204000	乌鲁克萨依乡
653225205000	奴尔乡
653225206000	博斯坦乡
653226100000	木尕拉镇
653226101000	先拜巴扎镇
653226200000	加依乡
653226201000	科克亚乡
653226202000	阿热勒乡
653226203000	阿日希乡
653226204000	兰干乡
653226205000	斯也克乡
653226206000	托格日尕孜乡
653226207000	喀拉克尔乡
653226208000	奥依托格拉克乡
653226209000	阿羌乡
653226210000	英巴格乡
653226211000	希吾勒乡
653226212000	达里雅布依乡
653226402000	于田监狱
653227100000	尼雅镇
653227200000	尼雅乡
653227201000	若克雅乡
653227202000	萨勒吾则克乡
653227203000	叶亦克乡
653227204000	安迪尔乡
653227205000	亚瓦通古孜乡
654002001000	萨依布依街道
654002002000	墩买里街道
654002003000	伊犁河路街道
654002004000	喀赞其街道
654002005000	都来提巴格街道
654002006000	琼科瑞克街道
654002007000	艾兰木巴格街道
654002008000	解放路街道
654002100000	巴彦岱镇
654002101000	潘津镇
654002102000	英也尔镇
654002103000	达达木图镇
654002201000	汉宾乡
654002202000	塔什科瑞克乡
654002203000	喀尔墩乡
654002204000	托格拉克乡
654002205000	克伯克于孜乡
654002403000	伊宁市边境经济合作区
654002404000	伊犁河南岸新区
654003001000	团结路街道
654003002000	乌东路街道
654003003000	北京路街道
654003004000	乌鲁木齐西路街道
654003005000	火车站街道
654003201000	开干齐乡
654003508000	兵团一三一团
654003510000	天北新区
654004001000	卡拉苏街道
654004002000	亚欧东路街道
654004003000	亚欧西路街道
654004004000	工业园区街道
654004200000	伊车嘎善乡
654004505000	兵团六十一团
654004506000	兵团六十二团
654021100000	吉里于孜镇
654021101000	墩麻扎镇
654021102000	英塔木镇
654021103000	胡地于孜镇
654021104000	巴依托海镇
654021105000	阿热吾斯塘镇
654021106000	萨木于孜镇
654021107000	喀什镇
654021201000	吐鲁番于孜乡
654021202000	喀拉亚尕奇乡
654021203000	武功乡
654021204000	萨地克于孜乡
654021205000	愉群翁回族乡
654021209000	维吾尔玉其温乡
654021212000	麻扎乡
654021213000	温亚尔乡
654021214000	阿乌利亚乡
654021215000	曲鲁海乡
654021501000	兵团七十团中心团场
654022100000	察布查尔镇
654022101000	爱新色里镇
654022102000	孙扎齐牛录镇
654022103000	绰霍尔镇
654022104000	加尕斯台镇
654022105000	琼博拉镇
654022200000	堆齐牛录乡
654022203000	纳达齐牛录乡
654022204000	扎库齐牛录乡
654022205000	米粮泉回族乡
654022206000	坎乡
654022207000	阔洪奇乡
654022208000	海努克乡
654022401000	安班巴格良繁场
654022403000	伊犁州平原林场
654022404000	山区林场
654022408000	都拉塔口岸
654022503000	兵团六十七团分部
654022504000	兵团六十九团
654023100000	水定镇
654023101000	清水河镇
654023102000	芦草沟镇
654023103000	惠远镇
654023104000	萨尔布拉克镇
654023200000	兰干乡
654023201000	三道河乡
654023204000	三宫乡
654023205000	大西沟乡
654023402000	果子沟牧场
654023403000	良种繁育中心
654023509000	兵团六十六团分部
654024100000	巩留镇
654024101000	阿克吐别克镇
654024102000	库尔德宁镇
654024103000	东买里镇
654024104000	阿尕尔森镇
654024105000	提克阿热克镇
654024201000	吉尔格郎乡
654024204000	塔斯托别乡
654024400000	综合农场
654024401000	阔什阿尕什羊场
654024402000	牛场
654024403000	良凡场
654024405000	林场
654024510000	兵团七十三团
654025100000	新源镇
654025101000	则克台镇
654025102000	阿热勒托别镇
654025103000	塔勒德镇
654025104000	那拉提镇
654025105000	肖尔布拉克镇
654025106000	喀拉布拉镇
654025107000	阿勒玛勒镇
654025108000	坎苏镇
654025200000	别斯托别乡
654025204000	吐尔根乡
654025400000	种羊场
654025403000	公安农场
654025511000	兵团七十一团
654025512000	兵团七十二团
654026100000	昭苏镇
654026101000	喀夏加尔镇
654026102000	阿克达拉镇
654026103000	喀拉苏镇
654026104000	洪纳海镇
654026201000	乌尊布拉克乡
654026203000	萨尔阔布乡
654026206000	察汗乌苏蒙古族乡
654026207000	夏特柯尔克孜族乡
654026208000	胡松图喀尔逊蒙古族乡
654026403000	天山西部林业局昭苏林场
654026513000	兵团七十四团
654026514000	兵团七十五团
654026515000	兵团七十六团
654026516000	兵团七十七团
654027100000	特克斯镇
654027101000	乔拉克铁热克镇
654027102000	喀拉达拉镇
654027103000	齐勒乌泽克镇
654027104000	喀拉托海镇
654027200000	呼吉尔特蒙古民族乡
654027201000	阔克苏乡
654027203000	阔克铁热克柯尔克孜民族乡
654027404000	特克斯县马场
654027405000	科克苏林场
654027517000	兵团七十八团
654028100000	尼勒克镇
654028101000	乌拉斯台镇
654028102000	乌赞镇
654028103000	木斯镇
654028200000	苏布台乡
654028201000	喀拉苏乡
654028202000	加哈乌拉斯台乡
654028204000	科克浩特浩尔蒙古民族乡
654028206000	克令乡
654028207000	喀拉托别乡
654028208000	胡吉尔台乡
654028404000	种蜂场
654028518000	兵团七十九团
"""

data = """
654201001000	和平街道
654201002000	杜别克街道
654201003000	新城街道
654201100000	二工镇
654201101000	恰夏镇
654201200000	喀拉哈巴克乡
654201202000	阿西尔达斡尔民族乡
654201203000	阿不都拉乡
654201204000	也门勒乡
654201403000	恰合吉牧场
654201404000	博孜达克农场
654201405000	窝依加依劳牧场
654201406000	地区种牛场
654201502000	兵团第九师一六二团
654201503000	兵团农九师一六三团
654201504000	兵团农九师一六四团
654202001000	南苑街道
654202002000	虹桥街道
654202003000	新市区街道
654202006000	西城街道
654202007000	奎河街道
654202100000	白杨沟镇
654202101000	哈图布呼镇
654202102000	皇宫镇
654202103000	车排子镇
654202104000	甘河子镇
654202105000	百泉镇
654202106000	四棵树镇
654202107000	古尔图镇
654202108000	西湖镇
654202109000	西大沟镇
654202200000	八十四户乡
654202201000	夹河子乡
654202202000	九间楼乡
654202203000	石桥乡
654202204000	头台乡
654202205000	吉尔格勒特郭愣蒙古民族乡
654202206000	塔布勒合特蒙古民族乡
654202400000	甘家湖牧场
654202401000	巴音沟牧场
654202402000	赛力克提牧场
654202403000	乌苏监狱
654202500000	兵团一二三团生活区
654202501000	兵团一二四团生活区
654202502000	兵团一二五团分部生活区
654202503000	兵团一二六团生活区
654202504000	兵团一二七团生活区
654202505000	兵团一二八团分部生活区
654202507000	兵团一三零团分部生活区
654221100000	额敏镇
654221101000	玉什喀拉苏镇
654221102000	杰勒阿尕什镇
654221103000	上户镇
654221104000	玛热勒苏镇
654221105000	喀拉也木勒镇
654221200000	郊区乡
654221202000	额玛勒郭楞蒙古民族乡
654221207000	喇嘛昭乡
654221208000	霍吉尔特蒙古民族乡
654221209000	二道桥乡
654221400000	二支河牧场
654221401000	加尔布拉克农场
654221402000	阔什比克良种场
654221403000	萨尔也木勒牧场
654221404000	也木勒牧场
654221405000	塔城地区种羊场
654221406000	吾宗布拉克牧场
654221505000	兵团农九师一六五团
654221506000	兵团农九师一六六团
654221507000	兵团农九师一六七团
654221508000	兵团农九师一六八团
654221511000	兵团农九师团结农场
654223100000	三道河子镇
654223101000	四道河子镇
654223102000	老沙湾镇
654223103000	乌兰乌苏镇
654223104000	安集海镇
654223105000	东湾镇
654223106000	西戈壁镇
654223107000	柳毛湾镇
654223108000	金沟河镇
654223200000	商户地乡
654223201000	大泉乡
654223202000	博尔通古乡
654223400000	牛圈子牧场
654223401000	博尔通古牧场
654223402000	良种场
654223500000	兵团北泉镇分部
654223503000	兵团一二一团
654223506000	兵团一三三团
654223507000	兵团一三四团
654223509000	兵团一四一团
654223510000	兵团一四二团
654223511000	兵团一四三团
654223512000	兵团一四四团
654224100000	托里镇
654224101000	铁厂沟镇
654224102000	庙尔沟镇
654224200000	多拉特乡
654224201000	乌雪特乡
654224202000	库普乡
654224203000	阿克别里斗乡
654224401000	白杨河林场
654224402000	老风口林场
654224403000	巴尔鲁克山塔斯特林场
654224510000	兵团农九师一七零团
654225100000	哈拉布拉镇
654225101000	吉也克镇
654225200000	哈拉布拉乡
654225201000	新地乡
654225202000	阿勒腾也木勒乡
654225204000	江格斯乡
654225400000	察汗托海牧场
654225501000	兵团农九师一六一团
654226100000	和布克赛尔镇
654226101000	和什托洛盖镇
654226200000	夏孜盖乡
654226201000	铁布肯乌散乡
654226202000	查干库勒乡
654226203000	巴音傲瓦乡
654226204000	莫特格乡
654226205000	查和特乡
654226400000	伊克乌图布拉格牧场
654226401000	那仁和布克牧场
654226402000	巴尕乌图布拉格牧场
654226403000	布斯屯格牧场
654226500000	兵团一八四团
654226501000	新疆屯南煤业有限责任公司
654301001000	金山路街道
654301002000	解放路街道
654301003000	团结路街道
654301004000	恰秀路街道
654301100000	北屯镇
654301101000	阿苇滩镇
654301102000	红墩镇
654301103000	切木尔切克镇
654301104000	阿拉哈克镇
654301202000	汗德尕特蒙古族乡
654301203000	拉斯特乡
654301204000	喀拉希力克乡
654301205000	萨尔胡松乡
654301206000	巴里巴盖乡
654301207000	切尔克齐乡
654301400000	喀拉尕什牧场
654301401000	阿克吐木斯克牧场
654301500000	兵团一八一团
654321100000	布尔津镇
654321101000	冲乎尔镇
654321102000	窝依莫克镇
654321103000	阔斯特克镇
654321201000	杜来提乡
654321204000	也格孜托别乡
654321205000	禾木哈纳斯蒙古族乡
654322100000	库额尔齐斯镇
654322101000	可可托海镇
654322102000	恰库尔图镇
654322103000	喀拉通克镇
654322104000	杜热镇
654322200000	吐尔洪乡
654322202000	库尔特乡
654322203000	克孜勒希力克乡
654322204000	铁买克乡
654322205000	喀拉布勒根乡
654323100000	福海镇
654323101000	喀拉玛盖镇
654323102000	解特阿热勒镇
654323201000	阔克阿尕什乡
654323202000	齐干吉迭乡
654323204000	阿尔达乡
654323400000	地区一农场
654323401000	福海监狱
654323500000	兵团一八二团
654323504000	兵团一八三团分部
654323505000	兵团一八八团分部
654324100000	阿克齐镇
654324101000	萨尔布拉克镇
654324102000	齐巴尔镇
654324103000	库勒拜镇
654324200000	萨尔塔木乡
654324201000	加依勒玛乡
654324204000	铁热克提乡
654324500000	兵团一八五团
654325100000	青河镇
654325101000	塔克什肯镇
654325102000	阿热勒托别镇
654325103000	阿格达拉镇
654325104000	阿热勒镇
654325202000	萨尔托海乡
654325203000	查干郭勒乡
654325204000	阿尕什敖包乡
654326100000	托普铁热克镇
654326101000	吉木乃镇
654326102000	喀尔交镇
654326103000	乌拉斯特镇
654326201000	托斯特乡
654326202000	恰勒什海乡
654326204000	别斯铁热克乡
654326500000	兵团一八六团
659001001000	新城街道
659001002000	向阳街道
659001003000	红山街道
659001004000	老街街道
659001005000	东城街道
659001100000	北泉镇
659001101000	石河子镇
659001500000	兵团一五二团
659002001000	金银川路街道
659002002000	幸福路街道
659002003000	青松路街道
659002100000	金银川镇
659002101000	新井子镇
659002102000	甘泉镇
659002103000	永宁镇
659002104000	沙河镇
659002105000	双城镇
659002106000	花桥镇
659002107000	幸福镇
659002108000	金杨镇
659002200000	托喀依乡
659002402000	工业园区
659002500000	兵团七团
659002501000	兵团八团
659002503000	兵团十团
659002505000	兵团十二团
659002509000	兵团十六团
659002510000	兵团九团
659002518000	西工业园区
659003001000	锦绣街道
659003002000	前海街道
659003003000	永安坝街道
659003100000	草湖镇
659003101000	龙口镇
659003102000	前海镇
659003103000	永兴镇
659003104000	兴安镇
659003105000	嘉和镇
659003106000	河东镇
659003107000	夏河镇
659003504000	兵团四十四团
659003509000	兵团四十九团
659003511000	兵团五十一团
659003513000	兵团五十三团
659003514000	兵团图木舒克市喀拉拜勒镇
659004001000	军垦路街道
659004002000	青湖路街道
659004003000	人民路街道
659004100000	梧桐镇
659004101000	蔡家湖镇
659004500000	兵团一零一团
659004501000	五家渠经济技术开区
659005100000	双渠镇
659005101000	丰庆镇
659005102000	海川镇
659005400000	北屯市核心区
659006100000	博古其镇
659006101000	双丰镇
659006102000	河畔镇
659006103000	高桥镇
659006104000	天湖镇
659006105000	开泽镇
659006106000	米兰镇
659006107000	金山镇
659006108000	南屯镇
659007100000	双桥镇
659007101000	石峪镇
659007102000	博河镇
659007103000	双乐镇
659007400000	双河市核心区
659007500000	兵团八十九团
659008100000	榆树庄镇
659008101000	苇湖镇
659008102000	长丰镇
659008400000	可克达拉市核心区
659008500000	兵团六十六团
659008501000	兵团六十七团
659009100000	老兵镇
659009101000	昆泉镇
659009102000	昆牧镇
659009103000	玉泉镇
659009400000	昆玉市核心区
659009500000	兵团二二四团
659009501000	北京皮墨工业园区
659010400000	胡杨河市核心区
659010500000	兵团一二五团
659010501000	兵团一二八团
659010502000	兵团一二九团
659010503000	兵团一三零团
"""

data = """130207103000	小集镇
130207104000	黄各庄镇
130207105000	西葛镇
130207106000	大新庄镇
130207107000	钱营镇
130207108000	唐坊镇
130207109000	王兰庄镇
130207110000	柳树酄镇
130207111000	黑沿子镇
130207113000	胥各庄镇
130207114000	大齐各庄镇
130207115000	岔河镇
130207201000	南孙庄乡
130207202000	东田庄乡
130207203000	尖字沽乡"""

data = """130208001000	太平路街道
130208002000	燕山路街道
130208003000	浭阳街道
130208100000	丰润镇
130208102000	任各庄镇
130208103000	左家坞镇
130208104000	泉河头镇
130208105000	王官营镇
130208106000	火石营镇
130208109000	新军屯镇
130208110000	小张各庄镇
130208111000	丰登坞镇
130208112000	李钊庄镇
130208113000	白官屯镇
130208114000	石各庄镇
130208115000	沙流河镇
130208116000	七树庄镇
130208117000	杨官林镇
130208118000	银城铺镇
130208119000	常庄镇
130208202000	姜家营乡
130208205000	欢喜庄乡
130208208000	刘家营乡"""

data = """130224001000	友谊路街道
130224100000	倴城镇
130224101000	宋道口镇
130224102000	长凝镇
130224103000	胡各庄镇
130224104000	坨里镇
130224105000	姚王庄镇
130224106000	司各庄镇
130224107000	安各庄镇
130224108000	扒齿港镇
130224109000	程庄镇
130224110000	青坨营镇
130224111000	柏各庄镇
130224114000	南堡镇
130224115000	方各庄镇
130224116000	东黄坨镇
130224117000	马城镇"""

data = """130408100000	临洺关镇
130408101000	大北汪镇
130408102000	张西堡镇
130408103000	广府镇
130408105000	永合会镇
130408106000	刘营镇
130408107000	西苏镇
130408108000	讲武镇
130408109000	东杨庄镇
130408201000	界河店乡
130408203000	刘汉乡
130408204000	正西乡
130408206000	曲陌乡
130408207000	辛庄堡乡
130408208000	小龙马乡
130408211000	西河庄乡
130408213000	西阳城乡
"""

data = """130523100000	内丘镇
130523101000	大孟村镇
130523102000	金店镇
130523103000	官庄镇
130523104000	柳林镇
130523200000	五郭店乡
130523203000	南赛乡
130523204000	獐獏乡
130523205000	侯家庄乡
"""

data = """130533100000	洺州镇
130533101000	梨园屯镇
130533102000	章台镇
130533103000	侯贯镇
130533104000	七级镇
130533105000	贺营镇
130533106000	方家营镇
130533107000	常庄镇
130533108000	第什营镇
130533109000	贺钊镇
130533110000	赵村镇
130533202000	枣园乡
130533203000	固献乡
130533206000	张家营乡
130533207000	常屯乡
130533209000	高公庄乡
"""

data = """130638100000	雄州镇
130638101000	昝岗镇
130638102000	大营镇
130638103000	龙湾镇
130638104000	朱各庄镇
130638105000	米家务镇
130638106000	鄚州镇
130638107000	苟各庄镇
130638200000	北沙口乡
130638203000	双堂乡
130638204000	张岗乡
130638205000	七间房乡
"""

data = """130723100000	康保镇
130723101000	张纪镇
130723102000	土城子镇
130723103000	邓油坊镇
130723104000	李家地镇
130723105000	照阳河镇
130723106000	屯垦镇
130723200000	闫油坊乡
130723201000	丹清河乡
130723202000	哈咇嘎乡
130723203000	二号卜乡
130723204000	芦家营乡
130723205000	忠义乡
130723206000	处长地乡
130723207000	满德堂乡
130723500000	康保牧场
130723501000	屯垦林场
"""
data = """330203001000	南门街道
330203002000	江厦街道
330203003000	西门街道
330203004000	月湖街道
330203005000	鼓楼街道
330203006000	白云街道
330203007000	段塘街道
330203008000	望春街道
330203009000	石碶街道
330203100000	高桥镇
330203101000	横街镇
330203102000	集士港镇
330203103000	古林镇
330203104000	洞桥镇
330203105000	鄞江镇
330203106000	章水镇
330203200000	龙观乡
"""

data = """330206001000	大榭街道
330206002000	新碶街道
330206003000	小港街道
330206004000	大碶街道
330206005000	霞浦街道
330206006000	柴桥街道
330206007000	戚家山街道
330206008000	春晓街道
330206009000	梅山街道
330206010000	郭巨街道
330206011000	白峰街道
330206401000	保税区"""

data = """330226001000	跃龙街道
330226002000	桃源街道
330226003000	梅林街道
330226004000	桥头胡街道
330226101000	长街镇
330226102000	力洋镇
330226104000	一市镇
330226105000	岔路镇
330226106000	前童镇
330226107000	桑洲镇
330226108000	黄坛镇
330226109000	大佳何镇
330226110000	强蛟镇
330226111000	西店镇
330226112000	深甽镇
330226200000	胡陈乡
330226201000	茶院乡
330226202000	越溪乡"""


# split= re.split(r'\d+', data)
# print(split)
# name = []
# for item in split:
#     if len(item) == 0 or item == '\n' or item == '\r':
#         continue
#     replace = item.replace('\t', '').replace('\n', '')
#     name.append(replace)
# print(name)
# split= re.split(r'\D+', data)
# code = []
# for item in split:
#     if len(item) == 0:
#         continue
#     replace = item.replace('\t', '').replace('\n', '')
#     code.append(replace[:-3])
# print(code)
# d = dict(zip(code, name))
# dumps = json.dumps(d,ensure_ascii=False)
# print(dumps)

def read_data_to_file(file_name):
    result = {}
    try:
        with open(file_name, "r", encoding="utf-8") as f1:
            data = f1.readline()
            split = data.split(',')
            for item_index, item_val in enumerate(split):
                item_val = item_val.lstrip()
                if item_val.startswith('['):
                    item_val = item_val.replace('[', '')
                    item_val = item_val.replace('"', '')

                    result[item_val[0:9]] = split[item_index + 1].lstrip().replace('"','')
            return result
    except Exception as e:
        raise Exception('Save ERROR:', e)


def write_data_to_file(data, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f1:
            content = json.dumps(data, ensure_ascii=False)
            f1.write(content)
    except Exception as e:
        raise Exception('Save ERROR:', e)


data = read_data_to_file("C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇_1.txt")
write_data_to_file(data, "C:\\Users\\EDZ\\Desktop\\全国省、市、县、乡名称及对应的编码\\file\\镇.txt")
print(type(data))
print(data)
