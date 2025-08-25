"""
"""

from enum import Enum
from typing import List

import uuid


class Mode(Enum):
    """
    """
    
    FORWARD = 'forward'
    GLOBAL = 'global'


class EphemeralRig:
    """
    """

    def __init__(self, name: str, transforms: List[str]):
        """
        """

        self.name = name

        self.transforms = self.generate_transform_uids(transforms)
        self.uuid = uuid.uuid4()

        self.def_mode = Mode.FORWARD
        self.key_poses = {}  # What you can see as "keyed" on the timeline
        self.all_poses = {}  # All poses on all frames (interpolated + keyed)

    def generate_transform_uids(self, transforms: List[str]) -> dict:
        """
        """

        for tr in transforms:
            # TODO: Store as a metadata attr in the transform
            self.transforms[uuid.uuid4()] = tr

        return self.transforms

    def key_pose(self):
        """
        """

        pass

    def zero_out_transform(self):
        """
        """

        pass

    def go_to_bind_pose(self):
        """
        """

        pass

    def select_all_transforms(self):
        """
        """

        pass


class EphemeralRigSystem:
    """

    """
    
    def __init__(self, rigs: List[EphemeralRig] = None):
        """
        """
        
        self.rigs = rigs
        self.curr_mode = Mode.FORWARD
        self.curr_transform = ''
        self.curr_rig = None

    def build_transform_graph(self, transform: str):
        """
        """
        
        pass

    def on_transform_selected(self, transform: str):
        """
        """
        
        self.curr_transform = transform
        self.build_transform_graph(transform)
        # TODO: Key pose of current selected rig and update saved pose data in scene or JSON. If "auto-key" is ON,
        #  otherwise the user need to key the pose manually
        self.curr_rig.key_pose()
        
   
    def add_rig(self, name: str, transforms: list) -> EphemeralRig:
        """
        """
        
        rig = EphemeralRig(name, transforms)

        self.rigs.append(rig)

        return rig
