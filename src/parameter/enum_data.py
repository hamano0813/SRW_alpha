#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide6.QtCore import QObject


# noinspection PyUnresolvedReferences
class EnumDataTrans(QObject):
    def __init__(self):
        super(EnumDataTrans, self).__init__(parent=None)
        self.SCENARIO = {
            0x00: ('[00]', '共通', '第０話', 'プロローグ'),
            0x01: ('[01]', self.tr('スーパー系'), '第１話', '鋼鉄のコクピット'),
            0x02: ('[02]', 'スーパー系', '第２話', 'マジンガーＺ絶体絶命'),
            0x03: ('[03]', 'スーパー系', '第３話', 'ゲッターチーム出撃せよ！'),
            0x04: ('[04]', 'スーパー系', '第４話', 'ジオン再臨'),
            0x05: ('[05]', 'スーパー系', '第５話', 'シークレット・ナンバーズ'),
            0x06: ('[06]', 'スーパー系', '第６話', 'アーガマ撃墜命令'),
            0x07: ('[07]', 'リアル系', '第１話', 'バニシング・トルーパー'),
            0x08: ('[08]', 'リアル系', '第２話', '黒いガンダム'),
            0x09: ('[09]', 'リアル系', '第３話', 'ホワイトベース救出'),
            0x0A: ('[0A]', 'リアル系', '第４話', '死神と呼ばれたＧ'),
            0x0B: ('[0B]', 'リアル系', '第５話', 'ジオンの亡霊'),
            0x0C: ('[0C]', 'リアル系', '第６話', '対決、極東基地'),
            0x0D: ('[0D]', '共通', '第７話', 'レッツ！コンバイン'),
            0x0E: ('[0E]', '共通', '第８話', '出撃！その名はジャイアント・ロボ'),
            0x0F: ('[0F]', 'スーパー系', '第９話', '風を呼ぶ者'),
            0x10: ('[10]', 'リアル系', '第９話', '未知なる災い'),
            0x11: ('[11]', 'ジャブロー', '第１０話', 'アムロ再び'),
            0x12: ('[12]', 'ジャブロー', '第１１話', '白いモビルスーツ'),
            0x13: ('[13]', 'ジャブロー', '第１２話', '戦いは誰のために'),
            0x14: ('[14]', 'ジャブロー', '第１３話', '翼を持ったガンダム'),
            0x15: ('[15]', '南アタリア島', '第１０話', '目覚めよ、勇者'),
            0x16: ('[16]', '南アタリア島', '第１１話', 'ガンダム強奪'),
            0x17: ('[17]', '南アタリア島', '第１２話', '野望の男'),
            0x18: ('[18]', '南アタリア島', '第１３話', '少女が見た流星'),
            0x19: ('[19]', '共通', '第１４話', '父との約束'),
            0x1A: ('[1A]', '共通', '第１５話', '使徒、襲来'),
            0x1B: ('[1B]', '共通', '第１６話', '咆哮、ＥＶＡ初号機'),
            0x1C: ('[1C]', '共通', '第１７話', 'ＧＲ対ＧＲ２'),
            0x1D: ('[1D]', 'リアル系', '第１８話', 'ゼータの鼓動'),
            0x1E: ('[1E]', 'リアル系', '第１９話', '第二次直上会戦'),
            0x1F: ('[1F]', 'スーパー系', '第１８話', '紅い稲妻 空飛ぶマジンガー'),
            0x20: ('[20]', 'スーパー系', '第１９話', '激突！ゲッターロボＶＳゲッターロボＧ'),
            0x21: ('[21]', '共通', '第２０話幕前', '決戦、第２新東京市'),
            0x22: ('[22]', '共通', '第２０話', '決戦、第２新東京市'),
            0x23: ('[23]', 'ＥＶＡ弐号機', '第２１話幕前', '圣战士たち'),
            0x24: ('[24]', 'ＥＶＡ弐号機', '第２１話', '圣战士たち'),
            0x25: ('[25]', 'ＥＶＡ弐号機', '第２２話', 'エレの霊力'),
            0x26: ('[24]', 'ＥＶＡ弐号機', '第２３話', 'ナの国の女王'),
            0x27: ('[25]', 'ＥＶＡ弐号機', '第２４話', 'オーラロード'),
            0x28: ('[26]', 'ＥＶＡ弐号機', '第２５話', '東京上空'),
            0x29: ('[27]', '極東基地', '第２１話', '獣を超え、人を超え、いでよ神の戦士'),
            0x2A: ('[28]', '極東基地', '第２２話', '戦いの海へ'),
            0x2B: ('[29]', '極東基地', '第２３話第１幕', 'マジンガーＺ対暗黒大将軍'),
            0x2C: ('[29]', '極東基地', '第２３話第２幕', 'マジンガーＺ対暗黒大将軍'),
            0x2D: ('[2A]', '極東基地', '第２４話', 'ボルテス起死回生'),
            0x2E: ('[2B]', '極東基地', '第２５話', 'シャーキン悪魔の戦い'),
            0x2F: ('[2C]', '宇宙', '第２１話', 'ホンコン・シティ'),
            0x30: ('[2D]', '宇宙', '第２２話', 'ガンダム、星の海へ'),
            0x31: ('[2E]', '宇宙', '第２３話', '始動ダブルゼータ'),
            0x32: ('[2F]', '宇宙', '第２４話', 'ソロモンの悪夢'),
            0x33: ('[30]', '宇宙', '第２５話', 'クロスボーン・バンガード'),
            0x34: ('[31]', 'ＥＶＡ弐号機／極東基地', '第２６話', '紅いエヴァンゲリオン'),
            0x35: ('[32]', '宇宙', '第２６話', '海からのマレビト'),
            0x36: ('[33]', '共通', '第２７話', 'マシン展開'),
            0x37: ('[34]', 'ＥＶＡ２体同時攻撃', '第３０話', '瞬間、心重ねて'),
            0x38: ('[35]', '弾丸を撃ち落す', '第３１話', 'ブービー・トラップ'),
            0x39: ('[36]', '弾丸を撃ち落す', '第３２話', 'カウント・ダウン'),
            0x3A: ('[37]', '弾丸を撃ち落す', '第３３話', 'トランス・フォーメーション'),
            0x3B: ('[38]', '弾丸を撃ち落す', '第３４話', '隠された殺意'),
            0x3C: ('[39]', '弾丸を撃ち落す', '第３５話', 'サタン・ファイト'),
            0x3D: ('[3A]', '弾丸を撃ち落す', '第３６話', 'リン・ミンメイ'),
            0x3E: ('[3B]', '弾丸を撃ち落す', '第３７話', 'ジュピトリアン'),
            0x3F: ('[3C]', '弾丸を撃ち落す', '第３８話', '帝国の女王'),
            0x40: ('[3D]', '弾丸を撃ち落す', '第３９話', '終末への前奏曲'),
            0x41: ('[3E]', 'ＥＶＡで受け止める', '第３１話', '奇跡の価値は'),
            0x42: ('[3F]', 'ＥＶＡで受け止める', '第３２話', 'スペース・フォールド'),
            0x43: ('[40]', 'ＥＶＡで受け止める', '第３３話', 'アームド・アタック'),
            0x44: ('[41]', 'ＥＶＡで受け止める', '第３４話', '天敵との遭遇'),
            0x45: ('[42]', 'ＥＶＡで受け止める', '第３５話', 'イングラムの真意'),
            0x46: ('[43]', 'ＥＶＡで受け止める', '第３６話', 'ミス・マクロス'),
            0x47: ('[44]', 'ＥＶＡで受け止める', '第３７話', '木星からの逃亡者'),
            0x48: ('[45]', 'ＥＶＡで受け止める', '第３８話', '人類を導く者'),
            0x49: ('[46]', 'ＥＶＡで受け止める', '第３９話', 'ファースト・コンタクト'),
            0x4A: ('[47]', '共通', '第４０話', 'ビッグ・エスケープ'),
            0x4B: ('[48]', '共通', '第４１話', 'バイバイ・マルス'),
            0x4C: ('[49]', 'リーンホースＪｒ．隊', '第４２話', 'アクシズからの使者'),
            0x4D: ('[4A]', 'リーンホースＪｒ．隊', '第４３話', 'プルとアクシズと'),
            0x4E: ('[4B]', 'リーンホースＪｒ．隊', '第４４話', 'リィナの血'),
            0x4F: ('[4C]', 'リーンホースＪｒ．隊', '第４５話', '漆黒の天使来たりて'),
            0x50: ('[4D]', 'グラン・ガラン隊', '第４２話', 'ジュピター・ゴースト'),
            0x51: ('[4E]', 'グラン・ガラン隊', '第４３話', '宇宙に咲く妖花'),
            0x52: ('[4F]', 'グラン・ガラン隊', '第４４話', 'ゼロと呼ばれたガンダム'),
            0x53: ('[50]', 'グラン・ガラン隊', '第４５話', '強襲、阻止限界点'),
            0x54: ('[51]', 'ゴラオン隊', '第４２話', '父よ地球は近い'),
            0x55: ('[52]', 'ゴラオン隊', '第４３話', '静止した闇の中で'),
            0x56: ('[53]', 'ゴラオン隊', '第４４話', '赤い髪の女'),
            0x57: ('[54]', 'ゴラオン隊', '第４５話', '神か、悪魔か・・・'),
            0x58: ('[55]', 'スーパー系', '第４６話', '龍と虎'),
            0x59: ('[56]', 'リアル系', '第４６話', '第三の力'),
            0x5A: ('[57]', '共通', '第４７話', '男の戦い'),
            0x5B: ('[58]', '共通', '第５０話', 'ヴァリアブル・フォーメーション'),
            0x5C: ('[59]', 'グラン・ガラン隊', '第５１話', 'ガラスの王国'),
            0x5D: ('[5A]', 'ラー・カイラム隊', '第５１話', 'ダカールの日'),
            0x5E: ('[5B]', 'グラン・ガラン隊', '第５２話', '王国崩壊'),
            0x5F: ('[5C]', 'ラー・カイラム隊', '第５２話', 'バイブレーション'),
            0x60: ('[5D]', 'ゴラオン隊', '第５４話', '思い出を未来へ'),
            0x61: ('[5E]', 'ラー・カイラム隊', '第５３話', 'ソロモン攻略戦'),
            0x62: ('[5F]', 'ラー・カイラム隊', '第５４話', '女たちの戦場'),
            0x63: ('[60]', 'ラー・カイラム隊', '第５５話', '駆け抜ける嵐'),
            0x64: ('[61]', 'ゴラオン隊', '第５１話', 'あしゅら男爵、散る'),
            0x65: ('[62]', 'ゴラオン隊', '第５２話', '魔神皇帝'),
            0x66: ('[63]', 'グラン・ガラン隊', '第５３話', 'クロス・ファイト'),
            0x67: ('[64]', 'グラン・ガラン隊', '第５４話', '異邦人たちの帰還'),
            0x68: ('[65]', 'ゴラオン隊', '第５３話', '地球を賭けた一騎討ち'),
            0x69: ('[66]', '共通', '第５６話', 'ジオンの幻像'),
            0x6A: ('[67]', 'ゴラオン隊', '第５５話', '父の胸の中で泣け！'),
            0x6B: ('[68]', 'グラン・ガラン隊', '第５５話', '女王リリーナ'),
            0x6C: ('[69]', '共通', '第５７話第０幕', '天使の輪の上で'),
            0x6D: ('[69]', '共通', '第５７話', '天使の輪の上で'),
            0x6E: ('[6A]', 'アクシズ', '第５８話', '神の国への誘惑'),
            0x6F: ('[6B]', 'アクシズ', '第５９話', 'クロス・ターゲット'),
            0x70: ('[6C]', 'アクシズ', '第６０話', '戦士、再び・・・'),
            0x71: ('[6D]', 'エンジェル・ハイロゥ', '第５８話', '勝者と敗者に祝福を'),
            0x72: ('[6E]', 'エンジェル・ハイロゥ', '第５９話', 'せめて、人間らしく'),
            0x73: ('[6F]', 'エンジェル・ハイロゥ', '第６０話', '最後のシ者'),
            0x74: ('[70]', '共通', '第６１話', '運命の矢'),
            0x75: ('[71]', '共通', '第６２話第１幕', '愛・おぼえていますか'),
            0x76: ('[71]', '共通', '第６２話第２幕', '愛・おぼえていますか'),
            0x77: ('[72]', '共通', '第６４話第１幕', 'Air'),
            0x78: ('[72]', '共通', '第６４話第２幕', 'Air'),
            0x79: ('[73]', '共通', '第６５話', 'ギア・オブ・デスティニー'),
            0x7A: ('[74]', '熟練度４５以上', '第６６話', '絶望の宴は今から始まる'),
            0x7B: ('[75]', '熟練度４５以上', '第６７話第１幕', 'この星の明日のために'),
            0x7C: ('[75]', '熟練度４５以上', '第６７話第２幕', 'この星の明日のために'),
            0x7D: ('[75]', '熟練度４５以上', '第６７話第３幕', 'この星の明日のために'),
            0x7E: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x7F: ('[77]', '熟練度４５未満', '第６６話', '人類に逃げ場なし'),
            0x80: ('[78]', '熟練度４５未満', '第６７話第１幕', '鋼の魂'),
            0x81: ('[78]', '熟練度４５未満', '第６７話第２幕', '鋼の魂'),
            0x82: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x83: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x84: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x85: ('ダミー', 'ダミー', 'ダミー', 'ダミー'),
            0x86: ('[7C]', '共通', '第２８話', 'ＥＯＴの島'),
            0x87: ('[7D]', 'スーパー系', '第２９話', '心に念じる見えない刃'),
            0x88: ('[7E]', 'リアル系', '第２９話', '黒い超闘士'),
            0x89: ('[7F]', '共通', '第４８話', '誰がために鐘は鳴る'),
            0x8A: ('[80]', '共通', '第４９話', '進路に光明、退路に絶望'),
            0x8B: ('[81]', '力ずくで撃退', '第３０話', '精霊憑依'),
        }
        self.STAGE = {
            0x00: '[00]共通 第０話 プロローグ',
            0x01: '[01]スーパー系 第１話 鋼鉄のコクピット',
            0x02: '[02]スーパー系 第２話 マジンガーＺ絶体絶命',
            0x03: '[03]スーパー系 第３話 ゲッターチーム出撃せよ！',
            0x04: '[04]スーパー系 第４話 ジオン再臨',
            0x05: '[05]スーパー系 第５話 シークレット・ナンバーズ',
            0x06: '[06]スーパー系 第６話 アーガマ撃墜命令',
            0x07: '[07]リアル系 第１話 バニシング・トルーパー',
            0x08: '[08]リアル系 第２話 黒いガンダム',
            0x09: '[09]リアル系 第３話 ホワイトベース救出',
            0x0A: '[0A]リアル系 第４話 死神と呼ばれたＧ',
            0x0B: '[0B]リアル系 第５話 ジオンの亡霊',
            0x0C: '[0C]リアル系 第６話 対決、極東基地',
            0x0D: '[0D]共通 第７話 レッツ！コンバイン',
            0x0E: '[0E]共通 第８話 出撃！その名はジャイアント・ロボ',
            0x0F: '[0F]スーパー系 第９話 風を呼ぶ者',
            0x10: '[10]リアル系 第９話 未知なる災い',
            0x11: '[11]ジャブロー 第１０話 アムロ再び',
            0x12: '[12]ジャブロー 第１１話 白いモビルスーツ',
            0x13: '[13]ジャブロー 第１２話 戦いは誰のために',
            0x14: '[14]ジャブロー 第１３話 翼を持ったガンダム',
            0x15: '[15]南アタリア島 第１０話 目覚めよ、勇者',
            0x16: '[16]南アタリア島 第１１話 ガンダム強奪',
            0x17: '[17]南アタリア島 第１２話 野望の男',
            0x18: '[18]南アタリア島 第１３話 少女が見た流星',
            0x19: '[19]共通 第１４話 父との約束',
            0x1A: '[1A]共通 第１５話 使徒、襲来',
            0x1B: '[1B]共通 第１６話 咆哮、ＥＶＡ初号機',
            0x1C: '[1C]共通 第１７話 ＧＲ対ＧＲ２',
            0x1D: '[1D]リアル系 第１８話 ゼータの鼓動',
            0x1E: '[1E]リアル系 第１９話 第二次直上会戦',
            0x1F: '[1F]スーパー系 第１８話 紅い稲妻　空飛ぶマジンガー',
            0x20: '[20]スーパー系 第１９話 激突！ゲッターロボＶＳゲッターロボＧ',
            0x21: '[21]共通 第２０話 決戦、第２新東京市',
            0x22: '[22]ＥＶＡ弐号機 第２１話 圣战士たち',
            0x23: '[23]ＥＶＡ弐号機 第２２話 エレの霊力',
            0x24: '[24]ＥＶＡ弐号機 第２３話 ナの国の女王',
            0x25: '[25]ＥＶＡ弐号機 第２４話 オーラロード',
            0x26: '[26]ＥＶＡ弐号機 第２５話 東京上空',
            0x27: '[27]極東基地 第２１話 獣を超え、人を超え、いでよ神の戦士',
            0x28: '[28]極東基地 第２２話 戦いの海へ',
            0x29: '[29]極東基地 第２３話 マジンガーＺ対暗黒大将軍',
            0x2A: '[2A]極東基地 第２４話 ボルテス起死回生',
            0x2B: '[2B]極東基地 第２５話 シャーキン悪魔の戦い',
            0x2C: '[2C]宇宙 第２１話 ホンコン・シティ',
            0x2D: '[2D]宇宙 第２２話 ガンダム、星の海へ',
            0x2E: '[2E]宇宙 第２３話 始動ダブルゼータ',
            0x2F: '[2F]宇宙 第２４話 ソロモンの悪夢',
            0x30: '[30]宇宙 第２５話 クロスボーン・バンガード',
            0x31: '[31]ＥＶＡ弐号機／極東基地 第２６話 紅いエヴァンゲリオン',
            0x32: '[32]宇宙 第２６話 海からのマレビト',
            0x33: '[33]共通 第２７話 マシン展開',
            0x34: '[34]ＥＶＡ２体同時攻撃 第３０話 瞬間、心重ねて',
            0x35: '[35]弾丸を撃ち落す 第３１話 ブービー・トラップ',
            0x36: '[36]弾丸を撃ち落す 第３２話 カウント・ダウン',
            0x37: '[37]弾丸を撃ち落す 第３３話 トランス・フォーメーション',
            0x38: '[38]弾丸を撃ち落す 第３４話 隠された殺意',
            0x39: '[39]弾丸を撃ち落す 第３５話 サタン・ファイト',
            0x3A: '[3A]弾丸を撃ち落す 第３６話 リン・ミンメイ',
            0x3B: '[3B]弾丸を撃ち落す 第３７話 ジュピトリアン',
            0x3C: '[3C]弾丸を撃ち落す 第３８話 帝国の女王',
            0x3D: '[3D]弾丸を撃ち落す 第３９話 終末への前奏曲',
            0x3E: '[3E]ＥＶＡで受け止める 第３１話 奇跡の価値は',
            0x3F: '[3F]ＥＶＡで受け止める 第３２話 スペース・フォールド',
            0x40: '[40]ＥＶＡで受け止める 第３３話 アームド・アタック',
            0x41: '[41]ＥＶＡで受け止める 第３４話 天敵との遭遇',
            0x42: '[42]ＥＶＡで受け止める 第３５話 イングラムの真意',
            0x43: '[43]ＥＶＡで受け止める 第３６話 ミス・マクロス',
            0x44: '[44]ＥＶＡで受け止める 第３７話 木星からの逃亡者',
            0x45: '[45]ＥＶＡで受け止める 第３８話 人類を導く者',
            0x46: '[46]ＥＶＡで受け止める 第３９話 ファースト・コンタクト',
            0x47: '[47]共通 第４０話 ビッグ・エスケープ',
            0x48: '[48]共通 第４１話 バイバイ・マルス',
            0x49: '[49]リーンホースＪｒ．隊 第４２話 アクシズからの使者',
            0x4A: '[4A]リーンホースＪｒ．隊 第４３話 プルとアクシズと',
            0x4B: '[4B]リーンホースＪｒ．隊 第４４話 リィナの血',
            0x4C: '[4C]リーンホースＪｒ．隊 第４５話 漆黒の天使来たりて',
            0x4D: '[4D]グラン・ガラン隊 第４２話 ジュピター・ゴースト',
            0x4E: '[4E]グラン・ガラン隊 第４３話 宇宙に咲く妖花',
            0x4F: '[4F]グラン・ガラン隊 第４４話 ゼロと呼ばれたガンダム',
            0x50: '[50]グラン・ガラン隊 第４５話 強襲、阻止限界点',
            0x51: '[51]ゴラオン隊 第４２話 父よ地球は近い',
            0x52: '[52]ゴラオン隊 第４３話 静止した闇の中で',
            0x53: '[53]ゴラオン隊 第４４話 赤い髪の女',
            0x54: '[54]ゴラオン隊 第４５話 神か、悪魔か・・・',
            0x55: '[55]スーパー系 第４６話 龍と虎',
            0x56: '[56]リアル系 第４６話 第三の力',
            0x57: '[57]共通 第４７話 男の戦い',
            0x58: '[58]共通 第５０話 ヴァリアブル・フォーメーション',
            0x59: '[59]グラン・ガラン隊 第５１話 ガラスの王国',
            0x5A: '[5A]ラー・カイラム隊 第５１話 ダカールの日',
            0x5B: '[5B]グラン・ガラン隊 第５２話 王国崩壊',
            0x5C: '[5C]ラー・カイラム隊 第５２話 バイブレーション',
            0x5D: '[5D]ゴラオン隊 第５４話 思い出を未来へ',
            0x5E: '[5E]ラー・カイラム隊 第５３話 ソロモン攻略戦',
            0x5F: '[5F]ラー・カイラム隊 第５４話 女たちの戦場',
            0x60: '[60]ラー・カイラム隊 第５５話 駆け抜ける嵐',
            0x61: '[61]ゴラオン隊 第５１話 あしゅら男爵、散る',
            0x62: '[62]ゴラオン隊 第５２話 魔神皇帝',
            0x63: '[63]グラン・ガラン隊 第５３話 クロス・ファイト',
            0x64: '[64]グラン・ガラン隊 第５４話 異邦人たちの帰還',
            0x65: '[65]ゴラオン隊 第５３話 地球を賭けた一騎討ち',
            0x66: '[66]共通 第５６話 ジオンの幻像',
            0x67: '[67]ゴラオン隊 第５５話 父の胸の中で泣け！',
            0x68: '[68]グラン・ガラン隊 第５５話 女王リリーナ',
            0x69: '[69]共通 第５７話 天使の輪の上で',
            0x6A: '[6A]アクシズ 第５８話 神の国への誘惑',
            0x6B: '[6B]アクシズ 第５９話 クロス・ターゲット',
            0x6C: '[6C]アクシズ 第６０話 戦士、再び・・・',
            0x6D: '[6D]エンジェル・ハイロゥ 第５８話 勝者と敗者に祝福を',
            0x6E: '[6E]エンジェル・ハイロゥ 第５９話 せめて、人間らしく',
            0x6F: '[6F]エンジェル・ハイロゥ 第６０話 最後のシ者',
            0x70: '[70]共通 第６１話 運命の矢',
            0x71: '[71]共通 第６２話 愛・おぼえていますか',
            0x72: '[72]共通 第６４話 Ａｉｒ',
            0x73: '[73]共通 第６５話 ギア・オブ・デスティニー',
            0x74: '[74]熟練度４５以上 第６６話 絶望の宴は今から始まる',
            0x75: '[75]熟練度４５以上 第６７話 この星の明日のために',
            0x77: '[77]熟練度４５未満 第６６話 人類に逃げ場なし',
            0x78: '[78]熟練度４５未満 第６７話 鋼の魂',
            0x79: '[79]共通 エンドデモ エンディング',
            0x7A: '',
            0x7B: '',
            0x7C: '[7C]共通 第２８話 ＥＯＴの島',
            0x7D: '[7D]スーパー系 第２９話 心に念じる見えない刃',
            0x7E: '[7E]リアル系 第２９話 黒い超闘士',
            0x7F: '[7F]共通 第４８話 誰がために鐘は鳴る',
            0x80: '[80]共通 第４９話 進路に光明、退路に絶望',
            0x81: '[81]力ずくで撃退 第３０話 精霊憑依',
        }
        self.SCRIPT = {
            0x00: ('[00]', '共通', '第０話', 'プロローグ', '关后',),
            0x01: ('[01]', 'スーパー系', '第１話', '鋼鉄のコクピット', '关前',),
            0x02: ('[01]', 'スーパー系', '第１話', '鋼鉄のコクピット', '关后',),
            0x03: ('[02]', 'スーパー系', '第２話', 'マジンガーＺ絶体絶命', '关前',),
            0x04: ('[02]', 'スーパー系', '第２話', 'マジンガーＺ絶体絶命', '关后',),
            0x05: ('[03]', 'スーパー系', '第３話', 'ゲッターチーム出撃せよ！', '关前',),
            0x06: ('[03]', 'スーパー系', '第３話', 'ゲッターチーム出撃せよ！', '关后',),
            0x07: ('[04]', 'スーパー系', '第４話', 'ジオン再臨', '关前',),
            0x08: ('[04]', 'スーパー系', '第４話', 'ジオン再臨', '关后',),
            0x09: ('[05]', 'スーパー系', '第５話', 'シークレット・ナンバーズ', '关前',),
            0x0A: ('[05]', 'スーパー系', '第５話', 'シークレット・ナンバーズ', '关后',),
            0x0B: ('[06]', 'スーパー系', '第６話', 'アーガマ撃墜命令', '关前',),
            0x0C: ('[06]', 'スーパー系', '第６話', 'アーガマ撃墜命令', '关后',),
            0x0D: ('[07]', 'リアル系', '第１話', 'バニシング・トルーパー', '关前',),
            0x0E: ('[07]', 'リアル系', '第１話', 'バニシング・トルーパー', '关后',),
            0x0F: ('[08]', 'リアル系', '第２話', '黒いガンダム', '关前',),
            0x10: ('[08]', 'リアル系', '第２話', '黒いガンダム', '关后',),
            0x11: ('[09]', 'リアル系', '第３話', 'ホワイトベース救出', '关前',),
            0x12: ('[09]', 'リアル系', '第３話', 'ホワイトベース救出', '关后',),
            0x13: ('[0A]', 'リアル系', '第４話', '死神と呼ばれたＧ', '关前',),
            0x14: ('[0A]', 'リアル系', '第４話', '死神と呼ばれたＧ', '关后',),
            0x15: ('[0B]', 'リアル系', '第５話', 'ジオンの亡霊', '关前',),
            0x16: ('[0B]', 'リアル系', '第５話', 'ジオンの亡霊', '关后',),
            0x17: ('[0C]', 'リアル系', '第６話', '対決、極東基地', '关前',),
            0x18: ('[0C]', 'リアル系', '第６話', '対決、極東基地', '关后',),
            0x19: ('[0D]', '共通', '第７話', 'レッツ！コンバイン', '关前',),
            0x1A: ('[0D]', '共通', '第７話', 'レッツ！コンバイン', '关后',),
            0x1B: ('[0E]', '共通', '第８話', '出撃！その名はジャイアント・ロボ', '关前',),
            0x1C: ('[0E]', '共通', '第８話', '出撃！その名はジャイアント・ロボ', '关后',),
            0x1D: ('[0F]', 'スーパー系', '第９話', '風を呼ぶ者', '关前',),
            0x1E: ('[0F]', 'スーパー系', '第９話', '風を呼ぶ者', '关后',),
            0x1F: ('[10]', 'リアル系', '第９話', '未知なる災い', '关前',),
            0x20: ('[10]', 'リアル系', '第９話', '未知なる災い', '关后',),
            0x21: ('[11]', 'ジャブロー', '第１０話', 'アムロ再び', '关前',),
            0x22: ('[11]', 'ジャブロー', '第１０話', 'アムロ再び', '关后',),
            0x23: ('[12]', 'ジャブロー', '第１１話', '白いモビルスーツ', '关前',),
            0x24: ('[12]', 'ジャブロー', '第１１話', '白いモビルスーツ', '关后',),
            0x25: ('[13]', 'ジャブロー', '第１２話', '戦いは誰のために', '关前',),
            0x26: ('[13]', 'ジャブロー', '第１２話', '戦いは誰のために', '关后',),
            0x27: ('[14]', 'ジャブロー', '第１３話', '翼を持ったガンダム', '关前',),
            0x28: ('[14]', 'ジャブロー', '第１３話', '翼を持ったガンダム', '关后',),
            0x29: ('[15]', '南アタリア島', '第１０話', '目覚めよ、勇者', '关前',),
            0x2A: ('[15]', '南アタリア島', '第１０話', '目覚めよ、勇者', '关后',),
            0x2B: ('[16]', '南アタリア島', '第１１話', 'ガンダム強奪', '关前',),
            0x2C: ('[16]', '南アタリア島', '第１１話', 'ガンダム強奪', '关后',),
            0x2D: ('[17]', '南アタリア島', '第１２話', '野望の男', '关前',),
            0x2E: ('[17]', '南アタリア島', '第１２話', '野望の男', '关后',),
            0x2F: ('[18]', '南アタリア島', '第１３話', '少女が見た流星', '关前',),
            0x30: ('[18]', '南アタリア島', '第１３話', '少女が見た流星', '关后',),
            0x31: ('[19]', '共通', '第１４話', '父との約束', '关前',),
            0x32: ('[19]', '共通', '第１４話', '父との約束', '关后',),
            0x33: ('[1A]', '共通', '第１５話', '使徒、襲来', '关前',),
            0x34: ('[1A]', '共通', '第１５話', '使徒、襲来', '关后',),
            0x35: ('[1B]', '共通', '第１６話', '咆哮、ＥＶＡ初号機', '关前',),
            0x36: ('[1B]', '共通', '第１６話', '咆哮、ＥＶＡ初号機', '关后',),
            0x37: ('[1C]', '共通', '第１７話', 'ＧＲ対ＧＲ２', '关前',),
            0x38: ('[1C]', '共通', '第１７話', 'ＧＲ対ＧＲ２', '关后',),
            0x39: ('[1D]', 'リアル系', '第１８話', 'ゼータの鼓動', '关前',),
            0x3A: ('[1D]', 'リアル系', '第１８話', 'ゼータの鼓動', '关后',),
            0x3B: ('[1E]', 'リアル系', '第１９話', '第二次直上会戦', '关前',),
            0x3C: ('[1E]', 'リアル系', '第１９話', '第二次直上会戦', '关后',),
            0x3D: ('[1F]', 'スーパー系', '第１８話', '紅い稲妻　空飛ぶマジンガー', '关前',),
            0x3E: ('[1F]', 'スーパー系', '第１８話', '紅い稲妻　空飛ぶマジンガー', '关后',),
            0x3F: ('[20]', 'スーパー系', '第１９話', '激突！ゲッターロボＶＳゲッターロボＧ', '关前',),
            0x40: ('[20]', 'スーパー系', '第１９話', '激突！ゲッターロボＶＳゲッターロボＧ', '关后',),
            0x41: ('[21]', '共通', '第２０話', '決戦、第２新東京市', '关前',),
            0x42: ('[21]', '共通', '第２０話', '決戦、第２新東京市', '幕间',),
            0x43: ('[21]', '共通', '第２０話', '決戦、第２新東京市', '关后',),
            0x44: ('[22]', 'ＥＶＡ弐号機', '第２１話', '圣战士たち', '关前',),
            0x45: ('[22]', 'ＥＶＡ弐号機', '第２１話', '圣战士たち', '幕间',),
            0x46: ('[22]', 'ＥＶＡ弐号機', '第２１話', '圣战士たち', '关后',),
            0x47: ('[23]', 'ＥＶＡ弐号機', '第２２話', 'エレの霊力', '关前',),
            0x48: ('[23]', 'ＥＶＡ弐号機', '第２２話', 'エレの霊力', '关后',),
            0x49: ('[24]', 'ＥＶＡ弐号機', '第２３話', 'ナの国の女王', '关前',),
            0x4A: ('[24]', 'ＥＶＡ弐号機', '第２３話', 'ナの国の女王', '关后',),
            0x4B: ('[25]', 'ＥＶＡ弐号機', '第２４話', 'オーラロード', '关前',),
            0x4C: ('[25]', 'ＥＶＡ弐号機', '第２４話', 'オーラロード', '关后',),
            0x4D: ('[26]', 'ＥＶＡ弐号機', '第２５話', '東京上空', '关后',),
            0x4E: ('[27]', '極東基地', '第２１話', '獣を超え、人を超え、いでよ神の戦士', '关前',),
            0x4F: ('[27]', '極東基地', '第２１話', '獣を超え、人を超え、いでよ神の戦士', '关后',),
            0x50: ('[28]', '極東基地', '第２２話', '戦いの海へ', '关前',),
            0x51: ('[28]', '極東基地', '第２２話', '戦いの海へ', '关后',),
            0x52: ('[29]', '極東基地', '第２３話', 'マジンガーＺ対暗黒大将軍', '关前',),
            0x53: ('[29]', '極東基地', '第２３話', 'マジンガーＺ対暗黒大将軍', '幕间',),
            0x54: ('[29]', '極東基地', '第２３話', 'マジンガーＺ対暗黒大将軍', '关后',),
            0x55: ('[2A]', '極東基地', '第２４話', 'ボルテス起死回生', '关前',),
            0x56: ('[2A]', '極東基地', '第２４話', 'ボルテス起死回生', '关后',),
            0x57: ('[2B]', '極東基地', '第２５話', 'シャーキン悪魔の戦い', '关前',),
            0x58: ('[2B]', '極東基地', '第２５話', 'シャーキン悪魔の戦い', '关后',),
            0x59: ('[31]', 'ＥＶＡ弐号機／極東基地', '第２６話', '紅いエヴァンゲリオン', '关前',),
            0x5A: ('[31]', 'ＥＶＡ弐号機／極東基地', '第２６話', '紅いエヴァンゲリオン', '关后',),
            0x5B: ('[2C]', '宇宙', '第２１話', 'ホンコン・シティ', '关前',),
            0x5C: ('[2C]', '宇宙', '第２１話', 'ホンコン・シティ', '关后',),
            0x5D: ('[2D]', '宇宙', '第２２話', 'ガンダム、星の海へ', '关前',),
            0x5E: ('[2D]', '宇宙', '第２２話', 'ガンダム、星の海へ', '关后',),
            0x5F: ('[2E]', '宇宙', '第２３話', '始動ダブルゼータ', '关前',),
            0x60: ('[2E]', '宇宙', '第２３話', '始動ダブルゼータ', '关后',),
            0x61: ('[2F]', '宇宙', '第２４話', 'ソロモンの悪夢', '关前',),
            0x62: ('[2F]', '宇宙', '第２４話', 'ソロモンの悪夢', '关后',),
            0x63: ('[30]', '宇宙', '第２５話', 'クロスボーン・バンガード', '关前',),
            0x64: ('[30]', '宇宙', '第２５話', 'クロスボーン・バンガード', '关后',),
            0x65: ('[32]', '宇宙', '第２６話', '海からのマレビト', '关前',),
            0x66: ('[32]', '宇宙', '第２６話', '海からのマレビト', '关后',),
            0x67: ('[33]', '共通', '第２７話', 'マシン展開', '关前',),
            0x68: ('[33]', '共通', '第２７話', 'マシン展開', '关后',),
            0x69: ('[7C]', '共通', '第２８話', 'ＥＯＴの島', '关前',),
            0x6A: ('[7C]', '共通', '第２８話', 'ＥＯＴの島', '关后',),
            0x6B: ('[7D]', 'スーパー系', '第２９話', '心に念じる見えない刃', '关前',),
            0x6C: ('[7D]', 'スーパー系', '第２９話', '心に念じる見えない刃', '关后',),
            0x6D: ('[7E]', 'リアル系', '第２９話', '黒い超闘士', '关前',),
            0x6E: ('[7E]', 'リアル系', '第２９話', '黒い超闘士', '关后',),
            0x6F: ('[34]', 'ＥＶＡ２体同時攻撃', '第３０話', '瞬間、心重ねて', '关前',),
            0x70: ('[34]', 'ＥＶＡ２体同時攻撃', '第３０話', '瞬間、心重ねて', '关后',),
            0x71: ('[81]', '力ずくで撃退', '第３０話', '精霊憑依', '关前',),
            0x72: ('[81]', '力ずくで撃退', '第３０話', '精霊憑依', '关后',),
            0x73: ('[35]', '弾丸を撃ち落す', '第３１話', 'ブービー・トラップ', '关前',),
            0x74: ('[35]', '弾丸を撃ち落す', '第３１話', 'ブービー・トラップ', '关后',),
            0x75: ('[36]', '弾丸を撃ち落す', '第３２話', 'カウント・ダウン', '关后',),
            0x76: ('[37]', '弾丸を撃ち落す', '第３３話', 'トランス・フォーメーション', '关前',),
            0x77: ('[37]', '弾丸を撃ち落す', '第３３話', 'トランス・フォーメーション', '关后',),
            0x78: ('[38]', '弾丸を撃ち落す', '第３４話', '隠された殺意', '关前',),
            0x79: ('[38]', '弾丸を撃ち落す', '第３４話', '隠された殺意', '关后',),
            0x7A: ('[39]', '弾丸を撃ち落す', '第３５話', 'サタン・ファイト', '关前',),
            0x7B: ('[3A]', '弾丸を撃ち落す', '第３６話', 'リン・ミンメイ', '关后',),
            0x7C: ('[3B]', '弾丸を撃ち落す', '第３７話', 'ジュピトリアン', '关前',),
            0x7D: ('[3B]', '弾丸を撃ち落す', '第３７話', 'ジュピトリアン', '关后',),
            0x7E: ('[3C]', '弾丸を撃ち落す', '第３８話', '帝国の女王', '关前',),
            0x7F: ('[3C]', '弾丸を撃ち落す', '第３８話', '帝国の女王', '关后',),
            0x80: ('[3D]', '弾丸を撃ち落す', '第３９話', '終末への前奏曲', '关前',),
            0x81: ('[3D]', '弾丸を撃ち落す', '第３９話', '終末への前奏曲', '关后',),
            0x82: ('[3E]', 'ＥＶＡで受け止める', '第３１話', '奇跡の価値は', '关前',),
            0x83: ('[3E]', 'ＥＶＡで受け止める', '第３１話', '奇跡の価値は', '关后',),
            0x84: ('[3F]', 'ＥＶＡで受け止める', '第３２話', 'スペース・フォールド', '关后',),
            0x85: ('[40]', 'ＥＶＡで受け止める', '第３３話', 'アームド・アタック', '关前',),
            0x86: ('[40]', 'ＥＶＡで受け止める', '第３３話', 'アームド・アタック', '关后',),
            0x87: ('[41]', 'ＥＶＡで受け止める', '第３４話', '天敵との遭遇', '关前',),
            0x88: ('[41]', 'ＥＶＡで受け止める', '第３４話', '天敵との遭遇', '关后',),
            0x89: ('[42]', 'ＥＶＡで受け止める', '第３５話', 'イングラムの真意', '关前',),
            0x8A: ('[42]', 'ＥＶＡで受け止める', '第３５話', 'イングラムの真意', '关后',),
            0x8B: ('[43]', 'ＥＶＡで受け止める', '第３６話', 'ミス・マクロス', '关前',),
            0x8C: ('[43]', 'ＥＶＡで受け止める', '第３６話', 'ミス・マクロス', '关后',),
            0x8D: ('[44]', 'ＥＶＡで受け止める', '第３７話', '木星からの逃亡者', '关前',),
            0x8E: ('[44]', 'ＥＶＡで受け止める', '第３７話', '木星からの逃亡者', '关后',),
            0x8F: ('[45]', 'ＥＶＡで受け止める', '第３８話', '人類を導く者', '关前',),
            0x90: ('[45]', 'ＥＶＡで受け止める', '第３８話', '人類を導く者', '关后',),
            0x91: ('[46]', 'ＥＶＡで受け止める', '第３９話', 'ファースト・コンタクト', '关前',),
            0x92: ('[46]', 'ＥＶＡで受け止める', '第３９話', 'ファースト・コンタクト', '关后',),
            0x93: ('[47]', '共通', '第４０話', 'ビッグ・エスケープ', '关前',),
            0x94: ('[47]', '共通', '第４０話', 'ビッグ・エスケープ', '关后',),
            0x95: ('[48]', '共通', '第４１話', 'バイバイ・マルス', '关前',),
            0x96: ('[48]', '共通', '第４１話', 'バイバイ・マルス', '关后',),
            0x97: ('[49]', 'リーンホースＪｒ．隊', '第４２話', 'アクシズからの使者', '关前',),
            0x98: ('[49]', 'リーンホースＪｒ．隊', '第４２話', 'アクシズからの使者', '关后',),
            0x99: ('[4A]', 'リーンホースＪｒ．隊', '第４３話', 'プルとアクシズと', '关前',),
            0x9A: ('[4B]', 'リーンホースＪｒ．隊', '第４４話', 'リィナの血', '关前',),
            0x9B: ('[4B]', 'リーンホースＪｒ．隊', '第４４話', 'リィナの血', '关后',),
            0x9C: ('[4C]', 'リーンホースＪｒ．隊', '第４５話', '漆黒の天使来たりて', '关前',),
            0x9D: ('[4C]', 'リーンホースＪｒ．隊', '第４５話', '漆黒の天使来たりて', '关后',),
            0x9E: ('[4D]', 'グラン・ガラン隊', '第４２話', 'ジュピター・ゴースト', '关前',),
            0x9F: ('[4D]', 'グラン・ガラン隊', '第４２話', 'ジュピター・ゴースト', '关后',),
            0xA0: ('[4E]', 'グラン・ガラン隊', '第４３話', '宇宙に咲く妖花', '关前',),
            0xA1: ('[4E]', 'グラン・ガラン隊', '第４３話', '宇宙に咲く妖花', '关后',),
            0xA2: ('[4F]', 'グラン・ガラン隊', '第４４話', 'ゼロと呼ばれたガンダム', '关前',),
            0xA3: ('[4F]', 'グラン・ガラン隊', '第４４話', 'ゼロと呼ばれたガンダム', '关后',),
            0xA4: ('[50]', 'グラン・ガラン隊', '第４５話', '強襲、阻止限界点', '关前',),
            0xA5: ('[50]', 'グラン・ガラン隊', '第４５話', '強襲、阻止限界点', '关后',),
            0xA6: ('[51]', 'ゴラオン隊', '第４２話', '父よ地球は近い', '关前',),
            0xA7: ('[51]', 'ゴラオン隊', '第４２話', '父よ地球は近い', '关后',),
            0xA8: ('[52]', 'ゴラオン隊', '第４３話', '静止した闇の中で', '关前',),
            0xA9: ('[52]', 'ゴラオン隊', '第４３話', '静止した闇の中で', '关后',),
            0xAA: ('[53]', 'ゴラオン隊', '第４４話', '赤い髪の女', '关前',),
            0xAB: ('[53]', 'ゴラオン隊', '第４４話', '赤い髪の女', '关后',),
            0xAC: ('[54]', 'ゴラオン隊', '第４５話', '神か、悪魔か・・・', '关前',),
            0xAD: ('[54]', 'ゴラオン隊', '第４５話', '神か、悪魔か・・・', '关后',),
            0xAE: ('[56]', 'リアル系', '第４６話', '第三の力', '关前',),
            0xAF: ('[56]', 'リアル系', '第４６話', '第三の力', '关后',),
            0xB0: ('[55]', 'スーパー系', '第４６話', '龍と虎', '关前',),
            0xB1: ('[55]', 'スーパー系', '第４６話', '龍と虎', '关后',),
            0xB2: ('[57]', '共通', '第４７話', '男の戦い', '关前',),
            0xB3: ('[57]', '共通', '第４７話', '男の戦い', '关后',),
            0xB4: ('[7F]', '共通', '第４８話', '誰がために鐘は鳴る', '关前',),
            0xB5: ('[80]', '共通', '第４９話', '進路に光明、退路に絶望', '关前',),
            0xB6: ('[80]', '共通', '第４９話', '進路に光明、退路に絶望', '关后',),
            0xB7: ('[58]', '共通', '第５０話', 'ヴァリアブル・フォーメーション', '关前',),
            0xB8: ('[58]', '共通', '第５０話', 'ヴァリアブル・フォーメーション', '关后',),
            0xB9: ('[59]', 'グラン・ガラン隊', '第５１話', 'ガラスの王国', '关前',),
            0xBA: ('[59]', 'グラン・ガラン隊', '第５１話', 'ガラスの王国', '关后',),
            0xBB: ('[5B]', 'グラン・ガラン隊', '第５２話', '王国崩壊', '关前',),
            0xBC: ('[5B]', 'グラン・ガラン隊', '第５２話', '王国崩壊', '关后',),
            0xBD: ('[63]', 'グラン・ガラン隊', '第５３話', 'クロス・ファイト', '关前',),
            0xBE: ('[63]', 'グラン・ガラン隊', '第５３話', 'クロス・ファイト', '关后',),
            0xBF: ('[64]', 'グラン・ガラン隊', '第５４話', '異邦人たちの帰還', '关前',),
            0xC0: ('[64]', 'グラン・ガラン隊', '第５４話', '異邦人たちの帰還', '关后',),
            0xC1: ('[68]', 'グラン・ガラン隊', '第５５話', '女王リリーナ', '关前',),
            0xC2: ('[68]', 'グラン・ガラン隊', '第５５話', '女王リリーナ', '关后',),
            0xC3: ('[5A]', 'ラー・カイラム隊', '第５１話', 'ダカールの日', '关前',),
            0xC4: ('[5A]', 'ラー・カイラム隊', '第５１話', 'ダカールの日', '关后',),
            0xC5: ('[5C]', 'ラー・カイラム隊', '第５２話', 'バイブレーション', '关前',),
            0xC6: ('[5C]', 'ラー・カイラム隊', '第５２話', 'バイブレーション', '关后',),
            0xC7: ('[5E]', 'ラー・カイラム隊', '第５３話', 'ソロモン攻略戦', '关前',),
            0xC8: ('[5E]', 'ラー・カイラム隊', '第５３話', 'ソロモン攻略戦', '关后',),
            0xC9: ('[5F]', 'ラー・カイラム隊', '第５４話', '女たちの戦場', '关前',),
            0xCA: ('[5F]', 'ラー・カイラム隊', '第５４話', '女たちの戦場', '关后',),
            0xCB: ('[60]', 'ラー・カイラム隊', '第５５話', '駆け抜ける嵐', '关前',),
            0xCC: ('[60]', 'ラー・カイラム隊', '第５５話', '駆け抜ける嵐', '关后',),
            0xCD: ('[61]', 'ゴラオン隊', '第５１話', 'あしゅら男爵、散る', '关前',),
            0xCE: ('[61]', 'ゴラオン隊', '第５１話', 'あしゅら男爵、散る', '关后',),
            0xCF: ('[62]', 'ゴラオン隊', '第５２話', '魔神皇帝', '关前',),
            0xD0: ('[62]', 'ゴラオン隊', '第５２話', '魔神皇帝', '关后',),
            0xD1: ('[65]', 'ゴラオン隊', '第５３話', '地球を賭けた一騎討ち', '关前',),
            0xD2: ('[65]', 'ゴラオン隊', '第５３話', '地球を賭けた一騎討ち', '关后',),
            0xD3: ('[5D]', 'ゴラオン隊', '第５４話', '思い出を未来へ', '关前',),
            0xD4: ('[5D]', 'ゴラオン隊', '第５４話', '思い出を未来へ', '关后',),
            0xD5: ('[67]', 'ゴラオン隊', '第５５話', '父の胸の中で泣け！', '关前',),
            0xD6: ('[67]', 'ゴラオン隊', '第５５話', '父の胸の中で泣け！', '关后',),
            0xD7: ('[66]', '共通', '第５６話', 'ジオンの幻像', '关前',),
            0xD8: ('[66]', '共通', '第５６話', 'ジオンの幻像', '关后',),
            0xD9: ('[69]', '共通', '第５７話', '天使の輪の上で', '关前',),
            0xDA: ('[69]', '共通', '第５７話', '天使の輪の上で', '关后',),
            0xDB: ('[6A]', 'アクシズ', '第５８話', '神の国への誘惑', '关前',),
            0xDC: ('[6A]', 'アクシズ', '第５８話', '神の国への誘惑', '关后',),
            0xDD: ('[6B]', 'アクシズ', '第５９話', 'クロス・ターゲット', '关前',),
            0xDE: ('[6B]', 'アクシズ', '第５９話', 'クロス・ターゲット', '关后',),
            0xDF: ('[6C]', 'アクシズ', '第６０話', '戦士、再び・・・', '关前',),
            0xE0: ('[6C]', 'アクシズ', '第６０話', '戦士、再び・・・', '关后',),
            0xE1: ('[6D]', 'エンジェル・ハイロゥ', '第５８話', '勝者と敗者に祝福を', '关前',),
            0xE2: ('[6D]', 'エンジェル・ハイロゥ', '第５８話', '勝者と敗者に祝福を', '关后',),
            0xE3: ('[6E]', 'エンジェル・ハイロゥ', '第５９話', 'せめて、人間らしく', '关前',),
            0xE4: ('[6E]', 'エンジェル・ハイロゥ', '第５９話', 'せめて、人間らしく', '关后',),
            0xE5: ('[6F]', 'エンジェル・ハイロゥ', '第６０話', '最後のシ者', '关前',),
            0xE6: ('[6F]', 'エンジェル・ハイロゥ', '第６０話', '最後のシ者', '幕间',),
            0xE7: ('[6F]', 'エンジェル・ハイロゥ', '第６０話', '最後のシ者', '关后',),
            0xE8: ('[70]', '共通', '第６１話', '運命の矢', '关前',),
            0xE9: ('[70]', '共通', '第６１話', '運命の矢', '关后',),
            0xEA: ('[71]', '共通', '第６２話', '愛・おぼえていますか', '关前',),
            0xEB: ('[71]', '共通', '第６２話', '愛・おぼえていますか', '幕间',),
            0xEC: ('[71]', '共通', '第６２話', '愛・おぼえていますか', '关后',),
            0xED: ('[76]', '共通', '第６３話', '終わりの始まり', '关前',),
            0xEE: ('[76]', '共通', '第６３話', '終わりの始まり', '关后',),
            0xEF: ('[72]', '共通', '第６４話', 'Ａｉｒ', '关前',),
            0xF0: ('[72]', '共通', '第６４話', 'Ａｉｒ', '幕间',),
            0xF1: ('[72]', '共通', '第６４話', 'Ａｉｒ', '关后',),
            0xF2: ('[73]', '共通', '第６５話', 'ギア・オブ・デスティニー', '关前',),
            0xF3: ('[73]', '共通', '第６５話', 'ギア・オブ・デスティニー', '关后',),
            0xF4: ('[74]', '熟練度４５以上', '第６６話', '絶望の宴は今から始まる', '关前',),
            0xF5: ('[74]', '熟練度４５以上', '第６６話', '絶望の宴は今から始まる', '关后',),
            0xF6: ('[75]', '熟練度４５以上', '第６７話', 'この星の明日のために', '关前',),
            0xF7: ('[75]', '熟練度４５以上', '第６７話', 'この星の明日のために', '幕间',),
            0xF8: ('[75]', '熟練度４５以上', '第６７話', 'この星の明日のために', '关后',),
            0xF9: ('[79]', '共通', 'エンドデモ', 'エンディング', '终幕',),
            0xFA: ('[77]', '熟練度４５未満', '第６６話', '人類に逃げ場なし', '关前',),
            0xFB: ('[78]', '熟練度４５未満', '第６７話', '鋼の魂', '关前',),
            0xFC: ('[78]', '熟練度４５未満', '第６７話', '鋼の魂', '幕间',),
            0xFD: ('[78]', '熟練度４５未満', '第６７話', '鋼の魂', '关后',),
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
            0x11: '交響曲 第9番 ニ短調 第４楽章 より',
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
            0x22: '艦隊戦',
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
        self.COMMAND['行动'] = {0x0: '行动完毕', 0x1: '尚未行动'}
        self.COMMAND['移动'] = {0x0: '', 0x1: '并进入搭载'}
        self.COMMAND['状态'] = {0x0: '于场景内存在', 0x1: '于场景内退场'}
        self.COMMAND['表情'] = {0: '平静', 1: '高兴', 2: '惊讶', 3: '坚毅', 4: '惊恐', 5: '激动'}
        self.COMMAND['阵营'] = {0x0: '中立', 0x1: '本方', 0x2: '友军', 0x3: '敌方'}
        self.COMMAND['点数'] = {0x0: '熟练度', 0x1: '恋爱度', 0x2: '宿敌度', 0x3: '未知', 0x5: '明美点', 0x6: '未沙点'}
        self.COMMAND['势力'] = self.COMMAND['选项'] = [f'第{i + 1}' for i in range(16)]
        self.COMMAND['演出'] = ['会心', '护盾', '破盾']
        self.COMMAND['菜单'] = ['移動', '攻撃', '精神', '変形', '分離', '合体', '説得', '地上', '水中', '空中', '地中', '水上',
                              '芯片', '修理', '補給', '接続', '切断', '待機', '搭載', '発進', '能力']
