from Huracan_GUI import*
import pytest
def test_create_account_number():
    acc_num_exampales = [0,100,231,50395,231]

    acc_num = create_account_number(acc_num_exampales)
    for _ in range(100):
        assert int(acc_num) > 0 and int(acc_num) < 10000

def test_get_date():
    date_example = "2022/12/6"
    date_test = get_date()

    assert len(date_test) == len(date_example)

def test_delete_item():

    dict_test = {
        1:"a", 
        2:"b",
        3:"c",
        4:"d",
        5:"e",
        6:"f"
    }
    len_o =len(dict_test)
    key_value = random.randint(1,6)
    delete_item(key_value, dict_test)

    assert len(dict_test) < len_o



pytest.main(["-v", "--tb=line", "-rN", __file__])