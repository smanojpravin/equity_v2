from django import template


register = template.Library()


# @register.filter
# def shrink_num(num):
#     """
#     Shrinks number rounding
#     123456  > 123,5K
#     123579  > 123,6K
#     1234567 > 1,2M
#     """

#     # num = int(num)
#     # magnitude = 0
#     # while abs(num) >= 1000:
#     #     magnitude += 1
#     #     num /= 1000.0
#     # # add more suffixes if you need them
#     # num = '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

#     # return num
#     # value = str(value)

#     if value.isdigit():
#         value_int = int(value)

#         if value_int >= 1000000:
#             value = "%.0f%s" % (value_int/1000000.00, 'M')
#         else:
#             if value_int >= 1000:
#                 value = "%.0f%s" % (value_int/1000.0, 'k')

#         return value

@register.filter
def shrink_num(value):
    """
    Shrinks number rounding
    123456  > 123,5K
    123579  > 123,6K
    1234567 > 1,2M
    """
    # value = str(value)

    # num = int(value)
    # magnitude = 0
    # while abs(num) >= 1000:
    #     magnitude += 1
    #     num /= 1000.0
    # # add more suffixes if you need them
    # num = '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])


    if value.isdigit():
        value_int = int(value)

        # if value_int >= 1000000:
        #     value = "%.0f%s" % (value_int/1000000.00, 'M')
        #else:
        if value_int >= 1000 :
            value = "%.0f %s" % (value_int/1000.0, 'k')
        if value_int <= -1000 :
            value = "%.0f %s" % (value_int/-1000.0, 'k')
    return value