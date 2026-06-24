
import math

def convert_to_radians(deg: float, min: float, sec: float) -> float:
    return round(((deg + (min / 60) + (sec / 3600)) * math.pi / 180), 2)


if __name__ == "__main__":
    print(convert_to_radians(180.0, 0.0, 0.0))
    print(convert_to_radians(180.0, 52.0, 0.0))
    print(convert_to_radians(180.0, 52.0, 39.0))
