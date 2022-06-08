def perimeter(rect):
    """Returns the perimeter of a rectangle."""
    return (rect[0] * 2) + (rect[1] * 2)


answer = perimeter([10, 20])
print(answer)

# The equivalent lambda function.

perimeter_1 = lambda rect: (rect[0] * 2) + (rect[1] * 2)

result = perimeter_1([10, 30])
print(result)
