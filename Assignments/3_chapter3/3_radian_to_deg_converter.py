
# Write a script that converts an angle
# in radians to angle in degrees, minutes and seconds
import math

# Do not permit angles in degrees greater than 360.
def convert_to_deg(angle_deg: float) -> tuple:
    total_angle = ((angle_deg * 180) / math.pi)
    angle_deg = int(total_angle)
    total_angle_min = (total_angle - angle_deg) * 60
    angle_min = int(total_angle_min)
    angle_sec = round(((total_angle_min - angle_min) * 60), 2)
    return angle_deg, angle_min, angle_sec

if __name__ == "__main__":
    print(convert_to_deg(math.pi))
    print(convert_to_deg(2 * math.pi))
    print(convert_to_deg(4 * math.pi))