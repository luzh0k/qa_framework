import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection(database_fix):
    database_fix.test_connection()

@pytest.mark.database
def test_check_all_users(database_fix):
    users = database_fix.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii(database_fix):
    user = database_fix.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update(database_fix):
    database_fix.update_product_qnt_by_id(1, 25)
    water_qnt = database_fix.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(database_fix):
    database_fix.insert_product(4, "печиво", "солодке", 30)
    coockie_qnt = database_fix.select_product_qnt_by_id(4)

    assert coockie_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete(database_fix):
    database_fix.insert_product(99, "test", "data", 999)
    database_fix.delete_product_by_id(99)
    qnt = database_fix.select_product_qnt_by_id(99)

    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_order(database_fix):
    orders = database_fix.get_detailed_orders()
    print("Замовлення", orders)
    #Check that quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders [0][3] == 'з цукром'
    assert orders [0][4] == '12:22:23'
