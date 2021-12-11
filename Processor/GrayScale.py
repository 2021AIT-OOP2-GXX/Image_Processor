import os
import cv2

from Processor.ProcessorBase import ProcessorBase


class GrayScaleProcessor(ProcessorBase):

    OUT_DIR = "./output_images/gs/"

    def process(self, filepath):
        out_filename = os.path.basename(filepath)
        img_bgr = cv2.imread(filepath)
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(self.OUT_DIR + out_filename, img_gray)
