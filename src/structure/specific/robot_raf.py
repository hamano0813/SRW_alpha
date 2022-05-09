#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parameter import HALF_TEXT_EXTRA
from structure.generic import Rom, Value, Text, Sequence

WEAPON_STRUCTURE = {
    'コード': Value(0x0, 0x1, (0, 4)),
    'ニュータイプ': Value(0x0, 0x1, (4, 6)),
    '聖戦士': Value(0x0, 0x1, (6, 8)),
    '気力': Value(0x1, 0x1),
    '改造タイプ': Value(0x2, 0x1, (0, 2)),
    '近射程': Value(0x2, 0x1, (2, 4)),
    '遠射程': Value(0x2, 0x1, (4, 8)),
    'マップ分類': Value(0x3, 0x1, (0, 2)),
    '着弾点指定型攻撃半径': Value(0x3, 0x1, (2, 5)),
    '攻撃力': Value(0x4, 0x2),
    '分類': Value(0x6, 0x1, 0),
    '属性': Value(0x6, 0x1, (1, 8)),
    '改造追加': Value(0x7, 0x1, (4, 8)),
    '武器': Text(0x8, 0x15, 'shiftjisx0213', HALF_TEXT_EXTRA),
    '方向指定型範囲': Value(0x1D, 0x1),
    'マップ演出': Value(0x1E, 0x1),
    'ＥＮ': Value(0x1F, 0x1),
    '命中': Value(0x20, -0x1),
    'ＣＴ': Value(0x21, -0x1),
    '初期弾数': Value(0x22, 0x1),
    '最大弾数': Value(0x23, 0x1),
    '空適応': Value(0x24, 0x1),
    '陸適応': Value(0x25, 0x1),
    '海適応': Value(0x26, 0x1),
    '宇適応': Value(0x27, 0x1),
}

ROBOT_STRUCTURE = {
    '機体': Text(0x0, 0x1A, 'shiftjisx0213', HALF_TEXT_EXTRA),
    'コード': Value(0x1A, 0x2),
    'タイプ': Value(0x1C, 0x1, (0, 4)),
    '移動力': Value(0x1D, 0x1),
    'ＨＰ': Value(0x1E, 0x2),
    'ＥＮ': Value(0x20, 0x2),
    '運動性': Value(0x22, 0x2),
    '装甲': Value(0x24, 0x2),
    '限界': Value(0x26, 0x2),
    'サイズ': Value(0x28, 0x1),
    'パーツ': Value(0x29, 0x1),
    '乗り換え系': Value(0x2A, 0x2, (0, 10)),
    '特性': Value(0x2C, 0x4, (0, 31)),
    '修理費': Value(0x30, 0x2),
    '資金': Value(0x32, 0x2),
    '变形チーム': Value(0x34, 0x1),
    '变形番号': Value(0x35, 0x1),
    '合体チーム': Value(0x36, 0x1),
    '合体番号': Value(0x37, 0x1),
    '分離機体': Value(0x38, 0x2),
    '合体数': Value(0x3A, 0x1),
    '換装システム': Value(0x3B, 0x1),
    '機体BGM': Value(0x3C, 0x1),
    '空適応': Value(0x40, 0x1),
    '陸適応': Value(0x41, 0x1),
    '海適応': Value(0x42, 0x1),
    '宇適応': Value(0x43, 0x1),
    '武器リスト': Sequence(WEAPON_STRUCTURE, 0x44, 0x28, 0x10),
}


class RobotRAF(Rom):
    def __init__(self):
        super(RobotRAF, self).__init__()
        self.structures = {
            '機体リスト': Sequence(ROBOT_STRUCTURE, 0x0, 0x2C4, 0x1E6),
        }

    def robots(self) -> dict[int, str]:
        if not self.data:
            return dict()
        return {idx: f"[{idx:03X}] {node['機体']}" for idx, node in enumerate(self.data['機体リスト'])}
