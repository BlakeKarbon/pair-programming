

def applyCoupon(subtotal, couponType, value, minimumSpend):
    return subtotal




subtotal = 5.50
couponType = "PERCENT"
value = 0.5
minimumSpend = 10.00
if isinstance(applyCoupon(subtotal, couponType, value, minimumSpend),float):
    print("Float return test passed.")
else:
    print("Float return test failed.")
