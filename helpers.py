def relative(point, shape):
    h, w = shape[:2]
    return (int(point.x * w), int(point.y * h))

def relativeT(point, shape):
    h, w = shape[:2]
    return (point.x * w, point.y * h, point.z * w)
