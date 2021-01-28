"""
每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法
例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，
另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。
注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
在结果列表中，选择 字典序最小 的名字作为真实名字。

示例：
输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]
"""
import re
from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        # names = dict(zip([re.search(r'[a-zA-Z]+', item).group() for item in names],
        #                  [int(re.search(r'\d+', item).group()) for item in names]))
        # print(names)
        #
        # synonyms = [item.replace('(', '').replace(',', ' ').replace(')', '').split(' ') for item in synonyms]
        # print(synonyms)
        #
        # result = {}
        # dict_name = {}
        # for item_key, item_val in names.items():
        #     dict_name[item_key] = item_key
        # print(dict_name)
        #
        # def __find_root(key: str) -> str:
        #     while True:
        #         if key == dict_name.get(key):
        #             return key
        #         else:
        #             key = dict_name.get(key)
        #
        # for item in synonyms:
        #     if not dict_name.__contains__(item[0]):
        #         dict_name[item[0]] = item[0]
        #     if not dict_name.__contains__(item[1]):
        #         dict_name[item[1]] = item[1]
        #     temp_root = __find_root(item[0])
        #     temp_val = __find_root(item[1])
        #     if temp_root >= temp_val:
        #         dict_name[temp_root] = temp_val
        #     else:
        #         dict_name[temp_val] = temp_root
        # print(dict_name)
        #
        # for item_key, item_val in names.items():
        #     # 获取根名字对应的根
        #     root = __find_root(item_key)
        #     result[root] = result.get(root, 0) + item_val
        #
        # return [item_key + '(' + str(item_val) + ')' for item_key, item_val in result.items()]

        # 这道题不采用普通并查集class(数组)写是因为父亲数组需要动态变化
        # hashmap可以灵活的增加元素
        # 这道题容易忽视的corner case是names里面的两个name 通过中间的不曾出现过的name链接起来
        # 譬如names里面a:14 d:13 连接关系(a,b)(b,c)(c,d)可以把ad合并
        # 但是其他人的代码里都没体现这一点

        f, cnt = {}, {}
        for name in names:
            n, c = name.split("(")
            f[n], cnt[n] = n, int(c[:-1])

        # 并查集查找同类根
        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for s in synonyms:
            name1, name2 = s[1:-1].split(",")
            # 不存在的话 仍然需要在f和cnt里进行增加 因为连接关系仍有用
            if name1 not in f:
                f[name1] = name1
                cnt[name1] = 0
            if name2 not in f:
                f[name2] = name2
                cnt[name2] = 0
            p1, p2 = find(name1), find(name2)
            if p1 == p2:
                # 父亲一样 那么此时什么都不做
                continue
            # 父亲不一样 需要合并 字典序小的作为父亲
            freq = cnt[p1] + cnt[p2]
            fa = min(p1, p2)
            ch = max(p1, p2)
            f[ch] = fa
            cnt[ch] = 0
            cnt[fa] = freq

        ans = {}
        for k, v in f.items():
            if k == v and cnt[k] != 0:
                ans[k] = cnt[k]
        return [k + '(' + str(v) + ')' for k, v in ans.items()]


# print(Solution().trulyMostPopular(names=["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
#                                   synonyms=["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]))


names = ["Fcclu(70)", "Ommjh(63)", "Dnsay(60)", "Qbmk(45)", "Unsb(26)", "Gauuk(75)", "Wzyyim(34)", "Bnea(55)",
         "Kri(71)", "Qnaakk(76)", "Gnplfi(68)", "Hfp(97)", "Qoi(70)", "Ijveol(46)", "Iidh(64)", "Qiy(26)", "Mcnef(59)",
         "Hvueqc(91)", "Obcbxb(54)", "Dhe(79)", "Jfq(26)", "Uwjsu(41)", "Wfmspz(39)", "Ebov(96)", "Ofl(72)",
         "Uvkdpn(71)", "Avcp(41)", "Msyr(9)", "Pgfpma(95)", "Vbp(89)", "Koaak(53)", "Qyqifg(85)", "Dwayf(97)",
         "Oltadg(95)", "Mwwvj(70)", "Uxf(74)", "Qvjp(6)", "Grqrg(81)", "Naf(3)", "Xjjol(62)", "Ibink(32)", "Qxabri(41)",
         "Ucqh(51)", "Mtz(72)", "Aeax(82)", "Kxutz(5)", "Qweye(15)", "Ard(82)", "Chycnm(4)", "Hcvcgc(97)", "Knpuq(61)",
         "Yeekgc(11)", "Ntfr(70)", "Lucf(62)", "Uhsg(23)", "Csh(39)", "Txixz(87)", "Kgabb(80)", "Weusps(79)", "Nuq(61)",
         "Drzsnw(87)", "Xxmsn(98)", "Onnev(77)", "Owh(64)", "Fpaf(46)", "Hvia(6)", "Kufa(95)", "Chhmx(66)", "Avmzs(39)",
         "Okwuq(96)", "Hrschk(30)", "Ffwni(67)", "Wpagta(25)", "Npilye(14)", "Axwtno(57)", "Qxkjt(31)", "Dwifi(51)",
         "Kasgmw(95)", "Vgxj(11)", "Nsgbth(26)", "Nzaz(51)", "Owk(87)", "Yjc(94)", "Hljt(21)", "Jvqg(47)", "Alrksy(69)",
         "Tlv(95)", "Acohsf(86)", "Qejo(60)", "Gbclj(20)", "Nekuam(17)", "Meutux(64)", "Tuvzkd(85)", "Fvkhz(98)",
         "Rngl(12)", "Gbkq(77)", "Uzgx(65)", "Ghc(15)", "Qsc(48)", "Siv(47)"]

synonyms = ["(Gnplfi,Qxabri)", "(Uzgx,Siv)", "(Bnea,Lucf)", "(Qnaakk,Msyr)", "(Grqrg,Gbclj)", "(Uhsg,Qejo)",
            "(Csh,Wpagta)", "(Xjjol,Lucf)", "(Qoi,Obcbxb)", "(Npilye,Vgxj)", "(Aeax,Ghc)", "(Txixz,Ffwni)",
            "(Qweye,Qsc)", "(Kri,Tuvzkd)", "(Ommjh,Vbp)", "(Pgfpma,Xxmsn)", "(Uhsg,Csh)", "(Qvjp,Kxutz)", "(Qxkjt,Tlv)",
            "(Wfmspz,Owk)", "(Dwayf,Chycnm)", "(Iidh,Qvjp)", "(Dnsay,Rngl)", "(Qweye,Tlv)", "(Wzyyim,Kxutz)",
            "(Hvueqc,Qejo)", "(Tlv,Ghc)", "(Hvia,Fvkhz)", "(Msyr,Owk)", "(Hrschk,Hljt)", "(Owh,Gbclj)", "(Dwifi,Uzgx)",
            "(Iidh,Fpaf)", "(Iidh,Meutux)", "(Txixz,Ghc)", "(Gbclj,Qsc)", "(Kgabb,Tuvzkd)", "(Uwjsu,Grqrg)",
            "(Vbp,Dwayf)", "(Xxmsn,Chhmx)", "(Uxf,Uzgx)"]

print(Solution().trulyMostPopular(names, synonyms))

for item in synonyms:
    if item.__contains__('Chycnm') or item.__contains__('Dwayf') or item.__contains__('Vbp'):
        print(item)
