import pytest
from modules.common.database import Database
from  modules.common import generate_data



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

@pytest.mark.database
def test_scheme_create_select_delete_select(database_fix):
    new_id = database_fix.generate_new_id('products')
    isproduct = database_fix.get_product_by_id(new_id)
    
    assert isproduct == []

    name = generate_data.generate_string(5, 1)
    description = generate_data.generate_string(6, 2)
    qnt = generate_data.generate_number(55)
    database_fix.insert_product(new_id, name, description, qnt)
    new_product = database_fix.get_product_by_id(new_id)

    assert new_product[0][0] == new_id
    assert new_product[0][1] == name
    assert new_product[0][2] == description
    assert new_product[0][3] == qnt

    database_fix.delete_product_by_id(new_id)
    isproduct2 = database_fix.get_product_by_id(new_id)
    assert isproduct2 == []

@pytest.mark.database
def test_get_all_products(database_fix):
    products = database_fix.get_all_products()
    print(products)
