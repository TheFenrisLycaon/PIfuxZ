import random

from torch.utils.data import Dataset


class BaseDataset(Dataset):
    """
    This is the Base Datasets.
    Itself does nothing and is not runnable.
    Check self.getItem function to see what it should return.
    """

    @staticmethod
    def modifyCLI(parser, is_train):
        return parser

    def __init__(self, opt, phase="train"):
        self.opt = opt
        self.is_train = self.phase == "train"
        self.projection_mode = "orthogonal"  # Declare projection mode here

    def __len__(self):
        return 0

    def getItem(self, index):
        # In case of a missing file or IO error, switch to a random sample instead
        try:
            res = {
                "name": None,  # name of this subject
                # Bounding box (x_min, y_min, z_min) of target space
                "b_min": None,
                # Bounding box (x_max, y_max, z_max) of target space
                "b_max": None,
                "samples": None,  # [3, N] samples
                "labels": None,  # [1, N] labels
                "img": None,  # [num_views, C, H, W] input images
                "calib": None,  # [num_views, 4, 4] calibration matrix
                "extrinsic": None,  # [num_views, 4, 4] extrinsic matrix
                "mask": None,  # [num_views, 1, H, W] segmentation masks
            }
            return res
        except:
            print(
                "Requested index %s has missing files. Using a random sample instead."
                % index
            )
            return self.getItem(index=random.randint(0, self.__len__() - 1))

    def __getitem__(self, index):
        return self.getItem(index)
