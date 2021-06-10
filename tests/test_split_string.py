from utilites.make_data import split_string


def test_impact_list_format_1():
    _string = "DHKKT32-DHKKT12"
    _splited_str = split_string(_string)
    assert _splited_str == ["DHKKT32", "DHKKT12"]
    assert len(_splited_str) == 2

def test_impact_list_format_2():
    _string = "DKD , DHKHL32/DHKHLC1"
    _splited_str = split_string(_string)
    assert _splited_str == ["DHKHL32", "DHKHLC1"]
    assert len(_splited_str) == 2

def test_impact_list_format_3():
    _string = "DKD , DHKHL32/DHKHL8F, ,1,3,4,56,78,8,8,,,,,,,,,,"
    _splited_str = split_string(_string)
    assert _splited_str == ["DHKHL32", "DHKHL8F"]
    assert len(_splited_str) == 2

def test_impact_list_format_4():
    _string = "DKD , DHKHL32@;DHKHL21, ,1,3,4,56,78,8,8,"
    _splited_str = split_string(_string)
    assert _splited_str == ["DHKHL32", "DHKHL21"]
    assert len(_splited_str) == 2

def test_impact_list_format_5():
    _string = r"MBBRL06-MBBRL07; PBSDR38@ PBSDR39/ KUDLP05\ JHKLG17; KUMRP16; MASDR19. MASDR25. MHGNG05, PBSDR20, SOme , Garbage, Text"
    _splited_str = split_string(_string)
    assert _splited_str == ["MBBRL06", "MBBRL07", "PBSDR38", "PBSDR39", "KUDLP05", "JHKLG17", "KUMRP16", "MASDR19", "MASDR25", "MHGNG05", "PBSDR20"]
    assert len(_splited_str) == 11

def test_impact_list_format_6():
    _string = r"MBBRL06-MBBRL07; PBSDR38@ PBSDR39/ KUDLP05\ JHKLG17; KUMRP16; MASDR19. MASDR25. MHGNG05- PBSDR20-s00me- GarbAge- Text"
    _splited_str = split_string(_string)
    assert _splited_str == ["MBBRL06", "MBBRL07", "PBSDR38", "PBSDR39",
                                    "KUDLP05", "JHKLG17", "KUMRP16", "MASDR19", "MASDR25", "MHGNG05", "PBSDR20"]
    assert len(_splited_str) == 11

def test_impact_list_format_7():
    _string = r"EMPTY LIST SHOULD RETURN RETURNN"
    _splited_str = split_string(_string)
    assert _splited_str == []
    assert len(_splited_str) == 0
    assert isinstance(_splited_str, list)

def test_impact_list_format_8():
    _string = "DKD , DHKHL32@;D@KHL21, ,1,3,4,56,78,8,8, DH98K01"
    _splited_str = split_string(_string)
    assert _splited_str == ["DHKHL32"]
    assert len(_splited_str) == 1
    assert isinstance(_splited_str, list)
