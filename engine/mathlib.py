"""Generic classes to help with math."""

import math
from typing import NamedTuple, Self


class Vec2:
    """Class representing a 2d point in space, or a 2d vector."""

    def __init__(self: Self, x: float, y: float) -> None:
        """Create a new Vec2 object."""
        self.x: float = x
        self.y: float = y

    def __eq__(self: Self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self: Self) -> int:
        return hash((self.x, self.y))

    def __add__(self: Self, other: Self) -> Self:
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self: Self, other: Self) -> Self:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self: Self, scalar: float) -> Self:
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self: Self, scalar: float) -> Self:
        return self * scalar

    def __truediv__(self: Self, v: Self | float) -> Self:
        if isinstance(v, Vec2):
            return Vec2(self.x / v.x, self.y / v.y)
        return Vec2(self.x / v, self.y / v)

    def close_to(self: Self, other: Self, precision: float) -> bool:
        """Return true if the two points are close to each other."""
        return (
            self.x < other.x + precision
            and self.x > other.x - precision
            and self.y < other.y + precision
            and self.y > other.y - precision
        )

    def rotated(self: Self, rad_angle: float, center: Self | None = None) -> Self:
        """Return the point rotated in 2d space."""
        s = math.sin(rad_angle)
        c = math.cos(rad_angle)
        # Move point to center
        center = center or Vec2(0, 0)
        translated = self - center
        # Rotate point using 2d matrix
        x_new = translated.x * c - translated.y * s
        y_new = translated.x * s + translated.y * c
        # Translate point back
        return Vec2(x_new, y_new) + center

    @property
    def invert_y(self: Self) -> Self:
        """Invert the y-axis and return new point."""
        return Vec2(self.x, -self.y)

    @property
    def norm(self: Self) -> float:
        """Calculate the length of the vector."""
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def normalized(self: Self) -> Self:
        """Calculate a vector with the same direction but with length 1."""
        norm = self.norm
        return self if norm == 0 else Vec2(self.x / norm, self.y / norm)

    @property
    def angle(self: Self) -> float:
        """Calculate the angle of the vector, from the x-axis."""
        return math.atan2(self.y, self.x)

    def __repr__(self: Self) -> str:
        return f"Vec2({self.x:.3f}, {self.y:.3f})"


def cross(p1: Vec2, p2: Vec2, point: Vec2) -> float:
    """Calculate 2d cross product."""
    return (p2.x - p1.x) * (point.y - p1.y) - (p2.y - p1.y) * (point.x - p1.x)


def is_left(p1: Vec2, p2: Vec2, point: Vec2) -> bool:
    """Calculate if the point is left of the line described by (p1, p2)."""
    return cross(p1, p2, point) > 0


class Polar:
    """Polar coordinate. A point in space, defined by an angle and a distance from origo."""

    def __init__(self: Self, r: float, theta: float) -> None:
        """Initialize a new Polar coordinate object."""
        self.r: float = r
        self.theta: float = theta

    def to_vec2(self: Self) -> Vec2:
        """Convert polar coordinate to Vec2 point."""
        return Vec2(
            math.cos(self.theta) * self.r,
            math.sin(self.theta) * self.r,
        )

    def __repr__(self: Self) -> str:
        return f"Polar({self.r:.3f}, {self.theta:.3f})"


def dist(a: Vec2, b: Vec2) -> float:
    """Calculate distance between two 2d points."""
    dx = b.x - a.x
    dy = b.y - a.y
    return math.sqrt(dx * dx + dy * dy)


def is_close(a: Vec2, b: Vec2, precision: float) -> bool:
    """Return true if two points are close to each other."""
    return dist(a, b) <= precision


def find_closest_point(origin: Vec2, points: list[Vec2]) -> Vec2:
    """Return the 2d point in a list that's closest to the origin point."""
    closest_point = None
    closest_dist = 999
    for point in points:
        dist_to_point = dist(origin, point)
        if dist_to_point < closest_dist:
            closest_dist = dist_to_point
            closest_point = point
    return closest_point


def angle_between(alpha: float, beta: float) -> float:
    """Compare two angles and return the angle between the two. Accounts for -PI/+PI."""
    if abs(beta - alpha) < math.pi:
        return beta - alpha
    return beta - alpha - math.pi * 2 if (beta > alpha) else beta - alpha + math.pi * 2


def angle_mod(angle: float) -> float:
    """Bring radian angle into range -pi..pi."""
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle


class Box2(NamedTuple):
    """
    Describes a 2d box aligned to the x-y coordinate system.

    The tl/tr/bl/br functions assume a y-axis that points down for top/bottom.
    """

    pos: Vec2
    w: float
    h: float

    def __repr__(self: Self) -> str:
        return f"Box[{self.pos}, w: {self.w}, h: {self.h}]"

    def contains(self: Self, pos: Vec2) -> bool:
        """Return true if 2d point is inside box boundary."""
        left, top = self.pos.x, self.pos.y
        right, bottom = self.pos.x + self.w, self.pos.y + self.h
        return pos.x >= left and pos.x <= right and pos.y >= top and pos.y <= bottom

    # Top-left, Top-right, Bot-left, Bot-right
    def tl(self: Self) -> Vec2:
        """Return top left corner of box."""
        return self.pos

    def tr(self: Self) -> Vec2:
        """Return top right corner of box."""
        return Vec2(self.pos.x + self.w, self.pos.y)

    def bl(self: Self) -> Vec2:
        """Return bottom left corner of box."""
        return Vec2(self.pos.x, self.pos.y + self.h)

    def br(self: Self) -> Vec2:
        """Return bottom right corner of box."""
        return Vec2(self.pos.x + self.w, self.pos.y + self.h)


def get_box_with_size(center: Vec2, half_size: float) -> Box2:
    """Create a square `Box2` centered around a 2d point."""
    return Box2(
        pos=Vec2(center.x - half_size, center.y - half_size),
        w=2 * half_size,
        h=2 * half_size,
    )


def grow_box(box: Box2, amount: int = 1) -> Box2:
    """Expand a `Box2` by a set amount in all directions."""
    return Box2(
        pos=Vec2(box.pos.x - amount, box.pos.y - amount),
        w=box.w + 2 * amount,
        h=box.h + 2 * amount,
    )


# https://gist.github.com/tatsy/e14dd18079bca60ac8f78217b77332c1
class Vec3:
    """Class representing a 3d point in space, or a 3d vector."""

    def __init__(self: Self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dot(v1: Self, v2: Self) -> float:
        """Calculate dot-product."""
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1: Self, v2: Self) -> Self:
        """Calculate cross-product. Returns the vector perpendicular to both v1 and v2."""
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.x * v2.x - v1.x * v2.z
        z = v1.z * v2.y - v1.y * v2.x
        return Vec3(x, y, z)

    @staticmethod
    def normalize(v: Self) -> Self:
        """Normalize vector v, returning a vector with the same direction and length 1."""
        return v / v.norm()

    @staticmethod
    def dist(v1: Self, v2: Self) -> float:
        """Calculate the distance between two points."""
        dx = v2.x - v1.x
        dy = v2.y - v1.y
        dz = v2.z - v1.z
        return math.sqrt(dx * dx + dy * dy + dz * dz)

    @staticmethod
    def is_close(v1: Self, v2: Self, precision: float) -> bool:
        """Return true if the points v1 and v2 are close to each other."""
        return Vec3.dist(v1, v2) <= precision

    def norm(self: Self) -> float:
        """Calculate length of vector."""
        return math.sqrt(Vec3.dot(self, self))

    def __eq__(self: Self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self: Self) -> int:
        return hash((self.x, self.y, self.z))

    def __add__(self: Self, v: Self) -> Self:
        return Vec3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self: Self) -> Self:
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self: Self, v: Self) -> Self:
        return self + (-v)

    def __mul__(self: Self, v: Self | float) -> Self:
        if isinstance(v, Vec3):
            return Vec3(self.x * v.x, self.y * v.y, self.z * v.z)
        return Vec3(self.x * v, self.y * v, self.z * v)

    def __rmul__(self: Self, v: Self) -> Self:
        return self.__mul__(v)

    def __truediv__(self: Self, v: Self | float) -> Self:
        if isinstance(v, Vec3):
            return Vec3(self.x / v.x, self.y / v.y, self.z / v.z)
        return Vec3(self.x / v, self.y / v, self.z / v)

    def __repr__(self: Self) -> str:
        return f"[ {self.x:.3f}, {self.y:.3f}, {self.z:.3f} ]"


class Quaternion:
    """Class that represents a (x,y,z,w) Quaternion."""

    def __init__(self: Self, x: float, y: float, z: float, w: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    # https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles
    # Section: Quaternion to Euler angles (in 3-2-1 sequence) conversion
    def to_angles(self: Self) -> Vec3:
        """Convert Quaternion to Euler angles."""
        return Vec3(
            math.atan2(
                2 * (self.w * self.x + self.y * self.z),
                1 - 2 * (self.x * self.x + self.y * self.y),
            ),
            math.asin(2 * (self.w * self.y - self.x * self.z)),
            math.atan2(
                2 * (self.w * self.z + self.x * self.y),
                1 - 2 * (self.y * self.y + self.z * self.z),
            ),
        )

    # Some math to correct the angle into a range of +-pi
    #   East = 0
    #   North = pi/2
    #   West = +-pi
    #   South = -pi/2
    def to_yaw(self: Self) -> float:
        """Get yaw rotation."""
        angles = self.to_angles()
        if angles.x > 0:
            return angles.y - math.pi / 2
        return math.pi - (angles.y + math.pi / 2)
