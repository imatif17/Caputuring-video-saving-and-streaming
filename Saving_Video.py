{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import cv2\n",
    "\n",
    "cam = cv2.VideoCapture(0)\n",
    "out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'DIVX'),20,(640,480))\n",
    "while(cam.isOpened()):\n",
    "    ret,frame = cam.read()\n",
    "    if ret:\n",
    "        frame = cv2.flip(frame,1)\n",
    "        out.write(frame)\n",
    "        cv2.imshow('frame',frame)\n",
    "        if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "            break\n",
    "    else:\n",
    "        break\n",
    "cam.release()\n",
    "out.release()\n",
    "cv2.destroyAllWindows()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
