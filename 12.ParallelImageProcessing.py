from mpi4py import MPI
import numpy as np
import cv2

# Get the rank of the process and the size of the communicator
rank = MPI.COMM_WORLD.rank
size = MPI.COMM_WORLD.size

# read an image
img = cv2.imread("onion.png")

if rank == 1:
    # convert to gray
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image',img_gray)
    cv2.waitKey()

if rank == 2:
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # convert to blur
    img_blur = cv2.GaussianBlur(img_gray,(7,7),0)
    cv2.imshow('Blur Image', img_blur)
    cv2.waitKey()

if rank == 3:
    # finding edges using canny functions
    img_canny = cv2.Canny(img,200,200)
    cv2.imshow('Canny Image', img_canny)
    cv2.waitKey()


if rank == 0:
    cv2.imshow('original Image',img)
    cv2.waitKey()