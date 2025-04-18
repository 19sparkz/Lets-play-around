# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = centre align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
#: = insert a space before positive numbers
# :, = comma seperator


price1 = 3000.3445
price2 = -987.345
price3 = 1200.23

print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")
