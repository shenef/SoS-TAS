"""
Sets up the Route Helper imgui sub-window.

It is a tool that is used to quickly build long sequences of movement
nodes to inject into a TAS route (usually by grabbing player coordinates
and building long chains of `SeqMove` nodes).
"""

import logging
from enum import Enum, auto
from typing import Self

from imgui_bundle import imgui

from engine.mathlib import Vec2, Vec3
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
    """Which type of coordinate a certain entry is."""

    MOVE = auto()  # Vec3
    INTERACT_MOVE = auto()  # InteractMove
    HOLD_DIRECTION = auto()  # HoldDirection
    GRAPLOU = auto()  # Graplou
    BRACELET = auto()  # Mistral Bracelet


class RouteCoord:
    """Holds a coordinate and a type."""

    def __init__(self: Self, coord_type: RouteCoordType, coord: Vec3, joy_dir: Vec2 = None) -> None:
        self.coord_type = coord_type
        self.coord = coord
        self.joy_dir = joy_dir

    def __repr__(self: Self) -> str:
        coord = f"{self.coord.x:.3f}, {self.coord.y:.3f}, {self.coord.z:.3f}"
        match self.coord_type:
            case RouteCoordType.MOVE:
                return f"Vec3({coord})"
            case RouteCoordType.INTERACT_MOVE:
                return f"InteractMove({coord})"
            case RouteCoordType.HOLD_DIRECTION:
                return f"HoldDirection({coord}, joy_dir=Vec2(x, y))"
            case RouteCoordType.GRAPLOU:
                return f"Graplou({coord}, joy_dir=Vec2(x, y), hold_timer=0.1)"
            case RouteCoordType.BRACELET:
                joy_dir = f"Vec2({self.joy_dir.x}, {self.joy_dir.y})"
                return f"MistralBracelet(joy_dir={joy_dir})"
        return ""


class RouteSegmentType(Enum):
    """Which type of sequencer node should be used for this segment."""

    MOVE = auto()  # SeqMove
    CLIMB = auto()  # SeqClimb
    CLIFF_MOVE = auto()  # SeqCliffMove
    CLIFF_CLIMB = auto()  # SeqCliffClimb
    BOAT = auto()  # SeqBoat
    BRACELET_PUZZLE = auto()  # SeqBraceletPuzzle


class RouteSegment:
    """Holds a single segment of the current route, with a list of coordinates and a type."""

    def __init__(self: Self, segment_type: RouteSegmentType) -> None:
        self.segment_type = segment_type
        self.coords: list[RouteCoord] = []

    def add_coord(self: Self, coord: RouteCoord) -> None:
        """Add a new coordinate to this segment."""
        self.coords.append(coord)

    def _type_str(self: Self) -> str:
        """Map segment type to a string representing the sequencer node."""
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
            case RouteSegmentType.BRACELET_PUZZLE:
                return "SeqBraceletPuzzle"
        return ""

    def __repr__(self: Self) -> str:
        ret = f"{self._type_str()}(\n"
        ret += '    name="",\n'
        ret += "    coords=[\n"
        for coord in self.coords:
            ret += f"        {coord},\n"
        ret += "    ],\n"
        ret += ")"
        return ret


class _Direction:
    """Direction and label."""

    def __init__(self: Self, joy_dir: Vec2, label: str) -> None:
        self.joy_dir = joy_dir
        self.label = label


class RouteHelper(Menu):
    """The actual imgui menu. Contains the code to set up the GUI window."""

    def __init__(self: Self, window: Window) -> None:
        super().__init__(window, title="Route helper")
        self.segments: list[RouteSegment] = []
        self.current_type = RouteSegmentType.MOVE

    def gui_section(
        self: Self, idx: int, segment_type: RouteSegmentType, coord: Vec3, coord2: Vec3 = None
    ) -> None:
        """
        Generate the GUI section (a set of buttons) for a particular segment.

        The coord parameter should usually be the current player position.
        """
        if imgui.button(f"Move##{idx}"):
            self.add_coord(
                coord=RouteCoord(RouteCoordType.MOVE, coord),
                segment_type=segment_type,
            )
        if segment_type not in {RouteSegmentType.BOAT, RouteSegmentType.BRACELET_PUZZLE}:
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
        if segment_type == RouteSegmentType.MOVE:
            imgui.same_line()
            if imgui.button(f"Graplou##{idx}"):
                self.add_coord(
                    # Use gameobject coord for this
                    coord=RouteCoord(RouteCoordType.GRAPLOU, coord2),
                    segment_type=segment_type,
                )
        if segment_type == RouteSegmentType.BRACELET_PUZZLE:
            directions = [
                _Direction(joy_dir=Vec2(1, 0), label="E"),
                _Direction(joy_dir=Vec2(0, 1), label="N"),
                _Direction(joy_dir=Vec2(-1, 0), label="W"),
                _Direction(joy_dir=Vec2(0, -1), label="S"),
            ]
            for direction in directions:
                imgui.same_line()
                if imgui.button(f"Bracelet({direction.label})"):
                    self.add_coord(
                        coord=RouteCoord(RouteCoordType.BRACELET, coord, joy_dir=direction.joy_dir),
                        segment_type=segment_type,
                    )

    def execute(self: Self, top_level: bool) -> bool:
        """Render the menu and handle input."""
        self.window.start_window(self.title)

        imgui.set_window_pos(self.title, imgui.ImVec2(5, 135), imgui.Cond_.first_use_ever)
        imgui.set_window_size(self.title, imgui.ImVec2(240, 410), cond=imgui.Cond_.first_use_ever)
        imgui.set_window_collapsed(1, cond=imgui.Cond_.once)

        imgui.text(f"{len(self.segments)} segments")
        if imgui.button("To clipboard"):
            imgui.set_clipboard_text(f"{self}")

        if imgui.button("CLEAR"):
            self.segments = []

        if len(self.segments) > 0:
            imgui.text(f"Last: {self.segments[-1].coords[-1]}")

        LayoutHelper.add_spacer()

        player_pos = player_party_manager.position or Vec3(0, 0, 0)

        gameobject_pos = player_party_manager.gameobject_position or Vec3(0, 0, 0)

        imgui.text(
            f"Regular movement:{' (cur)' if self.current_type is RouteSegmentType.MOVE else ''}"
        )
        self.gui_section(1, RouteSegmentType.MOVE, coord=player_pos, coord2=gameobject_pos)
        LayoutHelper.add_spacer()

        imgui.text(f"Climb wall:{' (cur)' if self.current_type is RouteSegmentType.CLIMB else ''}")
        self.gui_section(2, RouteSegmentType.CLIMB, coord=player_pos)
        LayoutHelper.add_spacer()

        imgui.text(
            f"Ledge move:{' (cur)' if self.current_type is RouteSegmentType.CLIFF_MOVE else ''}"
        )
        self.gui_section(3, RouteSegmentType.CLIFF_MOVE, coord=gameobject_pos)
        LayoutHelper.add_spacer()

        imgui.text(
            f"Ledge climb:{' (cur)' if self.current_type is RouteSegmentType.CLIFF_CLIMB else ''}"
        )
        self.gui_section(4, RouteSegmentType.CLIFF_CLIMB, coord=gameobject_pos)
        LayoutHelper.add_spacer()

        boat_pos = boat_manager.position or Vec3(0, 0, 0)

        imgui.text(f"Boat:{' (cur)' if self.current_type is RouteSegmentType.BOAT else ''}")
        self.gui_section(5, RouteSegmentType.BOAT, coord=boat_pos)
        LayoutHelper.add_spacer()

        imgui.text(
            f"Bracelet Puzzle:{' (cur)' if self.current_type is RouteSegmentType.BRACELET_PUZZLE else ''}"  # noqa E501
        )
        self.gui_section(6, RouteSegmentType.BRACELET_PUZZLE, coord=player_pos)

        ret = False
        if not top_level and imgui.button("Back"):
            ret = True
        self.window.end_window()
        return ret

    def add_coord(self: Self, coord: RouteCoord, segment_type: RouteSegmentType) -> None:
        """Add a new coordinate to the current segment, or start a new segment."""
        if not self.segments or segment_type != self.current_type:
            self.segments.append(RouteSegment(segment_type))
            self.current_type = segment_type
        self.segments[-1].add_coord(coord)

    def __repr__(self: Self) -> str:
        ret = ""
        for segment in self.segments:
            ret += f"{segment},\n"
        return ret
