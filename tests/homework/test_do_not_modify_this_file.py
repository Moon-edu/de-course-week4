from tests.homework.csv import *
from tests.homework.excel import *
from tests.homework.json import *
from tests.homework.xml import *

"""
이 파일은 채점을 위한 파일입니다. 수정하지 마세요.
"""
def test_q1_test_find_richest_and_asset():
    result = find_richest_and_asset()
    assert result == ("Donald", 1023014)

def test_q1_test_find_top3_richest_city():
    result = find_top3_richest_city()
    assert len(result) == 3
    assert ["Dublin", "Seoul", "New York"] in result


def test_q2_test_find_richest_and_asset():
    result = find_corp_total_asset()
    assert result == 10239102305

def test_q2_test_find_llc_total_asset():
    result = find_llc_total_asset()
    assert abs(result - 1025831.87653) < 0.00001


def test_q3_test_summarize():
    result = summarize()
    assert result == (100391284324, 198312.8732, 500)


def test_q4_test_find_poor_and_asset():
    result = find_poor_and_asset()
    assert result == ("Donald", -102314)

def test_q4_test_find_top5_poorest_city():
    result = find_top3_poorest_city()
    assert len(result) == 3
    assert ["Dublin", "Seoul", "New York"] in result