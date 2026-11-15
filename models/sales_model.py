import numpy as np


def train_model(data):

    print("Training the model...")

    # 1. Input X = day of the month, output y = revenue
    X = data["Date"].dt.day.to_numpy()
    y = data["Revenue"].to_numpy()

    # 2. Find the best line: revenue = slope * day + intercept
    slope, intercept = np.polyfit(X, y, 1)

    # 3. Check the model quality (R2)
    predictions = slope * X + intercept
    ss_res = np.sum((y - predictions) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    score = 1 - ss_res / ss_tot
    print("Model score (R2):", round(score, 2))

    # 4. Keep the model in a dictionary
    model = {"slope": slope, "intercept": intercept}

    print("Model trained!")

    return model


def predict_revenue(model, day):

    # 1. Predict the revenue for a given day
    prediction = model["slope"] * day + model["intercept"]

    return prediction