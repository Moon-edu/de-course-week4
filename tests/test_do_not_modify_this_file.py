from tests.homework.hw_csv import *
from tests.homework.excel import *
from tests.homework.json import *
from tests.homework.xml import *

"""
이 파일은 채점을 위한 파일입니다. 수정하지 마세요.
"""
def test_q1_test_find_richest_and_asset():
    result = find_richest_and_asset()
    assert result == ("Xantha", 9977373)


def test_q1_test_find_top3_richest_city():
    result = find_top3_richest_city()
    assert len(result) == 3
    assert sorted(['Delhi', 'Dortyol', 'Freiberg']) == sorted(result)


def test_q2_test_find_corp_total_asset():
    result = find_corp_total_asset()
    assert result == 153092707


def test_q2_test_find_llc_total_asset():
    result = find_llc_total_asset()
    assert abs(result - (175985567 / 34)) < 0.00001


def test_q3_test_summarize():
    result = summarize()
    assert result[0] == 2510970992
    assert abs(result[1] - 5021941.984) < 0.001
    assert result[2] == 500


def test_q4_test_find_poor_and_asset():
    result = find_poor_and_asset()
    assert result == ('Noah', 28401)


def test_q4_test_find_top3_poorest_city():
    result = find_top3_poorest_city()
    assert len(result) == 3
    assert sorted(["Pinneberg", "Gorzow Wielkopolski", "Guri"]) == sorted(result)
