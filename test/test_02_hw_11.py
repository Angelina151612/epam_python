from hw.hw_11_task_02 import ElderDiscount, MorningDiscount, Order


def test_order():
    order_1 = Order(100, MorningDiscount)
    assert order_1.final_price() == 75

    order_2 = Order(100, ElderDiscount)
    assert order_2.final_price() == 85
