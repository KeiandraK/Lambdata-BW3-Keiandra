{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Lovely_Baby():\n",
    "\n",
    "  secret_name = \"secret_boss_baby\"  \n",
    "  \n",
    "  def __init__(self, is_baby, first_name, last_name=\"baby\"):\n",
    "    \n",
    "      self.is_baby = is_baby\n",
    "      self.first_name = first_name\n",
    "      self.last_name = last_name\n",
    "      \n",
    "  def diaper_change(self):\n",
    "      \n",
    "      print(self.first_name, self.last_name, \"is beautiful\")\n",
    "  \n",
    "  \n",
    "class Happy_Mommy(Lovely_Baby):\n",
    "  \n",
    "  secret_name = \"superfly_boss_mommy\"\n",
    "  \n",
    "  # remember for this -- we only changed the last name.  \n",
    "  def __init__(self, is_baby, first_name, last_name=\"mommy\"):\n",
    "    \n",
    "      super().__init__(is_baby, first_name)\n",
    "      \n",
    "      self.last_name = last_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "bossy = Happy_Mommy(\"yes\", \"bossy\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bossy mommy is beautiful\n"
     ]
    }
   ],
   "source": [
    "bossy.diaper_change()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'superfly_boss_mommy'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bossy.secret_name"
   ]
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
