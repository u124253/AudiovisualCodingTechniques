def yuv_to_rgb(yuv):
    """
    Coverts YUV coordinates to RGB
    input: y,u,v coordinates
    output: r,g,b coordinates
    """
    y, u, v = yuv

    r = y + 1.402 * (v - 128)
    g = y - 0.3441 * (u - 128) - 0.7141 * (v - 128)
    b = y + 1.772 * (u - 128)

    r = round(max(0, min(255, r)))
    g = round(max(0, min(255, g)))
    b = round(max(0, min(255, b)))

    rgb = (r, g, b)

    return rgb


def rgb_to_yuv(rgb):
    """
    Coverts RGB coordinates to YUV
    input: r,g,b coordinate
    output: y,u,v coordinates
    """
    r, g, b = rgb
    y = round(r * .299000 + g * .587000 + b * .114000)
    u = round(r * -.168736 + g * -.331264 + b * .500000 + 128)
    v = round(r * .500000 + g * -.418688 + b * -.081312 + 128)
    yuv1 = (y, u, v)
    return yuv1


print(rgb_to_yuv((0, 0, 0)))


print(yuv_to_rgb((0, 128, 128)))


