{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "56ad252a-9262-446f-bbea-b36537da4744",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "import numpy as np\n",
    "from fastapi import FastAPI\n",
    "from pydantic import BaseModel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8c57720a-75ab-4d44-870b-9a553e8ce33e",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load(\"model.pkl\")\n",
    "scaler = joblib.load(\"scaler.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "198049c0-1e57-4075-a76b-aa1e0fdef2d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = FastAPI(title=\"DON Prediction API\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a227cc48-53a7-4d35-a4b7-8951e8bec2d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define input data format\n",
    "class SpectralData(BaseModel):\n",
    "    features: list  # Expecting a list of spectral reflectance values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b102d2a8-6637-464d-b63d-644f953ba22c",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.post(\"/predict\")\n",
    "def predict_don(data: SpectralData):\n",
    "    try:\n",
    "        # Convert input into numpy array\n",
    "        input_data = np.array(data.features).reshape(1, -1)\n",
    "\n",
    "        # Scale the input data\n",
    "        input_scaled = scaler.transform(input_data)\n",
    "\n",
    "        # Make prediction (log-transformed)\n",
    "        log_pred = model.predict(input_scaled)\n",
    "\n",
    "        # Convert back to original scale\n",
    "        don_prediction = np.expm1(log_pred)[0]\n",
    "\n",
    "        return {\"predicted_vomitoxin_ppb\": round(don_prediction, 3)}\n",
    "\n",
    "    except Exception as e:\n",
    "        return {\"error\": str(e)}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efcc8901-971d-4d53-9c30-4739891b5b19",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
