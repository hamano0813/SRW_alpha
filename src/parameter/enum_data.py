#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import QObject


# noinspection PyUnresolvedReferences
class EnumDataTrans(QObject):
    def __init__(self):
        super(EnumDataTrans, self).__init__(parent=None)
        self.SCENARIO = {
            0x00: ('[00]', '共通', '第0話', 'プロローグ'),
            0x01: ('[01]', self.tr('スーパー系'), '第1話', '鋼鉄のコクピット'),
            0x02: ('[02]', 'スーパー系', '第2話', 'マジンガーZ絶体絶命'),
            0x03: ('[03]', 'スーパー系', '第3話', 'ゲッターチーム出撃せよ！'),
            0x04: ('[04]', 'スーパー系', '第4話', 'ジオン再臨'),
            0x05: ('[05]', 'スーパー系', '第5話', 'シークレット・ナンバーズ'),
            0x06: ('[06]', 'スーパー系', '第6話', 'アーガマ撃墜命令'),
            0x07: ('[07]', 'リアル系', '第1話', 'バニシング・トルーパー'),
            0x08: ('[08]', 'リアル系', '第2話', '黒いガンダム'),
            0x09: ('[09]', 'リアル系', '第3話', 'ホワイトベース救出'),
            0x0A: ('[0A]', 'リアル系', '第4話', '死神と呼ばれたG'),
            0x0B: ('[0B]', 'リアル系', '第5話', 'ジオンの亡霊'),
            0x0C: ('[0C]', 'リアル系', '第6話', '対決、極東基地'),
            0x0D: ('[0D]', '共通', '第7話', 'レッツ！コンバイン'),
            0x0E: ('[0E]', '共通', '第8話', '出撃！その名はジャイアント・ロボ'),
            0x0F: ('[0F]', 'スーパー系', '第9話', '風を呼ぶ者'),
            0x10: ('[10]', 'リアル系', '第9話', '未知なる災い'),
            0x11: ('[11]', 'ジャブロー', '第10話', 'アムロ再び'),
            0x12: ('[12]', 'ジャブロー', '第11話', '白いモビルスーツ'),
            0x13: ('[13]', 'ジャブロー', '第12話', '戦いは誰のために'),
            0x14: ('[14]', 'ジャブロー', '第13話', '翼を持ったガンダム'),
            0x15: ('[15]', '南アタリア島', '第10話', '目覚めよ、勇者'),
            0x16: ('[16]', '南アタリア島', '第11話', 'ガンダム強奪'),
            0x17: ('[17]', '南アタリア島', '第12話', '野望の男'),
            0x18: ('[18]', '南アタリア島', '第13話', '少女が見た流星'),
            0x19: ('[19]', '共通', '第14話', '父との約束'),
            0x1A: ('[1A]', '共通', '第15話', '使徒、襲来'),
            0x1B: ('[1B]', '共通', '第16話', '咆哮、EVA初号機'),
            0x1C: ('[1C]', '共通', '第17話', 'GR対GR2'),
            0x1D: ('[1D]', 'リアル系', '第18話', 'ゼータの鼓動'),
            0x1E: ('[1E]', 'リアル系', '第19話', '第二次直上会議'),
            0x1F: ('[1F]', 'スーパー系', '第18話', '紅い稲妻 空飛ぶマジンガー'),
            0x20: ('[20]', 'スーパー系', '第19話', '激突！ゲッターロボVSゲッターロボG'),
            0x21: ('[21]', '共通', '第20話幕前', '決戦、第2新東京市'),
            0x22: ('[22]', '共通', '第20話', '決戦、第2新東京市'),
            0x23: ('[23]', 'EVA弐号機', '第21話幕前', '圣战士たち'),
            0x24: ('[24]', 'EVA弐号機', '第21話', '圣战士たち'),
            0x25: ('[25]', 'EVA弐号機', '第22話', 'エレの霊力'),
            0x26: ('[24]', 'EVA弐号機', '第23話', 'ナの国の女王'),
            0x27: ('[25]', 'EVA弐号機', '第24話', 'オーラロード'),
            0x28: ('[26]', 'EVA弐号機', '第25話', '東京上空'),
            0x29: ('[27]', '極東基地', '第21話', '獣を超え、人を超え、いでよ神の戦士'),
            0x2A: ('[28]', '極東基地', '第22話', '戦いの海へ'),
            0x2B: ('[29]', '極東基地', '第23話第1幕', 'マジンガーZ対暗黒大将軍'),
            0x2C: ('[29]', '極東基地', '第23話第2幕', 'マジンガーZ対暗黒大将軍'),
            0x2D: ('[2A]', '極東基地', '第24話', 'ボルテス起死回生'),
            0x2E: ('[2B]', '極東基地', '第25話', 'シャーキン悪魔の戦い'),
            0x2F: ('[2C]', '宇宙', '第21話', 'ホンコン・シティ'),
            0x30: ('[2D]', '宇宙', '第22話', 'ガンダム、星の海へ'),
            0x31: ('[2E]', '宇宙', '第23話', '始動ダブルゼータ'),
            0x32: ('[2F]', '宇宙', '第24話', 'ソロモンの悪夢'),
            0x33: ('[30]', '宇宙', '第25話', 'クロスボーン・バンガード'),
            0x34: ('[31]', 'EVA弐号機/極東基地', '第26話', '紅いエヴァンゲリオン'),
            0x35: ('[32]', '宇宙', '第26話', '海からのマレビト'),
            0x36: ('[33]', '共通', '第27話', 'マシン展開'),
            0x37: ('[34]', 'EVA2体同時攻撃', '第30話', '瞬間、心重ねて'),
            0x38: ('[35]', '弾丸を撃ち落す', '第31話', 'ブービー・トラップ'),
            0x39: ('[36]', '弾丸を撃ち落す', '第32話', 'カウント・ダウン'),
            0x3A: ('[37]', '弾丸を撃ち落す', '第33話', 'トランス・フォーメーション'),
            0x3B: ('[38]', '弾丸を撃ち落す', '第34話', '隠された殺意'),
            0x3C: ('[39]', '弾丸を撃ち落す', '第35話', 'サタン・ファイト'),
            0x3D: ('[3A]', '弾丸を撃ち落す', '第36話', 'リン・ミンメイ'),
            0x3E: ('[3B]', '弾丸を撃ち落す', '第37話', 'ジュピトリアン'),
            0x3F: ('[3C]', '弾丸を撃ち落す', '第38話', '帝国の女王'),
            0x40: ('[3D]', '弾丸を撃ち落す', '第39話', '終末への前奏曲'),
            0x41: ('[3E]', 'EVAで受け止める', '第31話', '奇跡の価値は'),
            0x42: ('[3F]', 'EVAで受け止める', '第32話', 'スペース・フォールド'),
            0x43: ('[40]', 'EVAで受け止める', '第33話', 'アームド・アタック'),
            0x44: ('[41]', 'EVAで受け止める', '第34話', '天敵との遭遇'),
            0x45: ('[42]', 'EVAで受け止める', '第35話', 'イングラムの真意'),
            0x46: ('[43]', 'EVAで受け止める', '第36話', 'ミス・マクロス'),
            0x47: ('[44]', 'EVAで受け止める', '第37話', '木星からの逃亡者'),
            0x48: ('[45]', 'EVAで受け止める', '第38話', '人類を導く者'),
            0x49: ('[46]', 'EVAで受け止める', '第39話', 'ファースト・コンタクト'),
            0x4A: ('[47]', '共通', '第40話', 'ビッグ・エスケープ'),
            0x4B: ('[48]', '共通', '第41話', 'バイバイ・マルス'),
            0x4C: ('[49]', 'リーンホースJr.组', '第42話', 'アクシズからの使者'),
            0x4D: ('[4A]', 'リーンホースJr.组', '第43話', 'プルとアクシズと'),
            0x4E: ('[4B]', 'リーンホースJr.组', '第44話', 'リィナの血'),
            0x4F: ('[4C]', 'リーンホースJr.组', '第45話', '漆黒の天使来たりて'),
            0x50: ('[4D]', 'グラン・ガラン组', '第42話', 'ジュピター・ゴースト'),
            0x51: ('[4E]', 'グラン・ガラン组', '第43話', '宇宙に咲く妖花'),
            0x52: ('[4F]', 'グラン・ガラン组', '第44話', 'ゼロと呼ばれたガンダム'),
            0x53: ('[50]', 'グラン・ガラン组', '第45話', '強襲、阻止限界点'),
            0x54: ('[51]', 'ゴラオン组', '第42話', '父よ地球は近い'),
            0x55: ('[52]', 'ゴラオン组', '第43話', '静止した闇の中で'),
            0x56: ('[53]', 'ゴラオン组', '第44話', '赤い髪の女'),
            0x57: ('[54]', 'ゴラオン组', '第45話', '神か、悪魔か・・・'),
            0x58: ('[55]', 'スーパー系', '第46話', '龍と虎'),
            0x59: ('[56]', 'リアル系', '第46話', '第三の力'),
            0x5A: ('[57]', '共通', '第47話', '男の戦い'),
            0x5B: ('[58]', '共通', '第50話', 'ヴァリアブル・フォーメーション'),
            0x5C: ('[59]', 'グラン・ガラン组', '第51話', 'ガラスの王国'),
            0x5D: ('[5A]', 'ラー・カイラム组', '第51話', 'ダカールの日'),
            0x5E: ('[5B]', 'グラン・ガラン组', '第52話', '王国崩壊'),
            0x5F: ('[5C]', 'ラー・カイラム组', '第52話', 'バイブレーション'),
            0x60: ('[5D]', 'ゴラオン组', '第54話', '思い出を未来へ'),
            0x61: ('[5E]', 'ラー・カイラム组', '第53話', 'ソロモン攻略戦'),
            0x62: ('[5F]', 'ラー・カイラム组', '第54話', '女たちの戦場'),
            0x63: ('[60]', 'ラー・カイラム组', '第55話', '駆け抜ける嵐'),
            0x64: ('[61]', 'ゴラオン组', '第51話', 'あしゅら男爵、散る'),
            0x65: ('[62]', 'ゴラオン组', '第52話', '魔神皇帝'),
            0x66: ('[63]', 'グラン・ガラン组', '第53話', 'クロス・ファイト'),
            0x67: ('[64]', 'グラン・ガラン组', '第54話', '異邦人たちの帰還'),
            0x68: ('[65]', 'ゴラオン组', '第53話', '地球を賭けた一騎討ち'),
            0x69: ('[66]', '共通', '第56話', 'ジオンの幻像'),
            0x6A: ('[67]', 'ゴラオン组', '第55話', '父の胸の中で泣け！'),
            0x6B: ('[68]', 'グラン・ガラン组', '第55話', '女王リリーナ'),
            0x6C: ('[69]', '共通', '第57話0', '天使の輪の上で'),
            0x6D: ('[69]', '共通', '第57話', '天使の輪の上で'),
            0x6E: ('[6A]', 'アクシズ', '第58話', '神の国への誘惑'),
            0x6F: ('[6B]', 'アクシズ', '第59話', 'クロス・目标机师'),
            0x70: ('[6C]', 'アクシズ', '第60話', '戦士、再び・・・'),
            0x71: ('[6D]', 'エンジェル・ハイロゥ', '第58話', '勝者と敗者に祝福を'),
            0x72: ('[6E]', 'エンジェル・ハイロゥ', '第59話', 'せめて、人間らしく'),
            0x73: ('[6F]', 'エンジェル・ハイロゥ', '第60話', '最後のシ者'),
            0x74: ('[70]', '共通', '第61話', '運命の矢'),
            0x75: ('[71]', '共通', '第62話第1幕', '愛・おぼえていますか'),
            0x76: ('[71]', '共通', '第62話第2幕', '愛・おぼえていますか'),
            0x77: ('[72]', '共通', '第64話第1幕', 'Air'),
            0x78: ('[72]', '共通', '第64話第2幕', 'Air'),
            0x79: ('[73]', '共通', '第65話', 'ギア・オブ・デスティニー'),
            0x7A: ('[74]', '熟練度45以上', '第66話', '絶望の宴は今から始まる'),
            0x7B: ('[75]', '熟練度45以上', '第67話第1幕', 'この星の明日のために'),
            0x7C: ('[75]', '熟練度45以上', '第67話第2幕', 'この星の明日のために'),
            0x7D: ('[75]', '熟練度45以上', '第67話第3幕', 'この星の明日のために'),
            0x7E: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x7F: ('[77]', '熟練度45未満', '第66話', '人類に逃げ場なし'),
            0x80: ('[78]', '熟練度45未満', '第67話第1幕', '鋼の魂'),
            0x81: ('[78]', '熟練度45未満', '第67話第2幕', '鋼の魂'),
            0x82: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x83: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x84: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x85: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x86: ('[7C]', '共通', '第28話', 'ＥＯＴの島'),
            0x87: ('[7D]', 'スーパー系', '第29話', '心に念じる見えない刃'),
            0x88: ('[7E]', 'リアル系', '第29話', '黒い超闘士'),
            0x89: ('[7F]', '共通', '第48話', '誰がために鐘は鳴る'),
            0x8A: ('[80]', '共通', '第49話', '進路に光明、退路に絶望'),
            0x8B: ('[81]', '力ずくで撃退', '第30話', '精霊憑依'),
        }
        self.STAGE = {
            0x00: '共通 プロローグ プロローグ',
            0x01: 'スーパー系 第１話 鋼鉄のコクピット',
            0x02: 'スーパー系 第２話 マジンガーＺ絶体絶命',
            0x03: 'スーパー系 第３話 ゲッターチーム出撃せよ！',
            0x04: 'スーパー系 第４話 ジオン再臨',
            0x05: 'スーパー系 第５話 シークレット・ナンバーズ',
            0x06: 'スーパー系 第６話 アーガマ撃墜命令',
            0x07: 'リアル系 第１話 バニシング・トルーパー',
            0x08: 'リアル系 第２話 黒いガンダム',
            0x09: 'リアル系 第３話 ホワイトベース救出',
            0x0A: 'リアル系 第４話 死神と呼ばれたＧ',
            0x0B: 'リアル系 第５話 ジオンの亡霊',
            0x0C: 'リアル系 第６話 対決、極東基地',
            0x0D: '共通 第７話 レッツ！コンバイン',
            0x0E: '共通 第８話 出撃！その名はジャイアント・ロボ',
            0x0F: 'スーパー系 第９話 風を呼ぶ者',
            0x10: 'リアル系 第９話 未知なる災い',
            0x11: 'ジャブロー 第１０話 アムロ再び',
            0x12: 'ジャブロー 第１１話 白いモビルスーツ',
            0x13: 'ジャブロー 第１２話 戦いは誰のために',
            0x14: 'ジャブロー 第１３話 翼を持ったガンダム',
            0x15: '南アタリア島 第１０話 目覚めよ、勇者',
            0x16: '南アタリア島 第１１話 ガンダム強奪',
            0x17: '南アタリア島 第１２話 野望の男',
            0x18: '南アタリア島 第１３話 少女が見た流星',
            0x19: '共通 第１４話 父との約束',
            0x1A: '共通 第１５話 使徒、襲来',
            0x1B: '共通 第１６話 咆哮、ＥＶＡ初号機',
            0x1C: '共通 第１７話 ＧＲ対ＧＲ２',
            0x1D: 'リアル系 第１８話 ゼータの鼓動',
            0x1E: 'リアル系 第１９話 第二次直上会議',
            0x1F: 'スーパー系 第１８話 紅い稲妻　空飛ぶマジンガー',
            0x20: 'スーパー系 第１９話 激突！ゲッターロボＶＳゲッターロボＧ',
            0x21: '共通 第２０話 決戦、第２新東京市',
            0x22: 'ＥＶＡ弐号機 第２１話 圣战士たち',
            0x23: 'ＥＶＡ弐号機 第２２話 エレの霊力',
            0x24: 'ＥＶＡ弐号機 第２３話 ナの国の女王',
            0x25: 'ＥＶＡ弐号機 第２４話 オーラロード',
            0x26: 'ＥＶＡ弐号機 第２５話 東京上空',
            0x27: '極東基地 第２１話 獣を超え、人を超え、いでよ神の戦士',
            0x28: '極東基地 第２２話 戦いの海へ',
            0x29: '極東基地 第２３話 マジンガーＺ対暗黒大将軍',
            0x2A: '極東基地 第２４話 ボルテス起死回生',
            0x2B: '極東基地 第２５話 シャーキン悪魔の戦い',
            0x2C: '宇宙 第２１話 ホンコン・シティ',
            0x2D: '宇宙 第２２話 ガンダム、星の海へ',
            0x2E: '宇宙 第２３話 始動ダブルゼータ',
            0x2F: '宇宙 第２４話 ソロモンの悪夢',
            0x30: '宇宙 第２５話 クロスボーン・バンガード',
            0x31: 'ＥＶＡ弐号機／極東基地 第２６話 紅いエヴァンゲリオン',
            0x32: '宇宙 第２６話 海からのマレビト',
            0x33: '共通 第２７話 マシン展開',
            0x34: 'ＥＶＡ２体同時攻撃 第３０話 瞬間、心重ねて',
            0x35: '弾丸を撃ち落す 第３１話 ブービー・トラップ',
            0x36: '弾丸を撃ち落す 第３２話 カウント・ダウン',
            0x37: '弾丸を撃ち落す 第３３話 トランス・フォーメーション',
            0x38: '弾丸を撃ち落す 第３４話 隠された殺意',
            0x39: '弾丸を撃ち落す 第３５話 サタン・ファイト',
            0x3A: '弾丸を撃ち落す 第３６話 リン・ミンメイ',
            0x3B: '弾丸を撃ち落す 第３７話 ジュピトリアン',
            0x3C: '弾丸を撃ち落す 第３８話 帝国の女王',
            0x3D: '弾丸を撃ち落す 第３９話 終末への前奏曲',
            0x3E: 'ＥＶＡで受け止める 第３１話 奇跡の価値は',
            0x3F: 'ＥＶＡで受け止める 第３２話 スペース・フォールド',
            0x40: 'ＥＶＡで受け止める 第３３話 アームド・アタック',
            0x41: 'ＥＶＡで受け止める 第３４話 天敵との遭遇',
            0x42: 'ＥＶＡで受け止める 第３５話 イングラムの真意',
            0x43: 'ＥＶＡで受け止める 第３６話 ミス・マクロス',
            0x44: 'ＥＶＡで受け止める 第３７話 木星からの逃亡者',
            0x45: 'ＥＶＡで受け止める 第３８話 人類を導く者',
            0x46: 'ＥＶＡで受け止める 第３９話 ファースト・コンタクト',
            0x47: '共通 第４０話 ビッグ・エスケープ',
            0x48: '共通 第４１話 バイバイ・マルス',
            0x49: 'リーンホースJr.组 第４２話 アクシズからの使者',
            0x4A: 'リーンホースJr.组 第４３話 プルとアクシズと',
            0x4B: 'リーンホースJr.组 第４４話 リィナの血',
            0x4C: 'リーンホースJr.组 第４５話 漆黒の天使来たりて',
            0x4D: 'グラン・ガラン组 第４２話 ジュピター・ゴースト',
            0x4E: 'グラン・ガラン组 第４３話 宇宙に咲く妖花',
            0x4F: 'グラン・ガラン组 第４４話 ゼロと呼ばれたガンダム',
            0x50: 'グラン・ガラン组 第４５話 強襲、阻止限界点',
            0x51: 'ゴラオン组 第４２話 父よ地球は近い',
            0x52: 'ゴラオン组 第４３話 静止した闇の中で',
            0x53: 'ゴラオン组 第４４話 赤い髪の女',
            0x54: 'ゴラオン组 第４５話 神か、悪魔か・・・',
            0x55: 'スーパー系 第４６話 龍と虎',
            0x56: 'リアル系 第４６話 第三の力',
            0x57: '共通 第４７話 男の戦い',
            0x58: '共通 第５０話 ヴァリアブル・フォーメーション',
            0x59: 'グラン・ガラン组 第５１話 ガラスの王国',
            0x5A: 'ラー・カイラム组 第５１話 ダカールの日',
            0x5B: 'グラン・ガラン组 第５２話 王国崩壊',
            0x5C: 'ラー・カイラム组 第５２話 バイブレーション',
            0x5D: 'ゴラオン组 第５４話 思い出を未来へ',
            0x5E: 'ラー・カイラム组 第５３話 ソロモン攻略戦',
            0x5F: 'ラー・カイラム组 第５４話 女たちの戦場',
            0x60: 'ラー・カイラム组 第５５話 駆け抜ける嵐',
            0x61: 'ゴラオン组 第５１話 あしゅら男爵、散る',
            0x62: 'ゴラオン组 第５２話 魔神皇帝',
            0x63: 'グラン・ガラン组 第５３話 クロス・ファイト',
            0x64: 'グラン・ガラン组 第５４話 異邦人たちの帰還',
            0x65: 'ゴラオン组 第５３話 地球を賭けた一騎討ち',
            0x66: '共通 第５６話 ジオンの幻像',
            0x67: 'ゴラオン组 第５５話 父の胸の中で泣け！',
            0x68: 'グラン・ガラン组 第５５話 女王リリーナ',
            0x69: '共通 第５７話 天使の輪の上で',
            0x6A: 'アクシズ 第５８話 神の国への誘惑',
            0x6B: 'アクシズ 第５９話 クロス・目标机师',
            0x6C: 'アクシズ 第６０話 戦士、再び・・・',
            0x6D: 'エンジェル・ハイロゥ 第５８話 勝者と敗者に祝福を',
            0x6E: 'エンジェル・ハイロゥ 第５９話 せめて、人間らしく',
            0x6F: 'エンジェル・ハイロゥ 第６０話 最後のシ者',
            0x70: '共通 第６１話 運命の矢',
            0x71: '共通 第６２話 愛・おぼえていますか',
            0x72: '共通 第６４話 Ａｉｒ',
            0x73: '共通 第６５話 ギア・オブ・デスティニー',
            0x74: '熟練度４５以上 第６６話 絶望の宴は今から始まる',
            0x75: '熟練度４５以上 第６７話 この星の明日のために',
            0x77: '熟練度４５未満 第６６話 人類に逃げ場なし',
            0x78: '熟練度４５未満 第６７話 鋼の魂',
            0x7C: '共通 第２８話 EOTの島',
            0x7D: 'スーパー系 第２９話 心に念じる見えない刃',
            0x7E: 'リアル系 第２９話 黒い超闘士',
            0x7F: '共通 第４８話 誰がために鐘は鳴る',
            0x80: '共通 第４９話 進路に光明、退路に絶望',
            0x81: '力ずくで撃退 第３０話 精霊憑依',
        }
        self.SCRIPT = {
            0x00: ['[0x00]プロローグ 关后'],
            0x01: ['[0x01]鋼鉄のコクピット 关前'],
            0x02: ['[0x01]鋼鉄のコクピット 关后'],
            0x03: ['[0x02]マジンガーＺ絶体絶命 关前'],
            0x04: ['[0x02]マジンガーＺ絶体絶命 关后'],
            0x05: ['[0x03]ゲッターチーム出撃せよ！ 关前'],
            0x06: ['[0x03]ゲッターチーム出撃せよ！ 关后'],
            0x07: ['[0x04]ジオン再臨 关前'],
            0x08: ['[0x04]ジオン再臨 关后'],
            0x09: ['[0x05]シークレット・ナンバーズ 关前'],
            0x0A: ['[0x05]シークレット・ナンバーズ 关后'],
            0x0B: ['[0x06]アーガマ撃墜命令 关前'],
            0x0C: ['[0x06]アーガマ撃墜命令 关后'],
            0x0D: ['[0x07]バニシング・トルーパー 关前'],
            0x0E: ['[0x07]バニシング・トルーパー 关后'],
            0x0F: ['[0x08]黒いガンダム 关前'],
            0x10: ['[0x08]黒いガンダム 关后'],
            0x11: ['[0x09]ホワイトベース救出 关前'],
            0x12: ['[0x09]ホワイトベース救出 关后'],
            0x13: ['[0x0A]死神と呼ばれたＧ 关前'],
            0x14: ['[0x0A]死神と呼ばれたＧ 关后'],
            0x15: ['[0x0B]ジオンの亡霊 关前'],
            0x16: ['[0x0B]ジオンの亡霊 关后'],
            0x17: ['[0x0C]対決、極東基地 关前'],
            0x18: ['[0x0C]対決、極東基地 关后'],
            0x19: ['[0x0D]レッツ！コンバイン 关前'],
            0x1A: ['[0x0D]レッツ！コンバイン 关后'],
            0x1B: ['[0x0E]出撃！その名はジャイアント・ロボ 关前'],
            0x1C: ['[0x0E]出撃！その名はジャイアント・ロボ 关后'],
            0x1D: ['[0x0F]風を呼ぶ者 关前'],
            0x1E: ['[0x0F]風を呼ぶ者 关后'],
            0x1F: ['[0x10]未知なる災い 关前'],
            0x20: ['[0x10]未知なる災い 关后'],
            0x21: ['[0x11]アムロ再び 关前'],
            0x22: ['[0x11]アムロ再び 关后'],
            0x23: ['[0x12]白いモビルスーツ 关前'],
            0x24: ['[0x12]白いモビルスーツ 关后'],
            0x25: ['[0x13]戦いは誰のために 关前'],
            0x26: ['[0x13]戦いは誰のために 关后'],
            0x27: ['[0x14]翼を持ったガンダム 关前'],
            0x28: ['[0x14]翼を持ったガンダム 关后'],
            0x29: ['[0x15]目覚めよ、勇者 关前'],
            0x2A: ['[0x15]目覚めよ、勇者 关后'],
            0x2B: ['[0x16]ガンダム強奪 关前'],
            0x2C: ['[0x16]ガンダム強奪 关后'],
            0x2D: ['[0x17]野望の男 关前'],
            0x2E: ['[0x17]野望の男 关后'],
            0x2F: ['[0x18]少女が見た流星 关前'],
            0x30: ['[0x18]少女が見た流星 关后'],
            0x31: ['[0x19]父との約束 关前'],
            0x32: ['[0x19]父との約束 关后'],
            0x33: ['[0x1A]使徒、襲来 关前'],
            0x34: ['[0x1A]使徒、襲来 关后'],
            0x35: ['[0x1B]咆哮、ＥＶＡ初号機 关前'],
            0x36: ['[0x1B]咆哮、ＥＶＡ初号機 关后'],
            0x37: ['[0x1C]ＧＲ対ＧＲ２ 关前'],
            0x38: ['[0x1C]ＧＲ対ＧＲ２ 关后'],
            0x39: ['[0x1D]ゼータの鼓動 关前'],
            0x3A: ['[0x1D]ゼータの鼓動 关后'],
            0x3B: ['[0x1E]第二次直上会議 关前'],
            0x3C: ['[0x1E]第二次直上会議 关后'],
            0x3D: ['[0x1F]紅い稲妻　空飛ぶマジンガー 关前'],
            0x3E: ['[0x1F]紅い稲妻　空飛ぶマジンガー 关后'],
            0x3F: ['[0x20]激突！ゲッターロボＶＳゲッターロボＧ 关前'],
            0x40: ['[0x20]激突！ゲッターロボＶＳゲッターロボＧ 关后'],
            0x41: ['[0x21]決戦、第２新東京市 关前'],
            0x42: ['[0x21]決戦、第２新東京市 幕间'],
            0x43: ['[0x21]決戦、第２新東京市 关后'],
            0x44: ['[0x22]圣战士たち 关前'],
            0x45: ['[0x22]圣战士たち 幕间'],
            0x46: ['[0x22]圣战士たち 关后'],
            0x47: ['[0x23]エレの霊力 关前'],
            0x48: ['[0x23]エレの霊力 关后'],
            0x49: ['[0x24]ナの国の女王 关前'],
            0x4A: ['[0x24]ナの国の女王 关后'],
            0x4B: ['[0x25]オーラロード 关前'],
            0x4C: ['[0x25]オーラロード 关后'],
            0x4D: ['[0x26]東京上空 关后'],
            0x4E: ['[0x27]獣を超え、人を超え、いでよ神の戦士 关前'],
            0x4F: ['[0x27]獣を超え、人を超え、いでよ神の戦士 关后'],
            0x50: ['[0x28]戦いの海へ 关前'],
            0x51: ['[0x28]戦いの海へ 关后'],
            0x52: ['[0x29]マジンガーＺ対暗黒大将軍 关前'],
            0x53: ['[0x29]マジンガーＺ対暗黒大将軍 幕间'],
            0x54: ['[0x29]マジンガーＺ対暗黒大将軍 关后'],
            0x55: ['[0x2A]ボルテス起死回生 关前'],
            0x56: ['[0x2A]ボルテス起死回生 关后'],
            0x57: ['[0x2B]シャーキン悪魔の戦い 关前'],
            0x58: ['[0x2B]シャーキン悪魔の戦い 关后'],
            0x59: ['[0x31]紅いエヴァンゲリオン 关前'],
            0x5A: ['[0x31]紅いエヴァンゲリオン 关后'],
            0x5B: ['[0x2C]ホンコン・シティ 关前'],
            0x5C: ['[0x2C]ホンコン・シティ 关后'],
            0x5D: ['[0x2D]ガンダム、星の海へ 关前'],
            0x5E: ['[0x2D]ガンダム、星の海へ 关后'],
            0x5F: ['[0x2E]始動ダブルゼータ 关前'],
            0x60: ['[0x2E]始動ダブルゼータ 关后'],
            0x61: ['[0x2F]ソロモンの悪夢 关前'],
            0x62: ['[0x2F]ソロモンの悪夢 关后'],
            0x63: ['[0x30]クロスボーン・バンガード 关前'],
            0x64: ['[0x30]クロスボーン・バンガード 关后'],
            0x65: ['[0x32]海からのマレビト 关前'],
            0x66: ['[0x32]海からのマレビト 关后'],
            0x67: ['[0x33]マシン展開 关前'],
            0x68: ['[0x33]マシン展開 关后'],
            0x69: ['[0x7C]ＥＯＴの島 关前'],
            0x6A: ['[0x7C]ＥＯＴの島 关后'],
            0x6B: ['[0x7D]心に念じる見えない刃 关前'],
            0x6C: ['[0x7D]心に念じる見えない刃 关后'],
            0x6D: ['[0x7E]黒い超闘士 关前'],
            0x6E: ['[0x7E]黒い超闘士 关后'],
            0x6F: ['[0x34]瞬間、心重ねて 关前'],
            0x70: ['[0x34]瞬間、心重ねて 关后'],
            0x71: ['[0x81]精霊憑依 关前'],
            0x72: ['[0x81]精霊憑依 关后'],
            0x73: ['[0x35]ブービー・トラップ 关前'],
            0x74: ['[0x35]ブービー・トラップ 关后'],
            0x75: ['[0x36]カウント・ダウン 关后'],
            0x76: ['[0x37]トランス・フォーメーション 关前'],
            0x77: ['[0x37]トランス・フォーメーション 关后'],
            0x78: ['[0x38]隠された殺意 关前'],
            0x79: ['[0x38]隠された殺意 关后'],
            0x7A: ['[0x39]サタン・ファイト 关前'],
            0x7B: ['[0x3A]リン・ミンメイ 关后'],
            0x7C: ['[0x3B]ジュピトリアン 关前'],
            0x7D: ['[0x3B]ジュピトリアン 关后'],
            0x7E: ['[0x3C]帝国の女王 关前'],
            0x7F: ['[0x3C]帝国の女王 关后'],
            0x80: ['[0x3D]終末への前奏曲 关前'],
            0x81: ['[0x3D]終末への前奏曲 关后'],
            0x82: ['[0x3E]奇跡の価値は 关前'],
            0x83: ['[0x3E]奇跡の価値は 关后'],
            0x84: ['[0x3F]スペース・フォールド 关后'],
            0x85: ['[0x40]アームド・アタック 关前'],
            0x86: ['[0x40]アームド・アタック 关后'],
            0x87: ['[0x41]天敵との遭遇 关前'],
            0x88: ['[0x41]天敵との遭遇 关后'],
            0x89: ['[0x42]イングラムの真意 关前'],
            0x8A: ['[0x42]イングラムの真意 关后'],
            0x8B: ['[0x43]ミス・マクロス 关前'],
            0x8C: ['[0x43]ミス・マクロス 关后'],
            0x8D: ['[0x44]木星からの逃亡者 关前'],
            0x8E: ['[0x44]木星からの逃亡者 关后'],
            0x8F: ['[0x45]人類を導く者 关前'],
            0x90: ['[0x45]人類を導く者 关后'],
            0x91: ['[0x46]ファースト・コンタクト 关前'],
            0x92: ['[0x46]ファースト・コンタクト 关后'],
            0x93: ['[0x47]ビッグ・エスケープ 关前'],
            0x94: ['[0x47]ビッグ・エスケープ 关后'],
            0x95: ['[0x48]バイバイ・マルス 关前'],
            0x96: ['[0x48]バイバイ・マルス 关后'],
            0x97: ['[0x49]アクシズからの使者 关前'],
            0x98: ['[0x49]アクシズからの使者 关后'],
            0x99: ['[0x4A]プルとアクシズと 关前'],
            0x9A: ['[0x4B]リィナの血 关前'],
            0x9B: ['[0x4B]リィナの血 关后'],
            0x9C: ['[0x4C]漆黒の天使来たりて 关前'],
            0x9D: ['[0x4C]漆黒の天使来たりて 关后'],
            0x9E: ['[0x4D]ジュピター・ゴースト 关前'],
            0x9F: ['[0x4D]ジュピター・ゴースト 关后'],
            0xA0: ['[0x4E]宇宙に咲く妖花 关前'],
            0xA1: ['[0x4E]宇宙に咲く妖花 关后'],
            0xA2: ['[0x4F]ゼロと呼ばれたガンダム 关前'],
            0xA3: ['[0x4F]ゼロと呼ばれたガンダム 关后'],
            0xA4: ['[0x50]強襲、阻止限界点 关前'],
            0xA5: ['[0x50]強襲、阻止限界点 关后'],
            0xA6: ['[0x51]父よ地球は近い 关前'],
            0xA7: ['[0x51]父よ地球は近い 关后'],
            0xA8: ['[0x52]静止した闇の中で 关前'],
            0xA9: ['[0x52]静止した闇の中で 关后'],
            0xAA: ['[0x53]赤い髪の女 关前'],
            0xAB: ['[0x53]赤い髪の女 关后'],
            0xAC: ['[0x54]神か、悪魔か・・・ 关前'],
            0xAD: ['[0x54]神か、悪魔か・・・ 关后'],
            0xAE: ['[0x56]第三の力 关前'],
            0xAF: ['[0x56]第三の力 关后'],
            0xB0: ['[0x55]龍と虎 关前'],
            0xB1: ['[0x55]龍と虎 关后'],
            0xB2: ['[0x57]男の戦い 关前'],
            0xB3: ['[0x57]男の戦い 关后'],
            0xB4: ['[0x7F]誰がために鐘は鳴る 关前'],
            0xB5: ['[0x80]進路に光明、退路に絶望 关前'],
            0xB6: ['[0x80]進路に光明、退路に絶望 关后'],
            0xB7: ['[0x58]ヴァリアブル・フォーメーション 关前'],
            0xB8: ['[0x58]ヴァリアブル・フォーメーション 关后'],
            0xB9: ['[0x59]ガラスの王国 关前'],
            0xBA: ['[0x59]ガラスの王国 关后'],
            0xBB: ['[0x5B]王国崩壊 关前'],
            0xBC: ['[0x5B]王国崩壊 关后'],
            0xBD: ['[0x63]クロス・ファイト 关前'],
            0xBE: ['[0x63]クロス・ファイト 关后'],
            0xBF: ['[0x64]異邦人たちの帰還 关前'],
            0xC0: ['[0x64]異邦人たちの帰還 关后'],
            0xC1: ['[0x68]女王リリーナ 关前'],
            0xC2: ['[0x68]女王リリーナ 关后'],
            0xC3: ['[0x5A]ダカールの日 关前'],
            0xC4: ['[0x5A]ダカールの日 关后'],
            0xC5: ['[0x5C]バイブレーション 关前'],
            0xC6: ['[0x5C]バイブレーション 关后'],
            0xC7: ['[0x5E]ソロモン攻略戦 关前'],
            0xC8: ['[0x5E]ソロモン攻略戦 关后'],
            0xC9: ['[0x5F]女たちの戦場 关前'],
            0xCA: ['[0x5F]女たちの戦場 关后'],
            0xCB: ['[0x60]駆け抜ける嵐 关前'],
            0xCC: ['[0x60]駆け抜ける嵐 关后'],
            0xCD: ['[0x61]あしゅら男爵、散る 关前'],
            0xCE: ['[0x61]あしゅら男爵、散る 关后'],
            0xCF: ['[0x62]魔神皇帝 关前'],
            0xD0: ['[0x62]魔神皇帝 关后'],
            0xD1: ['[0x65]地球を賭けた一騎討ち 关前'],
            0xD2: ['[0x65]地球を賭けた一騎討ち 关后'],
            0xD3: ['[0x5D]思い出を未来へ 关前'],
            0xD4: ['[0x5D]思い出を未来へ 关后'],
            0xD5: ['[0x67]父の胸の中で泣け！ 关前'],
            0xD6: ['[0x67]父の胸の中で泣け！ 关后'],
            0xD7: ['[0x66]ジオンの幻像 关前'],
            0xD8: ['[0x66]ジオンの幻像 关后'],
            0xD9: ['[0x69]天使の輪の上で 关前'],
            0xDA: ['[0x69]天使の輪の上で 关后'],
            0xDB: ['[0x6A]神の国への誘惑 关前'],
            0xDC: ['[0x6A]神の国への誘惑 关后'],
            0xDD: ['[0x6B]クロス・目标机师 关前'],
            0xDE: ['[0x6B]クロス・目标机师 关后'],
            0xDF: ['[0x6C]戦士、再び・・・ 关前'],
            0xE0: ['[0x6C]戦士、再び・・・ 关后'],
            0xE1: ['[0x6D]勝者と敗者に祝福を 关前'],
            0xE2: ['[0x6D]勝者と敗者に祝福を 关后'],
            0xE3: ['[0x6E]せめて、人間らしく 关前'],
            0xE4: ['[0x6E]せめて、人間らしく 关后'],
            0xE5: ['[0x6F]最後のシ者 关前'],
            0xE6: ['[0x6F]最後のシ者 幕间'],
            0xE7: ['[0x6F]最後のシ者 关后'],
            0xE8: ['[0x70]運命の矢 关前'],
            0xE9: ['[0x70]運命の矢 关后'],
            0xEA: ['[0x71]愛・おぼえていますか 关前'],
            0xEB: ['[0x71]愛・おぼえていますか 幕间'],
            0xEC: ['[0x71]愛・おぼえていますか 关后'],
            0xED: ['[0x76]終わりの始まり 关前'],
            0xEE: ['[0x76]終わりの始まり 关后'],
            0xEF: ['[0x72]Ａｉｒ 关前'],
            0xF0: ['[0x72]Ａｉｒ 幕间'],
            0xF1: ['[0x72]Ａｉｒ 关后'],
            0xF2: ['[0x73]ギア・オブ・デスティニー 关前'],
            0xF3: ['[0x73]ギア・オブ・デスティニー 关后'],
            0xF4: ['[0x74]絶望の宴は今から始まる 关前'],
            0xF5: ['[0x74]絶望の宴は今から始まる 关后'],
            0xF6: ['[0x75]この星の明日のために 关前'],
            0xF7: ['[0x75]この星の明日のために 幕间'],
            0xF8: ['[0x75]この星の明日のために 关后'],
            0xF9: ['[0x79]エンディング'],
            0xFA: ['[0x77]人類に逃げ場なし 关前'],
            0xFB: ['[0x78]鋼の魂 关前'],
            0xFC: ['[0x78]鋼の魂 幕间'],
            0xFD: ['[0x78]鋼の魂 关后'],
        }
        self.PART = {
            0x00: '一一',
            0x01: 'ブースター',
            0x02: 'メガブースター',
            0x03: 'アポジモーター',
            0x04: 'マグネットコーティング',
            0x05: 'バイオセンサー',
            0x06: 'サイコフレーム',
            0x07: 'ハロ',
            0x08: 'チョバムアーマー',
            0x09: 'ハイブリッドアーマー',
            0x0A: '超合金Ｚ',
            0x0B: '超合金ニューZ',
            0x0C: '高性能レーダー',
            0x0D: '高性能照準器',
            0x0E: 'ミノフスキークラフト',
            0x0F: 'ミノフスキードライブ',
            0x10: 'テム＝レイの回路',
            0x11: '対ビームコーティング',
            0x12: 'Iフィールド発生装置',
            0x13: 'ピンポイントバリア',
            0x14: 'イナーシャルキャンセラー',
            0x15: 'ミンメイ人形',
            0x16: 'アンドロメダ焼き',
            0x17: 'プロペラントタンク',
            0x18: 'プロペラントタンクＳ',
            0x19: 'リペアキット',
            0x1A: 'リペアキットＳ',
        }
        self.MUSIC = {
            0x00: 'コン・バトラーVのテーマ',
            0x01: '熱風！疾風！サイバスター',
            0x02: 'ダークプリズン',
            0x03: 'フラッパー・ガール',
            0x04: 'バーニング・ラブ',
            0x05: 'カムヒア！ダイターン3',
            0x06: 'ダンバインとぶ',
            0x07: '彼方へ',
            0x08: 'Invisible',
            0x09: '',
            0x0A: '黄昏の戦場',
            0x0B: '絶望の宴',
            0x0C: '全能たる調停者',
            0x0D: 'DECISIVE BATTLE',
            0x0E: 'A STEP FORWARD INTO TERROR',
            0x0F: 'EVA-02',
            0x10: 'THE BEAST II',
            0x11: '交響曲 第9番 ニ短調 第4楽章 より',
            0x12: '残酷な天使のテーゼ',
            0x13: '魂のルフラン',
            0x14: 'THE WINNER',
            0x15: 'MEN OF DESTINY',
            0x16: '出撃！その名はジャイアント・ロボ！',
            0x17: 'メイン・タイトル',
            0x18: 'MAIN TITLE',
            0x19: 'ゲッターロボ！',
            0x1A: 'F91ガンダム出撃',
            0x1B: '赤い彗星',
            0x1C: 'STAND UP TO THE VICTORY',
            0x1D: "DON'T STOP! CARRY ON!",
            0x1E: 'JUST COMMUNICATION',
            0x1F: 'RHYTHM EMOTION',
            0x20: 'WHITE REFLECTION',
            0x21: 'モビルスーツ戦 敵機襲来',
            0x22: '艦组戦',
            0x23: '宇宙を駆ける ゼータ発動',
            0x24: 'サイレントヴォイス',
            0x25: '運命の矢',
            0x26: '勝利と敗北の狭間で',
            0x27: 'この星の明日のために',
            0x28: '進路に光明、退路に絶望',
            0x29: '揺れる照星',
            0x2A: 'それぞれの大義のために',
            0x2B: '虚空からの使者',
            0x2C: '忌むべき訪問者',
            0x2D: 'ドッグ・ファイター',
            0x2E: '総攻撃',
            0x2F: '50万年の戦い',
            0x30: 'DOG FIGHT',
            0x31: 'おれはグレートマジンガー',
            0x32: 'マジンガ-Z',
            0x33: 'マジンカイザー',
            0x34: '勇者ライディーン',
            0x35: 'ACE ATTACKER',
            0x36: '我ニ敵ナシ',
            0x37: 'VANISHING TROOPER',
            0x38: '鋼鉄のコクピット',
            0x39: 'EVERYWHERE YOU GO',
            0x3A: 'ICE MAN',
            0x3B: 'PSYCHIC ENERGY',
            0x3C: 'BANPRESTO!',
            0x3D: 'MARIONETTE MESSIAH',
            0x3E: 'THE ARROW OF DESTINY',
            0x3F: '鋼の魂～SUPER ROBOT SPIRITS',
            0x40: 'TIME DIVER',
            0x41: '荒ぶる魂！！',
            0x42: '',
            0x43: '遠い日の安息',
            0x44: '誰がために鐘は踊る',
            0x45: '苦難の先に待つものは',
            0x46: '開かれた砲門',
            0x47: '一つの結末',
            0x48: '災い来たりて',
            0x49: '悲しい記憶',
            0x4A: '修羅の予感',
            0x4B: 'トップをねらえ！ ～Fly High～',
            0x4C: '作戦开始',
            0x4D: '危機',
            0x4E: 'ボルテスⅤの歌',
            0x4F: 'レッツ・コンバイン！',
            0x50: 'ダイターン3の名のもとに',
            0x51: '破嵐万丈',
            0x52: '水の星へ愛を込めて',
            0x53: '私の彼は机师',
            0x54: '愛・おぼえていますか',
            0x55: 'マクロス',
            0x56: '愛・おぼえていますか',
            0x57: '愛・おぼえていますか',
            0x58: 'Zのテーマ',
            0x59: '空飛ぶマジンガーZ',
            0x5A: 'マジンカイザー',
            0x5B: 'オレは洸だ',
            0x5C: 'ガンバスター',
        }
        self.SPIRIT = {
            0x00: '熱血',
            0x01: '魂',
            0x02: 'てかげん',
            0x03: '狙撃',
            0x04: 'ひらめき',
            0x05: '努力',
            0x06: '幸運',
            0x07: '集中',
            0x08: '必中',
            0x09: '鉄壁',
            0x0A: '隠れ身',
            0x0B: '加速',
            0x0C: '覚醒',
            0x0D: '激闘',
            0x0E: '捨て身',
            0x0F: 'かく乱',
            0x10: '挑発',
            0x11: '根性',
            0x12: 'ド根性',
            0x13: '気合',
            0x14: '信頼',
            0x15: '友情',
            0x16: '愛',
            0x17: '補給',
            0x18: '再動',
            0x19: '復活',
            0x1A: '脱力',
            0x1B: '戦慄',
            0x1C: '自爆',
            0x1D: '偵察',
            0x1E: '激励',
            0x1F: '大激励',
            0x20: '期待',
            0x21: '奇跡',
            0x22: '奇襲',
            0xFF: '一一',
        }
        self.ROBOT = dict()
        self.ROBOT['移动类型'] = ['空', '陸', '海', '地']
        self.ROBOT['体积'] = {0x0: 'SS', 0x1: 'S', 0x2: 'M', 0x3: 'L', 0x4: 'LL'}
        self.ROBOT['换乘系'] = [
            'ガンダム系(UC)',
            'ガンダム系(W)',
            'マジンガー系',
            'ダンバイン系',
            'ダンバイン系(妖精)',
            'マクロス系',
            'オリジナル系(リアル)',
            'ライディーン系',
            'ゼロシステム',
            'ダイターン系',
        ]
        self.ROBOT['特性'] = [
            'A.T.フィールド',
            'オーラバリア',
            'グラビティ・テリトリー',
            'ピンポイントバリア',
            'グラビティ・ウォール',
            '念動フィールド',
            'イナーシャルキャンセラー',
            'Iフィールド（ν）',
            'Iフィールド',
            'ビームコート',
            '盾装備',
            '剣装備',
            '補給装置',
            '修理装置',
            '分身',
            'HP回復(小)',
            'HP回復(大)',
            'EN回復(小)',
            'EN回復(大)',
            'マジンパワー',
            '暴走',
            '精霊憑依',
            'ゼロシステム',
            'S2機関',
            '変形',
            '合体',
            '分離',
            'アンビリカルケーブル',
            'VTOL属性',
            '量産',
            '搭載・発進',
        ]
        self.ROBOT['適応'] = {0x0: 'ー', 0x1: 'D', 0x2: 'C', 0x3: 'B', 0x4: 'A'}
        self.ROBOT['换装系统'] = {0x0: 'V2ガンダム', 0x1: 'ヒュッケバインMK-Ⅲ', 0xFF: '一一'}

        self.WEAPON = dict()
        self.WEAPON['分类'] = {0x0: '格斗', 0x1: '射击'}
        self.WEAPON['改造类型'] = {0x0: '[A]', 0x1: '[B]', 0x2: '[C]', 0x3: '[D]'}
        self.WEAPON['地图武器分类'] = {0x0: '一一', 0x1: '方向指定型', 0x2: '自機中心型', 0x3: '着弾地点指定型'}
        self.WEAPON['属性'] = ['Ⓟ', 'Ⓑ', '切り払', 'ボトム射出', 'ビット類', '突貫', '敵味方識別']
        self.WEAPON['適応'] = {0x0: 'ー', 0x1: 'C', 0x2: 'B', 0x3: 'A'}

        self.PILOT = dict()
        self.PILOT['换乘系'] = [
            'ガンダム系(UC)',
            'ガンダム系(W)',
            'マジンガー系',
            'ダンバイン系',
            'ダンバイン系(妖精)',
            'マクロス系',
            'オリジナル系(リアル)',
            'ライディーン系',
            'ゼロシステム',
            'ダイターン系',
        ]
        self.PILOT['特殊技能'] = [
            '底力', '天才', 'ガッツ', '野生化', '集中力', 'SP回復', '社長', '勇者', '王子', '王女', 'エース', '', '主役', 'サイボーグ', 'シンクロ', '妖精']
        self.PILOT['性格'] = {0x0: '弱気', 0x1: '普通', 0x2: '強気', 0x3: '超強気'}
        self.PILOT['適応'] = self.ROBOT.get('適応')
        self.PILOT['技能'] = {
            0x0: '新人类',
            0x1: '強化人間',
            0x2: '圣战士',
            0x3: '念動力',
            0x4: 'シールド防御',
            0x5: '切り払い',
            0xFF: '一一'
        }

        self.COMMAND = dict()
        self.COMMAND['比较'] = {0x0: '>', 0x1: '≥', 0x2: '=', 0x3: '≤', 0x4: '<'}
        self.COMMAND['触发'] = {0x0: '未触发', 0x1: '已触发'}
        self.COMMAND['阵营'] = {0x0: '中立', 0x1: '本方', 0x2: '友军', 0x3: '敌方'}
        self.COMMAND['点数'] = {0x0: '熟练度', 0x1: '恋爱度', 0x2: '宿敌度', 0x3: '未知', 0x5: '明美点', 0x6: '未沙点'}
        self.COMMAND['菜单'] = ['移動', '攻撃', '精神', '変形', '分離', '合体', '説得', '地上', '水中', '空中', '地中', '水上',
                              '芯片', '修理', '補給', '接続', '切断', '待機', '搭載', '発進', '能力']
        self.COMMAND['演出'] = ['会心', '护盾', '破盾'],
        self.COMMAND['简介'] = {
            0x00: '区块 - 区块号 BLOCK',
            0x01: '区块 - 结束符 STOP',
            0x02: '条件 - 单项判断 IF',
            0x03: '条件 - 多项判断 ANY',
            0x04: '条件 - 判断为真 THEN',
            0x05: '条件 - 判断为假 ELSE',
            0x06: '条件 - 判断结束 ENDIF',
            0x08: '流程 - 跳转定位 GOTO',
            0x09: '流程 - 执行定位 RUN',
            0x0A: '流程 - 执行回调 RETURN',
            0x0B: '流程 - 载入配置 LOAD',
            0x0C: '事件 - 触发全局事件',
            0x0D: '事件 - 触发场景事件',
            0x0E: '事件 - 操作场景点数',
            0x0F: '事件 - 操作全局点数',
            0x10: '事件 - 判断全局事件',
            0x11: '事件 - 判断场景事件',
            0x12: '事件 - 场景点数比较',
            0x13: '事件 - 全局点数比较',
            0x14: '判断 - 真实系为真',
            0x15: '判断 - 超级系为真',
            0x16: '判断 - 必定返回假',
            0x17: '文本 - 普通会话',
            0x18: '文本 - 变量会话',
            0x19: '文本 - 语音会话',
            0x1A: '文本 - 最终话不同主角对战BOSS切换',
            0x1B: '文本 - 最终话主角对战BOSS会话',
            0x1C: '文本 - 播放音乐会话',
            0x1D: '文本 - 停止音乐会话',
            0x1E: '文本 - 胜利与失败文本',
            0x1F: '文本 - 选项会话',
            0x21: '文本 - 判断选项',
            0x22: '剧情 - 场景胜利',
            0x23: '剧情 - 场景失败',
            0x24: '剧情 - 选择下一关卡',
            0x25: '剧情 - 判断当前回合数',
            0x26: '剧情 - 设定场景音乐',
            0x27: '剧情 - 播放指定音乐',
            0x28: '剧情 - 场景音乐复位',
            0x29: '剧情 - 播放音效',
            0x2A: '剧情 - 播放动画',
            0x2B: '剧情 - 静止等待',
            0x2C: '出击 - 敌方列表组出击',
            0x2D: '出击 - 敌方列表组出击到机师相对坐标',
            0x2F: '出击 - 敌方列表组再次出击',
            0x30: '机库 - 机库开启',
            0x31: '机库 - 机库关闭',
            0x32: '机库 - 增加机体',
            0x33: '机库 - 机体离队',
            0x34: '机库 - 机体归队',
            0x35: '机库 - 刪除机体',
            0x36: '机库 - 替换机体',
            0x37: '机库 - 增加机师',
            0x38: '机库 - 机师离队',
            0x39: '机库 - 机师归队',
            0x3A: '机库 - 删除机师',
            0x3B: '机库 - 替换机师',
            0x3C: '未知',
            0x3D: '机库 - 增加机体机师或强制换乘',
            0x3E: '机库 - 机师分流',
            0x3F: '机库 - 机体合流',
            0x40: '机库 - 机师合流',
            0x41: '机库 - 机体归队',
            0x42: '机库 - 机师离队',
            0x43: '机库 - 强制换乘',
            0x44: '机库 - 换乘空机体',
            0x45: '机库 - 取消机师乘坐',
            0x46: '机库 - 增加机体',
            0x47: '机库 - 机师强制出场',
            0x48: '机库 - 指定妖精搭配',
            0x49: '机库 - 隐藏机师',
            0x4A: '机库 - 隐藏机体',
            0x4B: '机库 - 换乘空机体',
            0x4E: '机库 - 合体允许分离',
            0x4F: '出击 - 出击开启',
            0x50: '出击 - 出击关闭',
            0x51: '出击 - 机师出击到绝对坐标',
            0x52: '出击 - 机师出击到相对坐标',
            0x54: '出击 - 机体出击到绝对坐标',
            0x55: '出击 - 机体出击到相对坐标',
            0x57: '出击 - 本方部队出击到绝对坐标',
            0x58: '出击 - 本方部队出击到相对坐标',
            0x5A: '出击 - 本方母舰出击到绝对坐标',
            0x5B: '机师 - 设定机师等级',
            0x5C: '机师 - 增加机师等级',
            0x5D: '机师 - 设定机师击坠',
            0x5E: '机师 - 增加机师击坠',
            0x5F: '阵营 - 敌方机师加入',
            0x60: '阵营 - 设定机师阵营',
            0x61: '资源 - 增加芯片',
            0x62: '未知',
            0x63: '未知',
            0x64: '资源 - 增加资金',
            0x65: '复活 - 复活机师',
            0x66: '复活 - 复活机体',
            0x67: '移动 - 移动机师到绝对坐标',
            0x68: '移动 - 移动机师到相对坐标',
            0x69: '移动 - 移动机师到敌方坐标',
            0x6A: '移动 - 移动光标到绝对坐标',
            0x6B: '移动 - 移动光标到相对坐标',
            0x6C: '移动 - 移动光标到绝对坐标后闪烁',
            0x6E: '移动 - 屏幕静止',
            0x6F: '撤退 - 指定机师撤退',
            0x70: '撤退 - 敌方单位撤退',
            0x71: '撤退 - 敌方小组撤退',
            0x72: '撤退 - 指定势力撤退',
            0x73: '撤退 - 指定阵营撤退',
            0x74: '撤退 - 指定阵营撤退到坐标区域',
            0x75: '判断 - 机师状态',
            0x77: '判断 - 机体状态',
            0x78: '判断 - 机师是否搭载',
            0x79: '判断 - 敌方小组剩余数量',
            0x7A: '判断 - 指定势力剩余数量',
            0x7B: '判断 - 指定阵营剩余数量',
            0x7C: '判断 - 指定机师位于坐标区域',
            0x7D: '判断 - 敌方单位位于坐标区域',
            0x7E: '判断 - 指定机体位于坐标区域',
            0x80: '判断 - 指定势力位于坐标区域',
            0x81: '判断 - 指定阵营位于坐标区域',
            0x82: '判断 - 指定机师坐标间的距离',
            0x83: '判断 - 指定机师与敌方单位距离',
            0x84: '调整 - 调整机师气力',
            0x85: '调整 - 调整阵营气力',
            0x86: '调整 - 调整机师EN',
            0x87: '未知',
            0x88: '调整 - 调整人物HP',
            0x89: '调整 - 调整阵营HP',
            0x8B: '调整 - 调整阵营SP',
            0x8C: '连接 - EVA机师电缆连接到坐标',
            0x8D: '连接 - EVA机师电缆连接到机师',
            0x8E: '连接 - EVA机师电缆就近连接',
            0x8F: '连接 - EVA机师电缆强制断开',
            0x90: '移动 - 移动机师到绝对坐标',
            0x91: '移动 - 移动敌方单位到绝对坐标',
            0x92: '移动 - 移动机师到相对坐标',
            0x93: '移动 - 移动机师到敌方坐标',
            0x94: '移动 - 移动敌方单位到相对坐标',
            0x96: '演出 - 指定机师强制攻击指定机师',
            0x97: '演出 - 敌方单位强制攻击指定机师',
            0x98: '演出 - 指定机师强制攻击敌方单位',
            0x99: '演出 - 演出关闭',
            0x9A: '规则 - 允许指定势力攻击指定势力',
            0x9B: '规则 - 禁止指定势力攻击指定势力',
            0x9C: '规则 - 禁用指定机师菜单选项',
            0x9D: '规则 - 禁用敌方单位菜单选项',
            0x9E: '规则 - 启用指定机师菜单选项',
            0x9F: '规则 - 指定机师强制击破',
            0xA0: '规则 - 指定敌方单位强制击破',
            0xA1: '规则 - 指定机师为搭载状态',
            0xA2: '规则 - 指定机师为未搭载状态',
            0xA3: '操作 - 指定机师浮上',
            0xA4: '操作 - 指定机师着地',
            0xA5: '操作 - 指定机师强制变形',
            0xA6: '操作 - 指定机师强制合体',
            0xA7: '操作 - 指定机师强制分离',
            0xA8: '操作 - 指定机师使用精神',
            0xA9: '操作 - 指定机师调整行动状态',
            0xAA: '操作 - EVA机师切换傀儡系统',
            0xAB: '操作 - 指定机师增加说得指定机师菜单选项',
            0xAC: '操作 - 指定机师增加说得敌方单位菜单选项',
            0xAD: '判断 - 指定机师说得指定机师',
            0xAE: '判断 - 指定机师说得敌方单位',
            0xAF: '判断 - 指定机师交战指定机师',
            0xB0: '判断 - 指定机师交战敌方单位',
            0xB1: '判断 - 指定机师攻击',
            0xB2: '判断 - 敌方单位被击破',
            0xB3: '判断 - 指定机师被击破',
            0xB4: '判断 - 指定机体被击破',
            0xB5: '未知',
            0xB6: '判断 - 指定机师HP量',
            0xB7: '判断 - 指定机师被击破',
            0xB8: '判断 - 敌方单位未击破',
            0xB9: '演出 - 相对坐标特殊演出',
            0xBA: '演出 - 绝对坐标地图演出',
            0xBB: '演出 - 相对坐标地图演出',
        }
