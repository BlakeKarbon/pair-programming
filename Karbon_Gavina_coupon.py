

def applyCoupon(subtotal, couponType, value, minimumSpend):
    if (minimumSpend > subtotal):
        return subtotal
    else:
        if couponType == "DOLLAR":
            return subtotal - value
        elif couponType == "PERCENT":
            return subtotal * value



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

minimumSpend = 10.00
if applyCoupon(subtotal, couponType, value, minimumSpend) != 5.50:
    print("Minimum Spend Check Failed")
else:
    print("Minimum Spend Check Passed")


couponType = "DOLLAR"
minimumSpend = 5.00
if applyCoupon(subtotal, couponType, value, minimumSpend) == 5.00:
    print("Dollar check pass")
else:
    print("Dollar check failed")




