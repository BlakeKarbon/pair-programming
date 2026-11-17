

def applyCoupon(subtotal, couponType, value, minimumSpend):
    return subtotal




subtotal = 5.50
couponType = "PERCENT"
value = 0.5
minimumSpend = 5.00
if isinstance(applyCoupon(subtotal, couponType, value, minimumSpend),float):
    print("Float return test passed.")
else:
    print("Float return test failed.")



if applyCoupon(subtotal, couponType, value, minimumSpend) == 2.75:
    print("Coupon applied")
else:
    print("Coupon failed")


