# -*- coding: utf-8 -*-
"""main

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UdkDiluqjlrMjPkUqbT2sCOvUv7CawkD
"""

! pip install pillow scikit-image tqdm numpy opencv-python trimesh pyexr

!git clone https://github.com/shunsukesaito/PIFu.git

!sh /content/PIFu/scripts/download_trained_model.sh

!python /content/PIFu/apps/crop_img.py -i /content/test_02.png -o /content/PIFu/sample_images

!cd PIFu && sh /content/PIFu/scripts/test.sh