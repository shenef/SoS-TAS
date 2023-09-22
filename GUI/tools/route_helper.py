import logging
from enum import Enum, auto
from typing import Self

from imgui_bundle import imgui

from engine.mathlib import Vec3
from GUI.GUI import LayoutHelper, Window
from GUI.menu import Menu
from memory import (
    boat_manager_handle,
    player_party_manager_handle,
)

logger = logging.getLogger(__name__)

player_party_manager = player_party_manager_handle()
boat_manager = boat_manager_handle()


class RouteCoordType(Enum):
    MOVE = auto()
    INTERACT_MOVE = auto()
    HOLD_DIRECTION = auto()


class RouteCoord:
    def __init__(self: Self, coord_type: RouteCoordType, coord: Vec3) -> None:
        self.coord_type = coord_type
        self.coord = coord

    def __repr__(self: Self) -> str:
        coord = f"{self.coord.x:.3f}, {self.coord.y:.3f}, {self.coord.z:.3f}"
        match self.coord_type:
            case RouteCoordType.MOVE:
                return f"Vec3({coord})"
            case RouteCoordType.INTERACT_MOVE:
                return f"InteractMove({coord})"
            case RouteCoordType.HOLD_DIRECTION:
                return f"HoldDirection({coord}, joy_dir=Vec2(x, y))"
        return ""


class RouteSegmentType(Enum):
    MOVE = auto()
    CLIMB = auto()
    CLIFF_MOVE = auto()
    CLIFF_CLIMB = auto()
    BOAT = auto()


class RouteSegment:
    def __init__(self: Self, segment_type: RouteSegmentType) -> None:
        self.segment_type = segment_type
        self.coords: list[RouteCoord] = []

    def add_coord(self: Self, coord: RouteCoord) -> None:
        self.coords.append(coord)

    def _type_str(self: Self) -> str:
        match self.segment_type:
            case RouteSegmentType.MOVE:
                return "SeqMove"
            case RouteSegmentType.CLIMB:
                return "SeqClimb"
            case RouteSegmentType.CLIFF_MOVE:
                return "SeqCliffMove"
            case RouteSegmentType.CLIFF_CLIMB:
                return "SeqCliffClimb"
            case RouteSegmentType.BOAT:
                return "SeqBoat"
        return ""

    def __repr__(self: Self) -> str:
        ret = f"{self._type_str()}(\n"
        ret += '    name="",  # Name\n'
        ret += "    coords=[\n"
        for coord in self.coords:
            ret += f"        {coord},\n"
        ret += "    ],\n"
        ret += ")"
        return ret


class RouteHelper(Menu):
    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Route helper")
        self.segments: list[RouteSegment] = []
        self.current_type = RouteSegmentType.MOVE

    def gui_section(
        self: Self, idx: int, segment_type: RouteSegmentType, coord: Vec3
    ) -> None:
        if imgui.button(f"Move##{idx}"):
            self.add_coord(
                coord=RouteCoord(RouteCoordType.MOVE, coord),
                segment_type=segment_type,
            )
        imgui.same_line()
        if imgui.button(f"Interact##{idx}"):
            self.add_coord(
                coord=RouteCoord(RouteCoordType.INTERACT_MOVE, coord),
                segment_type=segment_type,
            )
        imgui.same_line()
        if imgui.button(f"Hold##{idx}"):
            self.add_coord(
                coord=RouteCoord(RouteCoordType.HOLD_DIRECTION, coord),
                segment_type=segment_type,
            )

    def execute(self: Self, top_level: bool) -> bool:
        self.window.start_window(self.title)

        imgui.set_window_pos(
            self.title, imgui.ImVec2(5, 135), imgui.Cond_.first_use_ever
        )
        imgui.set_window_size(
            self.title, imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever
        )
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.text(f"{len(self.segments)} segments")
        if imgui.button("To clipboard"):
            imgui.core.set_clipboard_text(f"{self}")

        if imgui.button("CLEAR"):
            self.segments = []

        if len(self.segments) > 0:
            imgui.text(f"Last: {self.segments[-1].coords[-1]}")

        LayoutHelper.add_spacer()

        player_pos = Vec3(
            player_party_manager.position.x or 0,
            player_party_manager.position.y or 0,
            player_party_manager.position.z or 0,
        )

        imgui.text(
            f"Regular movement:{' (cur)' if self.current_type is RouteSegmentType.MOVE else ''}"
        )  # noqa: E501
        self.gui_section(1, RouteSegmentType.MOVE, coord=player_pos)
        LayoutHelper.add_spacer()

        imgui.text(
            f"Climb wall:{' (cur)' if self.current_type is RouteSegmentType.CLIMB else ''}"
        )  # noqa: E501
        self.gui_section(2, RouteSegmentType.CLIMB, coord=player_pos)
        LayoutHelper.add_spacer()

        gameobject_pos = Vec3(
            player_party_manager.gameobject_position.x or 0,
            player_party_manager.gameobject_position.y or 0,
            player_party_manager.gameobject_position.z or 0,
        )

        imgui.text(
            f"Ledge move:{' (cur)' if self.current_type is RouteSegmentType.CLIFF_MOVE else ''}"
        )  # noqa: E501
        self.gui_section(3, RouteSegmentType.CLIFF_MOVE, coord=gameobject_pos)
        LayoutHelper.add_spacer()

        imgui.text(
            f"Ledge climb:{' (cur)' if self.current_type is RouteSegmentType.CLIFF_CLIMB else ''}"
        )  # noqa: E501
        self.gui_section(4, RouteSegmentType.CLIFF_CLIMB, coord=gameobject_pos)
        LayoutHelper.add_spacer()

        boat_pos = Vec3(
            boat_manager.position.x or 0,
            boat_manager.position.y or 0,
            boat_manager.position.z or 0,
        )

        imgui.text(
            f"Boat:{' (cur)' if self.current_type is RouteSegmentType.BOAT else ''}"
        )  # noqa: E501
        self.gui_section(5, RouteSegmentType.BOAT, coord=boat_pos)

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret

    def add_coord(
        self: Self, coord: RouteCoord, segment_type: RouteSegmentType
    ) -> None:
        if not self.segments or segment_type != self.current_type:
            self.segments.append(RouteSegment(segment_type))
            self.current_type = segment_type
        self.segments[-1].add_coord(coord)

    def __repr__(self: Self) -> str:
        ret = ""
        for segment in self.segments:
            ret += f"{segment},\n"
        return ret
