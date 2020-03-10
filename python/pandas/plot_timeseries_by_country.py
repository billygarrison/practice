from datetime import datetime
import os
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker

# Parameters
country = "Japan"
save_data = True
min_cases = 1

# Read in data, subset to country
data = pd.read_csv("timeseries-data.csv", header=0)
data = data[data["Country/Region"] == country]

# Set up plot
ax = plt.gca()
formatter = mdates.DateFormatter("%b %#d/%y")  # ex: Mar 8/20
ax.xaxis.set_major_formatter(formatter)
locator = ticker.MultipleLocator(14)  # 14 days between xticks
ax.xaxis.set_major_locator(locator)

# Holds names for plot legend
labels = []

# Raise error if no records found for this country
if len(data.index) == 0:
    raise ValueError("Country not found: " + country)

# Single record means country isn't subdivided into provinces/states
if len(data.index) == 1:
    # Transpose dataframe and remove useless info
    df = data.T[5:]

    # Convert date index to column, rename columns
    df.reset_index(level=0, inplace=True)
    df.columns = ["date", "cases"]

    # Convert date string column to datetime
    df["date"] = pd.to_datetime(df.date)

    # Write CSV for this state/province
    if save_data:
        if not os.path.exists("data"):
            os.mkdir("data")
        file_path = os.path.join("data", country + ".csv")
        df.to_csv(file_path, index=False)

    # Add this state/province to plot
    plt.plot(df["date"], df["cases"])
    labels.append(country)

    # Get latest date to display on plot
    last_update = max(df["date"])

# Multiple records means multiple provinces/states
if len(data.index) > 1:
    # Subset to provinces/states with more cases that minimum specified
    data = data[data.iloc[:, -1] >= min_cases]
    if len(data.index) == 0:
        raise ValueError(
            "No provinces/states in " + country,
            + " with a minimum of " + min_cases,
            + " cases"
        )

    # Group by province/state
    data_groups = data.groupby("Province/State")

    # Loop through provinces/states
    for name, group in data_groups:
        # Transpose dataframe and remove useless info
        df = group.T[5:]

        # Convert date index to column, rename columns
        df.reset_index(level=0, inplace=True)
        df.columns = ["date", "cases"]

        # Convert date string column to datetime
        df["date"] = pd.to_datetime(df.date)

        # Write CSV for this state/province
        if save_data:
            dir_path = os.path.join("data", country)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            file_path = os.path.join(dir_path, name + ".csv")
            df.to_csv(file_path, index=False)

        # Add this state/province to plot
        plt.plot(df["date"], df["cases"])
        labels.append(name)

        # Get latest date to display on plot
        last_update = max(df["date"])

# Set plot title and legend
today = datetime.today().strftime("%B %#d, %Y")
last_update_str = last_update.strftime("%B %#d, %Y")
plt.title("Data from " + last_update_str + "\nPlot created " + today)
plt.legend(labels, loc="upper left", ncol=1, fancybox=True, shadow=True)

# Save current figure
fig_dir = "figures"
if not os.path.exists(fig_dir):
    os.makedirs(fig_dir)
fig_file = os.path.join(fig_dir, country + ".png")
fig = plt.gcf()
fig.set_size_inches(11, 8.5)
fig.savefig(fig_file, bbox_inches="tight")