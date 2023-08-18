import math
from enum import IntEnum
from typing import NamedTuple


class Vec2(NamedTuple):
    x: float
    y: float

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float):
        return self * scalar

    def close_to(self, other: object, precision: float) -> bool:
        return (
            self.x < other.x + precision
            and self.x > other.x - precision
            and self.y < other.y + precision
            and self.y > other.y - precision
        )

    def rotated(self, rad_angle: float, center=None):
        s = math.sin(rad_angle)
        c = math.cos(rad_angle)
        # Move point to center
        center = center or Vec2(0, 0)
        translated = self - center
        # Rotate point using 2d matrix
        xnew = translated.x * c - translated.y * s
        ynew = translated.x * s + translated.y * c
        # Translate point back
        return Vec2(xnew, ynew) + center

    @property
    def invert_y(self):
        return Vec2(self.x, -self.y)

    @property
    def norm(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def normalized(self):
        norm = self.norm
        return self if norm == 0 else Vec2(self.x / norm, self.y / norm)

    @property
    def angle(self) -> float:
        return math.atan2(self.y, self.x)

    def __repr__(self) -> str:
        return f"Vec2({self.x:0.3f}, {self.y:0.3f})"


def cross(p1: Vec2, p2: Vec2, point: Vec2) -> float:
    return (p2.x - p1.x) * (point.y - p1.y) - (p2.y - p1.y) * (point.x - p1.x)


def is_left(p1: Vec2, p2: Vec2, point: Vec2) -> bool:
    return cross(p1, p2, point) > 0


class Polar(NamedTuple):
    r: float
    theta: float

    def to_vec2(self) -> Vec2:
        return Vec2(
            math.cos(self.theta) * self.r,
            math.sin(self.theta) * self.r,
        )

    def __repr__(self) -> str:
        return f"Polar({self.r:.3f}, {self.theta:.3f})"


def dist(a: Vec2, b: Vec2) -> float:
    dx = b.x - a.x
    dy = b.y - a.y
    return math.sqrt(dx * dx + dy * dy)


def is_close(a: Vec2, b: Vec2, precision: float) -> bool:
    return dist(a, b) <= precision


def find_closest_point(origin: Vec2, points: list[Vec2]) -> Vec2:
    closest_point = None
    closest_dist = 999
    for point in points:
        dist_to_point = dist(origin, point)
        if dist_to_point < closest_dist:
            closest_dist = dist_to_point
            closest_point = point
    return closest_point


# Compare two angles and return the angle between the two. Accounts for -PI/+PI
def angle_between(alpha: float, beta: float) -> float:
    if abs(beta - alpha) < math.pi:
        return beta - alpha
    return beta - alpha - math.pi * 2 if (beta > alpha) else beta - alpha + math.pi * 2


def angle_mod(angle: float) -> float:
    """Bring radian angle into range -pi..pi"""
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


class Box2(NamedTuple):
    pos: Vec2
    w: float
    h: float

    def __repr__(self) -> str:
        return f"Box[{self.pos}, w: {self.w}, h: {self.h}]"

    def contains(self, pos: Vec2):
        left, top = self.pos.x, self.pos.y
        right, bottom = self.pos.x + self.w, self.pos.y + self.h
        return pos.x >= left and pos.x <= right and pos.y >= top and pos.y <= bottom

    # Top-left, Top-right, Bot-left, Bot-right
    def tl(self) -> Vec2:
        return self.pos

    def tr(self) -> Vec2:
        return Vec2(self.pos.x + self.w, self.pos.y)

    def bl(self) -> Vec2:
        return Vec2(self.pos.x, self.pos.y + self.h)

    def br(self) -> Vec2:
        return Vec2(self.pos.x + self.w, self.pos.y + self.h)


def get_box_with_size(center: Vec2, half_size: float) -> Box2:
    return Box2(
        pos=Vec2(center.x - half_size, center.y - half_size),
        w=2 * half_size,
        h=2 * half_size,
    )


# expand the box by a set amount in all directions
def grow_box(box: Box2, amount: int = 1) -> Box2:
    return Box2(
        pos=Vec2(box.pos.x - amount, box.pos.y - amount),
        w=box.w + 2 * amount,
        h=box.h + 2 * amount,
    )


class Facing(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


def is_facing_opposite(a: Facing, b: Facing) -> bool:
    match a:
        case Facing.LEFT:
            return b == Facing.RIGHT
        case Facing.RIGHT:
            return b == Facing.LEFT
        case Facing.UP:
            return b == Facing.DOWN
        case Facing.DOWN:
            return b == Facing.UP


def get_2d_facing_from_dir(direction: Vec2) -> Facing:
    if abs(direction.x) > abs(direction.y):
        return Facing.LEFT if direction.x < 0 else Facing.RIGHT
    # dir.y is larger:
    return Facing.UP if direction.y < 0 else Facing.DOWN


def facing_str(facing: Facing) -> str:
    match facing:
        case Facing.LEFT:
            return "left"
        case Facing.RIGHT:
            return "right"
        case Facing.UP:
            return "up"
        case Facing.DOWN:
            return "down"


def facing_ch(facing: Facing) -> str:
    match facing:
        case Facing.LEFT:
            return "<"
        case Facing.RIGHT:
            return ">"
        case Facing.UP:
            return "^"
        case Facing.DOWN:
            return "v"


# https://gist.github.com/tatsy/e14dd18079bca60ac8f78217b77332c1
class Vec3:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.x * v2.x - v1.x * v2.z
        z = v1.z * v2.y - v1.y * v2.x
        return Vec3(x, y, z)

    @staticmethod
    def normalize(v):
        return v / v.norm()

    @staticmethod
    def dist(v1, v2) -> float:
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        dz = v2.z - v1.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    @staticmethod
    def is_close(v1, v2, precision: float) -> bool:
        return Vec3.dist(v1, v2) <= precision

    def norm(self):
        return math.sqrt(Vec3.dot(self, self))

    def __add__(self, v):
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self, v):
        return self + (-v)

    def __mul__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        return Vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self, v):
        return self.__mul__(v)

    def __div__(self, v):
        if isinstance(v, Vec3):
            return Vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        return Vec3(self.x / v, self.y / v, self.z / v)

    def __repr__(self) -> str:
        return f"[ {self.x:.4f}, {self.y:.4f}, {self.z:.4f} ]"
