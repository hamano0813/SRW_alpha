#include "parser.h"

typedef struct
{
    unsigned char code : 4;
    unsigned char nt : 2;
    unsigned char ap : 2;
    unsigned char morale;
    unsigned char utype : 2;
    unsigned char srange : 2;
    unsigned char lrange : 4;
    unsigned char mtype : 2;
    unsigned char mrange : 3;
    unsigned char : 3;
    unsigned short dmg;
    unsigned char type : 1;
    unsigned char para : 7;
    unsigned char : 4;
    unsigned char add : 4;
    char name[0x15];
    unsigned char trange;
    unsigned char tmovie;
    unsigned char en;
    char acc;
    char ct;
    unsigned char sbullet;
    unsigned char mbullet;
    unsigned char air;
    unsigned char gnd;
    unsigned char sea;
    unsigned char cos;
} WEAPON;

typedef struct
{
    char name[0x1A];
    unsigned short code;
    unsigned char type : 4;
    unsigned char : 4;
    unsigned char move;
    unsigned short hp;
    unsigned short en;
    unsigned short mobi;
    unsigned short armor;
    unsigned short limit;
    unsigned char size;
    unsigned char part;
    unsigned short drive : 10;
    unsigned short : 6;
    unsigned int skill : 31;
    unsigned int : 1;
    unsigned short repair;
    unsigned short money;
    unsigned char trans_g;
    unsigned char trans_i;
    unsigned char comb_g;
    unsigned char comb_i;
    unsigned short core;
    unsigned char comb_c;
    unsigned char shift;
    unsigned char bgm;
    unsigned char : 8;
    unsigned char : 8;
    unsigned char : 8;
    unsigned char air;
    unsigned char gnd;
    unsigned char sea;
    unsigned char cos;
    WEAPON weapon[0x10];
} ROBOT;

const char parse_doc[] = "parse(buffer: bytearray, extra: dict, trans: dict) -> dict";

static PyObject *ROBOT_parse(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *BufBytearray;
    PyObject *ExtraDict;
    PyObject *TransDict;
    char *kw_list[] = {"buffer", "extra", "trans", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "YOO", kw_list, &BufBytearray, &ExtraDict, &TransDict))
        return NULL;
    unsigned char *data_byte;
    data_byte = PyByteArray_AsString(BufBytearray);
    if (!data_byte)
        return NULL;

    unsigned short robot_count = 0x1E6;
    unsigned char weapon_count = 0x10;

    ROBOT *robot_ptr;
    robot_ptr = (ROBOT *)data_byte;

    PyObject *RobotList = PyList_New(0);

    for (unsigned short robot_idx = 0; robot_idx < robot_count; robot_idx++)
    {
        size_t robot_len = strlen((robot_ptr + robot_idx)->name);
        PyObject *RobotStr = PyUnicode_Decode((robot_ptr + robot_idx)->name, robot_len, codec, "replace");
        RobotStr = replace(RobotStr, ExtraDict);
        RobotStr = replace(RobotStr, TransDict);

        PyObject *RobotDict = PyDict_New();
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "机体"), RobotStr);
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "代码"), Py_BuildValue("i", (robot_ptr + robot_idx)->code));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "移动类型"), Py_BuildValue("i", (robot_ptr + robot_idx)->type));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "移动力"), Py_BuildValue("i", (robot_ptr + robot_idx)->move));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "ＨＰ"), Py_BuildValue("i", (robot_ptr + robot_idx)->hp));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "ＥＮ"), Py_BuildValue("i", (robot_ptr + robot_idx)->en));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "运动性"), Py_BuildValue("i", (robot_ptr + robot_idx)->mobi));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "装甲"), Py_BuildValue("i", (robot_ptr + robot_idx)->armor));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "限界"), Py_BuildValue("i", (robot_ptr + robot_idx)->limit));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "体积"), Py_BuildValue("i", (robot_ptr + robot_idx)->size));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "芯片"), Py_BuildValue("i", (robot_ptr + robot_idx)->part));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "换乘系"), Py_BuildValue("i", (robot_ptr + robot_idx)->drive));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "特性"), Py_BuildValue("i", (robot_ptr + robot_idx)->skill));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "修理费"), Py_BuildValue("i", (robot_ptr + robot_idx)->repair));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "资金"), Py_BuildValue("i", (robot_ptr + robot_idx)->money));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "变形组号"), Py_BuildValue("i", (robot_ptr + robot_idx)->trans_g));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "变形序号"), Py_BuildValue("i", (robot_ptr + robot_idx)->trans_i));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "合体组号"), Py_BuildValue("i", (robot_ptr + robot_idx)->comb_g));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "合体序号"), Py_BuildValue("i", (robot_ptr + robot_idx)->comb_i));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "分离机体"), Py_BuildValue("i", (robot_ptr + robot_idx)->core));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "合体数"), Py_BuildValue("i", (robot_ptr + robot_idx)->comb_c));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "换装系统"), Py_BuildValue("i", (robot_ptr + robot_idx)->shift));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "机体BGM"), Py_BuildValue("i", (robot_ptr + robot_idx)->bgm));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "空适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->air));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "陆适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->gnd));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "海适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->sea));
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "宇适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->cos));

        PyObject *WeaponList = PyList_New(0);
        for (unsigned short weapon_idx = 0; weapon_idx < weapon_count; weapon_idx++)
        {
            size_t weapon_len = strlen((robot_ptr + robot_idx)->weapon[weapon_idx].name);
            PyObject *WeaponStr = PyUnicode_Decode((robot_ptr + robot_idx)->weapon[weapon_idx].name, weapon_len, codec, "replace");
            WeaponStr = replace(WeaponStr, ExtraDict);
            WeaponStr = replace(WeaponStr, TransDict);

            PyObject *WeaponDict = PyDict_New();
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "代码"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].code));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "新人类"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].nt));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "圣战士"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].ap));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "气力"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].morale));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "改造类型"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].utype));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "近射程"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].srange));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "远射程"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].lrange));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "地图武器分类"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].mtype));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "着弹点指定型攻击半径"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].mrange));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "攻击力"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].dmg));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "分类"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].type));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "属性"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].para));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "改造追加"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].add));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "武器"), WeaponStr);
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "方向指定型范围"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].trange));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "地图武器演出"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].tmovie));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "ＥＮ"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].en));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "命中"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].acc));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "ＣＴ"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].ct));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "初期弹数"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].sbullet));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "最大弹数"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].mbullet));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "空适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].air));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "陆适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].gnd));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "海适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].sea));
            PyDict_SetItem(WeaponDict, Py_BuildValue("s", "宇适应"), Py_BuildValue("i", (robot_ptr + robot_idx)->weapon[weapon_idx].cos));

            PyList_Append(WeaponList, WeaponDict);
        }
        PyDict_SetItem(RobotDict, Py_BuildValue("s", "武器列表"), WeaponList);
        PyList_Append(RobotList, RobotDict);
    }

    PyObject *DataDict = PyDict_New();
    PyDict_SetItem(DataDict, Py_BuildValue("s", "机体列表"), RobotList);

    return DataDict;
}

static PyMethodDef ROBOTMethods[] =
    {
        {"parse", (PyCFunction)ROBOT_parse, METH_VARARGS | METH_KEYWORDS, parse_doc},
        {NULL, NULL, 0, NULL}};

static struct PyModuleDef ROBOT_module =
    {
        PyModuleDef_HEAD_INIT,
        "ROBOT",
        "ROBOT.raf Parser",
        -1,
        ROBOTMethods};

PyMODINIT_FUNC PyInit_ROBOT(void)
{
    PyObject *module;
    module = PyModule_Create(&ROBOT_module);
    if (module == NULL)
        return NULL;
    return module;
}
