{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ceb6fc60-cd12-4f3c-9de4-38e019762070",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting fastapi\n",
      "  Downloading fastapi-0.115.11-py3-none-any.whl.metadata (27 kB)\n",
      "Collecting uvicorn\n",
      "  Downloading uvicorn-0.34.0-py3-none-any.whl.metadata (6.5 kB)\n",
      "Requirement already satisfied: numpy in c:\\users\\rockr\\anaconda3\\lib\\site-packages (1.26.4)\n",
      "Requirement already satisfied: pandas in c:\\users\\rockr\\anaconda3\\lib\\site-packages (2.1.4)\n",
      "Requirement already satisfied: scikit-learn in c:\\users\\rockr\\anaconda3\\lib\\site-packages (1.2.2)\n",
      "Requirement already satisfied: joblib in c:\\users\\rockr\\anaconda3\\lib\\site-packages (1.2.0)\n",
      "Collecting starlette<0.47.0,>=0.40.0 (from fastapi)\n",
      "  Downloading starlette-0.46.1-py3-none-any.whl.metadata (6.2 kB)\n",
      "Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from fastapi) (1.10.12)\n",
      "Requirement already satisfied: typing-extensions>=4.8.0 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from fastapi) (4.12.2)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from uvicorn) (8.1.7)\n",
      "Requirement already satisfied: h11>=0.8 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from uvicorn) (0.14.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from pandas) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: scipy>=1.3.2 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from scikit-learn) (1.11.4)\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from scikit-learn) (2.2.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from click>=7.0->uvicorn) (0.4.6)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Requirement already satisfied: anyio<5,>=3.6.2 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from starlette<0.47.0,>=0.40.0->fastapi) (4.2.0)\n",
      "Requirement already satisfied: idna>=2.8 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi) (3.4)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\rockr\\anaconda3\\lib\\site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi) (1.3.0)\n",
      "Downloading fastapi-0.115.11-py3-none-any.whl (94 kB)\n",
      "   ---------------------------------------- 0.0/94.9 kB ? eta -:--:--\n",
      "   ---------------------------------------- 94.9/94.9 kB 5.6 MB/s eta 0:00:00\n",
      "Downloading uvicorn-0.34.0-py3-none-any.whl (62 kB)\n",
      "   ---------------------------------------- 0.0/62.3 kB ? eta -:--:--\n",
      "   ---------------------------------------- 62.3/62.3 kB ? eta 0:00:00\n",
      "Downloading starlette-0.46.1-py3-none-any.whl (71 kB)\n",
      "   ---------------------------------------- 0.0/72.0 kB ? eta -:--:--\n",
      "   ---------------------------------------- 72.0/72.0 kB 3.9 MB/s eta 0:00:00\n",
      "Installing collected packages: uvicorn, starlette, fastapi\n",
      "Successfully installed fastapi-0.115.11 starlette-0.46.1 uvicorn-0.34.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install fastapi uvicorn numpy pandas scikit-learn joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a34e72ad-28bd-425f-b704-c0813a23ae7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import joblib\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.neural_network import MLPRegressor\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "181557c3-e2e9-48c3-b140-6495285d6287",
   "metadata": {},
   "outputs": [],
   "source": [
    "file_path = \"MLE-Assignment.csv\"  # Change this if needed\n",
    "df = pd.read_csv(file_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5608d6b2-f8db-4eda-9161-79ff64447025",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"vomitoxin_ppb_log\"] = np.log1p(df[\"vomitoxin_ppb\"])\n",
    "X = df.iloc[:, 1:-2]  # Select relevant features\n",
    "y = df[\"vomitoxin_ppb_log\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "67087fea-07ae-4449-a884-c4862adcc6a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "scaler = StandardScaler()\n",
    "X_scaled = scaler.fit_transform(X)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e7680d14-6389-4aef-8265-f2b85b3cae57",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a1451661-5972-4cf6-b7e9-0c21b60ee98a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=500, random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">MLPRegressor</label><div class=\"sk-toggleable__content\"><pre>MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=500, random_state=42)</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "MLPRegressor(hidden_layer_sizes=(128, 64), max_iter=500, random_state=42)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Train model\n",
    "model = MLPRegressor(hidden_layer_sizes=(128, 64), activation=\"relu\", solver=\"adam\", max_iter=500, random_state=42)\n",
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e188394f-717b-42c6-bf8f-9af9d8bc0d27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model and scaler saved successfully!\n"
     ]
    }
   ],
   "source": [
    "joblib.dump(model, \"model.pkl\")\n",
    "joblib.dump(scaler, \"scaler.pkl\")\n",
    "\n",
    "print(\"✅ Model and scaler saved successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "53a5d582-4255-41cc-a916-693256ae37b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "python: can't open file 'C:\\\\Users\\\\rockr\\\\Imago\\\\train_model.py': [Errno 2] No such file or directory\n"
     ]
    }
   ],
   "source": [
    "!python train_model.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d386309-542b-46d1-9251-88cfaa8c4e6f",
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
