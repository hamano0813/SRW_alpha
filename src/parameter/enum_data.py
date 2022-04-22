#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EnumData:
    SCENARIO = {
        0x00: ('共通', 'プロローグ', '[00]プロローグ'),
        0x01: ('スーパー系', '第１話', '[01]鋼鉄のコクピット'),
        0x02: ('スーパー系', '第２話', '[02]マジンガーＺ絶体絶命'),
        0x03: ('スーパー系', '第３話', '[03]ゲッターチーム出撃せよ！'),
        0x04: ('スーパー系', '第４話', '[04]ジオン再臨'),
        0x05: ('スーパー系', '第５話', '[05]シークレット・ナンバーズ'),
        0x06: ('スーパー系', '第６話', '[06]アーガマ撃墜命令'),
        0x07: ('リアル系', '第１話', '[07]バニシング・トルーパー'),
        0x08: ('リアル系', '第２話', '[08]黒いガンダム'),
        0x09: ('リアル系', '第３話', '[09]ホワイトベース救出'),
        0x0A: ('リアル系', '第４話', '[0A]死神と呼ばれたＧ'),
        0x0B: ('リアル系', '第５話', '[0B]ジオンの亡霊'),
        0x0C: ('リアル系', '第６話', '[0C]対決、極東基地'),
        0x0D: ('共通', '第７話', '[0D]レッツ！コンバイン'),
        0x0E: ('共通', '第８話', '[0E]出撃！その名はジャイアント・ロボ'),
        0x0F: ('スーパー系', '第９話', '[0F]風を呼ぶ者'),
        0x10: ('リアル系', '第９話', '[10]未知なる災い'),
        0x11: ('ジャブロー', '第１０話', '[11]アムロ再び'),
        0x12: ('ジャブロー', '第１１話', '[12]白いモビルスーツ'),
        0x13: ('ジャブロー', '第１２話', '[13]戦いは誰のために'),
        0x14: ('ジャブロー', '第１３話', '[14]翼を持ったガンダム'),
        0x15: ('南アタリア島', '第１０話', '[15]目覚めよ、勇者'),
        0x16: ('南アタリア島', '第１１話', '[16]ガンダム強奪'),
        0x17: ('南アタリア島', '第１２話', '[17]野望の男'),
        0x18: ('南アタリア島', '第１３話', '[18]少女が見た流星'),
        0x19: ('共通', '第１４話', '[19]父との約束'),
        0x1A: ('共通', '第１５話', '[1A]使徒、襲来'),
        0x1B: ('共通', '第１６話', '[1B]咆哮、ＥＶＡ初号機'),
        0x1C: ('共通', '第１７話', '[1C]ＧＲ対ＧＲ２'),
        0x1D: ('リアル系', '第１８話', '[1D]ゼータの鼓動'),
        0x1E: ('リアル系', '第１９話', '[1E]第二次直上会議'),
        0x1F: ('スーパー系', '第１８話', '[1F]紅い稲妻\u3000空飛ぶマジンガー'),
        0x20: ('スーパー系', '第１９話', '[20]激突！ゲッターロボＶＳゲッターロボＧ'),
        0x21: ('共通', '第２０話０', '[21]決戦、第２新東京市'),
        0x22: ('共通', '第２０話', '[22]決戦、第２新東京市'),
        0x23: ('ＥＶＡ弐号機', '第２１話０', '[23]聖戦士たち'),
        0x24: ('ＥＶＡ弐号機', '第２１話', '[24]聖戦士たち'),
        0x25: ('ＥＶＡ弐号機', '第２２話', '[25]エレの霊力'),
        0x26: ('ＥＶＡ弐号機', '第２３話', '[24]ナの国の女王'),
        0x27: ('ＥＶＡ弐号機', '第２４話', '[25]オーラロード'),
        0x28: ('ＥＶＡ弐号機', '第２５話', '[26]東京上空'),
        0x29: ('極東基地', '第２１話', '[27]獣を超え、人を超え、いでよ神の戦士'),
        0x2A: ('極東基地', '第２２話', '[28]戦いの海へ'),
        0x2B: ('極東基地', '第２３話１', '[29]マジンガーＺ対暗黒大将軍'),
        0x2C: ('極東基地', '第２３話２', '[29]マジンガーＺ対暗黒大将軍'),
        0x2D: ('極東基地', '第２４話', '[2A]ボルテス起死回生'),
        0x2E: ('極東基地', '第２５話', '[2B]シャーキン悪魔の戦い'),
        0x2F: ('宇宙', '第２１話', '[2C]ホンコン・シティ'),
        0x30: ('宇宙', '第２２話', '[2D]ガンダム、星の海へ'),
        0x31: ('宇宙', '第２３話', '[2E]始動ダブルゼータ'),
        0x32: ('宇宙', '第２４話', '[2F]ソロモンの悪夢'),
        0x33: ('宇宙', '第２５話', '[30]クロスボーン・バンガード'),
        0x34: ('ＥＶＡ弐号機\n／極東基地', '第２６話', '[31]紅いエヴァンゲリオン'),
        0x35: ('宇宙', '第２６話', '[32]海からのマレビト'),
        0x36: ('共通', '第２７話', '[33]マシン展開'),
        0x37: ('ＥＶＡ２体同時攻撃', '第３０話', '[34]瞬間、心重ねて'),
        0x38: ('弾丸を撃ち落す', '第３１話', '[35]ブービー・トラップ'),
        0x39: ('弾丸を撃ち落す', '第３２話', '[36]カウント・ダウン'),
        0x3A: ('弾丸を撃ち落す', '第３３話', '[37]トランス・フォーメーション'),
        0x3B: ('弾丸を撃ち落す', '第３４話', '[38]隠された殺意'),
        0x3C: ('弾丸を撃ち落す', '第３５話', '[39]サタン・ファイト'),
        0x3D: ('弾丸を撃ち落す', '第３６話', '[3A]リン・ミンメイ'),
        0x3E: ('弾丸を撃ち落す', '第３７話', '[3B]ジュピトリアン'),
        0x3F: ('弾丸を撃ち落す', '第３８話', '[3C]帝国の女王'),
        0x40: ('弾丸を撃ち落す', '第３９話', '[3D]終末への前奏曲'),
        0x41: ('ＥＶＡで受け止める', '第３１話', '[3E]奇跡の価値は'),
        0x42: ('ＥＶＡで受け止める', '第３２話', '[3F]スペース・フォールド'),
        0x43: ('ＥＶＡで受け止める', '第３３話', '[40]アームド・アタック'),
        0x44: ('ＥＶＡで受け止める', '第３４話', '[41]天敵との遭遇'),
        0x45: ('ＥＶＡで受け止める', '第３５話', '[42]イングラムの真意'),
        0x46: ('ＥＶＡで受け止める', '第３６話', '[43]ミス・マクロス'),
        0x47: ('ＥＶＡで受け止める', '第３７話', '[44]木星からの逃亡者'),
        0x48: ('ＥＶＡで受け止める', '第３８話', '[45]人類を導く者'),
        0x49: ('ＥＶＡで受け止める', '第３９話', '[46]ファースト・コンタクト'),
        0x4A: ('共通', '第４０話', '[47]ビッグ・エスケープ'),
        0x4B: ('共通', '第４１話', '[48]バイバイ・マルス'),
        0x4C: ('リーンホースＪｒ．隊', '第４２話', '[49]アクシズからの使者'),
        0x4D: ('リーンホースＪｒ．隊', '第４３話', '[4A]プルとアクシズと'),
        0x4E: ('リーンホースＪｒ．隊', '第４４話', '[4B]リィナの血'),
        0x4F: ('リーンホースＪｒ．隊', '第４５話', '[4C]漆黒の天使来たりて'),
        0x50: ('グラン・ガラン隊', '第４２話', '[4D]ジュピター・ゴースト'),
        0x51: ('グラン・ガラン隊', '第４３話', '[4E]宇宙に咲く妖花'),
        0x52: ('グラン・ガラン隊', '第４４話', '[4F]ゼロと呼ばれたガンダム'),
        0x53: ('グラン・ガラン隊', '第４５話', '[50]強襲、阻止限界点'),
        0x54: ('ゴラオン隊', '第４２話', '[51]父よ地球は近い'),
        0x55: ('ゴラオン隊', '第４３話', '[52]静止した闇の中で'),
        0x56: ('ゴラオン隊', '第４４話', '[53]赤い髪の女'),
        0x57: ('ゴラオン隊', '第４５話', '[54]神か、悪魔か・・・'),
        0x58: ('スーパー系', '第４６話', '[55]龍と虎'),
        0x59: ('リアル系', '第４６話', '[56]第三の力'),
        0x5A: ('共通', '第４７話', '[57]男の戦い'),
        0x5B: ('共通', '第５０話', '[58]ヴァリアブル・フォーメーション'),
        0x5C: ('グラン・ガラン隊', '第５１話', '[59]ガラスの王国'),
        0x5D: ('ラー・カイラム隊', '第５１話', '[5A]ダカールの日'),
        0x5E: ('グラン・ガラン隊', '第５２話', '[5B]王国崩壊'),
        0x5F: ('ラー・カイラム隊', '第５２話', '[5C]バイブレーション'),
        0x60: ('ゴラオン隊', '第５４話', '[5D]思い出を未来へ'),
        0x61: ('ラー・カイラム隊', '第５３話', '[5E]ソロモン攻略戦'),
        0x62: ('ラー・カイラム隊', '第５４話', '[5F]女たちの戦場'),
        0x63: ('ラー・カイラム隊', '第５５話', '[60]駆け抜ける嵐'),
        0x64: ('ゴラオン隊', '第５１話', '[61]あしゅら男爵、散る'),
        0x65: ('ゴラオン隊', '第５２話', '[62]魔神皇帝'),
        0x66: ('グラン・ガラン隊', '第５３話', '[63]クロス・ファイト'),
        0x67: ('グラン・ガラン隊', '第５４話', '[64]異邦人たちの帰還'),
        0x68: ('ゴラオン隊', '第５３話', '[65]地球を賭けた一騎討ち'),
        0x69: ('共通', '第５６話', '[66]ジオンの幻像'),
        0x6A: ('ゴラオン隊', '第５５話', '[67]父の胸の中で泣け！'),
        0x6B: ('グラン・ガラン隊', '第５５話', '[68]女王リリーナ'),
        0x6C: ('共通', '第５７話０', '[69]天使の輪の上で'),
        0x6D: ('共通', '第５７話', '[69]天使の輪の上で'),
        0x6E: ('アクシズ', '第５８話', '[6A]神の国への誘惑'),
        0x6F: ('アクシズ', '第５９話', '[6B]クロス・ターゲット'),
        0x70: ('アクシズ', '第６０話', '[6C]戦士、再び・・・'),
        0x71: ('エンジェル・ハイロゥ', '第５８話', '[6D]勝者と敗者に祝福を'),
        0x72: ('エンジェル・ハイロゥ', '第５９話', '[6E]せめて、人間らしく'),
        0x73: ('エンジェル・ハイロゥ', '第６０話', '[6F]最後のシ者'),
        0x74: ('共通', '第６１話', '[70]運命の矢'),
        0x75: ('共通', '第６２話１', '[71]愛・おぼえていますか'),
        0x76: ('共通', '第６２話２', '[71]愛・おぼえていますか'),
        0x77: ('共通', '第６４話１', '[72]Ａｉｒ'),
        0x78: ('共通', '第６４話２', '[72]Ａｉｒ'),
        0x79: ('共通', '第６５話', '[73]ギア・オブ・デスティニー'),
        0x7A: ('熟練度４５以上', '第６６話', '[74]絶望の宴は今から始まる'),
        0x7B: ('熟練度４５以上', '第６７話１', '[75]この星の明日のために'),
        0x7C: ('熟練度４５以上', '第６７話２', '[75]この星の明日のために'),
        0x7D: ('熟練度４５以上', '第６７話３', '[75]この星の明日のために'),
        0x7E: ('ダミー', 'ダミー', 'ダミー'),
        0x7F: ('熟練度４５未満', '第６６話', '[77]人類に逃げ場なし'),
        0x80: ('熟練度４５未満', '第６７話１', '[78]鋼の魂'),
        0x81: ('熟練度４５未満', '第６７話２', '[78]鋼の魂'),
        0x82: ('ダミー', 'ダミー', 'ダミー'),
        0x83: ('ダミー', 'ダミー', 'ダミー'),
        0x84: ('ダミー', 'ダミー', 'ダミー'),
        0x85: ('ダミー', 'ダミー', 'ダミー'),
        0x86: ('共通', '第２８話', '[7C]ＥＯＴの島'),
        0x87: ('スーパー系', '第２９話', '[7D]心に念じる見えない刃'),
        0x88: ('リアル系', '第２９話', '[7E]黒い超闘士'),
        0x89: ('共通', '第４８話', '[7F]誰がために鐘は鳴る'),
        0x8A: ('共通', '第４９話', '[80]進路に光明、退路に絶望'),
        0x8B: ('力ずくで撃退', '第３０話', '[81]精霊憑依'),
    }
    STAGE = {
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
        0x22: 'ＥＶＡ弐号機 第２１話 聖戦士たち',
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
        0x49: 'リーンホースＪｒ．隊 第４２話 アクシズからの使者',
        0x4A: 'リーンホースＪｒ．隊 第４３話 プルとアクシズと',
        0x4B: 'リーンホースＪｒ．隊 第４４話 リィナの血',
        0x4C: 'リーンホースＪｒ．隊 第４５話 漆黒の天使来たりて',
        0x4D: 'グラン・ガラン隊 第４２話 ジュピター・ゴースト',
        0x4E: 'グラン・ガラン隊 第４３話 宇宙に咲く妖花',
        0x4F: 'グラン・ガラン隊 第４４話 ゼロと呼ばれたガンダム',
        0x50: 'グラン・ガラン隊 第４５話 強襲、阻止限界点',
        0x51: 'ゴラオン隊 第４２話 父よ地球は近い',
        0x52: 'ゴラオン隊 第４３話 静止した闇の中で',
        0x53: 'ゴラオン隊 第４４話 赤い髪の女',
        0x54: 'ゴラオン隊 第４５話 神か、悪魔か・・・',
        0x55: 'スーパー系 第４６話 龍と虎',
        0x56: 'リアル系 第４６話 第三の力',
        0x57: '共通 第４７話 男の戦い',
        0x58: '共通 第５０話 ヴァリアブル・フォーメーション',
        0x59: 'グラン・ガラン隊 第５１話 ガラスの王国',
        0x5A: 'ラー・カイラム隊 第５１話 ダカールの日',
        0x5B: 'グラン・ガラン隊 第５２話 王国崩壊',
        0x5C: 'ラー・カイラム隊 第５２話 バイブレーション',
        0x5D: 'ゴラオン隊 第５４話 思い出を未来へ',
        0x5E: 'ラー・カイラム隊 第５３話 ソロモン攻略戦',
        0x5F: 'ラー・カイラム隊 第５４話 女たちの戦場',
        0x60: 'ラー・カイラム隊 第５５話 駆け抜ける嵐',
        0x61: 'ゴラオン隊 第５１話 あしゅら男爵、散る',
        0x62: 'ゴラオン隊 第５２話 魔神皇帝',
        0x63: 'グラン・ガラン隊 第５３話 クロス・ファイト',
        0x64: 'グラン・ガラン隊 第５４話 異邦人たちの帰還',
        0x65: 'ゴラオン隊 第５３話 地球を賭けた一騎討ち',
        0x66: '共通 第５６話 ジオンの幻像',
        0x67: 'ゴラオン隊 第５５話 父の胸の中で泣け！',
        0x68: 'グラン・ガラン隊 第５５話 女王リリーナ',
        0x69: '共通 第５７話 天使の輪の上で',
        0x6A: 'アクシズ 第５８話 神の国への誘惑',
        0x6B: 'アクシズ 第５９話 クロス・ターゲット',
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
        0x7C: '共通 第２８話 ＥＯＴの島',
        0x7D: 'スーパー系 第２９話 心に念じる見えない刃',
        0x7E: 'リアル系 第２９話 黒い超闘士',
        0x7F: '共通 第４８話 誰がために鐘は鳴る',
        0x80: '共通 第４９話 進路に光明、退路に絶望',
        0x81: '力ずくで撃退 第３０話 精霊憑依',
    }
    SCRIPT = {
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
        0x44: ['[0x22]聖戦士たち 关前'],
        0x45: ['[0x22]聖戦士たち 幕间'],
        0x46: ['[0x22]聖戦士たち 关后'],
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
        0xDD: ['[0x6B]クロス・ターゲット 关前'],
        0xDE: ['[0x6B]クロス・ターゲット 关后'],
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
    PART = {
        0x00: 'ーー',
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
    MUSIC = {
        0x00: 'コン・バトラーVのテーマ',
        0x01: '熱風！疾風！サイバスター',
        0x02: 'ダークプリズン',
        0x03: 'フラッパー・ガール',
        0x04: 'バーニング・ラブ',
        0x05: 'カムヒア！ダイターン3',
        0x06: 'ダンバインとぶ',
        0x07: '彼方へ',
        0x08: 'Invisible',
        0x09: '0x09',
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
        0x42: '42',
        0x43: '遠い日の安息',
        0x44: '誰がために鐘は踊る',
        0x45: '苦難の先に待つものは',
        0x46: '開かれた砲門',
        0x47: '一つの結末',
        0x48: '災い来たりて',
        0x49: '悲しい記憶',
        0x4A: '修羅の予感',
        0x4B: 'トップをねらえ！ ～Fly High～',
        0x4C: '作戦開始',
        0x4D: '危機',
        0x4E: 'ボルテスⅤの歌',
        0x4F: 'レッツ・コンバイン！',
        0x50: 'ダイターン3の名のもとに',
        0x51: '0x51',
        0x52: '0x52',
        0x53: '0x53',
        0x54: '愛・おぼえていますか',
        0x55: 'マクロス',
        0x56: '愛・おぼえていますか',
        0x57: '愛・おぼえていますか',
        0x58: 'Zのテーマ',
        0x59: '空飛ぶマジンガーZ',
        0x5A: '0x5A',
        0x5B: 'オレは洸だ',
        0x5C: 'ガンバスター',
    }
    SPIRIT = {
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
        0xFF: 'ーー',
    }
    ROBOT = dict()
    ROBOT['移動タイプ'] = ['空', '陸', '海', '地']
    ROBOT['サイズ'] = {0x0: 'ＳＳ', 0x1: 'Ｓ', 0x2: 'Ｍ', 0x3: 'Ｌ', 0x4: 'ＬＬ'}
    ROBOT['乗り換え系'] = [
        'ガンダム系（ＵＣ）',
        'ガンダム系（Ｗ）',
        'マジンガー系',
        'ダンバイン系',
        'ダンバイン系（妖精）',
        'マクロス系',
        'オリジナル系（リアル）',
        'ライディーン系',
        'ゼロシステム',
        'ダイターン系',
    ]
    ROBOT['特殊能力'] = [
        'Ａ.Ｔ.フィールド',
        'オーラバリア',
        'グラビティ・テリトリー',
        'ピンポイントバリア',
        'グラビティ・ウォール',
        '念動フィールド',
        'イナーシャルキャンセラー',
        'Ｉフィールド（ν）',
        'Ｉフィールド',
        'ビームコート',
        '盾装備',
        '剣装備',
        '補給装置',
        '修理装置',
        '分身',
        'ＨＰ回復（小）',
        'ＨＰ回復（大）',
        'ＥＮ回復（小）',
        'ＥＮ回復（大）',
        'マジンパワー',
        '暴走',
        '精霊憑依',
        'ゼロシステム',
        'Ｓ２機関',
        '変形',
        '合体',
        '分離',
        'アンビリカルケーブル',
        'ＶＴＯＬ属性',
        '量産',
        '搭載・発進',
    ]
    ROBOT['空適応'] = {0x0: 'ー', 0x1: 'Ｄ', 0x2: 'Ｃ', 0x3: 'Ｂ', 0x4: 'Ａ'}
    ROBOT['陸適応'] = ROBOT['海適応'] = ROBOT['宇適応'] = ROBOT['空適応']
    ROBOT['換装グループ'] = {0x0: 'V2ガンダム', 0x1: 'ヒュッケバインMK-Ⅲ', 0xFF: 'ーー'}

    WEAPON = dict()
    WEAPON['分類'] = {0x0: '格闘', 0x1: '射撃'}
    WEAPON['ＭＡＰタイプ'] = {0x0: 'ーー', 0x1: '方向指定型', 0x2: '自機中心型', 0x3: '着弾点指定型'}
    WEAPON['属性'] = ['Ｐ', 'Ｂ', '切り払', 'ボトム射出', 'ビット類', '突貫', '敵味方識別']
    WEAPON['空適応'] = {0x0: 'ー', 0x1: 'Ｃ', 0x2: 'Ｂ', 0x3: 'Ａ'}
    WEAPON['陸適応'] = WEAPON['海適応'] = WEAPON['宇適応'] = WEAPON['空適応']

    PILOT = dict()
    PILOT['乗り換え系'] = [
        'ガンダム系（ＵＣ）',
        'ガンダム系（Ｗ）',
        'マジンガー系',
        'ダンバイン系',
        'ダンバイン系（妖精）',
        'マクロス系',
        'オリジナル系（リアル）',
        'ライディーン系',
        'ゼロシステム',
        'ダイターン系',
    ]
    PILOT['先天技能'] = ['底力', '天才', 'ガッツ', '野生化', '集中力', 'ＳＰ回復', '社長', '勇者']
    PILOT['分類'] = ['主役', 'サイボーグ', 'シンクロ', '妖精']
    PILOT['性格'] = {0x0: '弱気', 0x1: '普通', 0x2: '強気', 0x3: '超強気'}
    PILOT['空適応'] = PILOT['陸適応'] = PILOT['海適応'] = PILOT['宇適応'] = ROBOT['空適応']
    PILOT['特殊技能'] = {
        0x0: 'ニュータイプ',
        0x1: '強化人間',
        0x2: '聖戦士',
        0x3: '念動力',
        0x4: 'シールド防御',
        0x5: '切り払い',
        0xFF: 'ーー'
    }
