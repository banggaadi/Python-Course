{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "489b9d5b",
   "metadata": {},
   "source": [
    "### Modified Tax Calculator\n",
    "\n",
    "Since the tax calculator we made was primarily for our Stowe employees, let's modify the tax calculator below to have a default tax rate of 6%. \n",
    "\n",
    "Also, we want the output of the function to return a list containing the subtotal, tax, and totals."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4105f94b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def tax_calculator(subtotal):\n",
    "    taxpct = 0.06\n",
    "    tax = subtotal * taxpct\n",
    "    total = subtotal + tax\n",
    "    lst = []\n",
    "    lst.extend((subtotal, tax, total))\n",
    "    return lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2784deb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 6.0, 106.0]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tax_calculator(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "859295e6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
