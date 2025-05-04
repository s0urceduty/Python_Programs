import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time

# Initialize the data
df = pd.DataFrame({
    'Time': pd.date_range(start='2024-07-24', periods=10, freq='S'),
    'Sensor1': np.random.randn(10).cumsum(),
    'Sensor2': np.random.randn(10).cumsum(),
    'Sensor3': np.random.randn(10).cumsum()
})

# Create the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line1, = ax.plot(df['Time'], df['Sensor1'], label='Sensor1')
line2, = ax.plot(df['Time'], df['Sensor2'], label='Sensor2')
line3, = ax.plot(df['Time'], df['Sensor3'], label='Sensor3')

plt.legend()
plt.xlabel('Time')
plt.ylabel('Sensor Values')
plt.title('Live Data Line Graph')

# Function to update the plot
def update_plot(new_data):
    df.loc[len(df)] = new_data
    line1.set_xdata(df['Time'])
    line1.set_ydata(df['Sensor1'])
    line2.set_xdata(df['Time'])
    line2.set_ydata(df['Sensor2'])
    line3.set_xdata(df['Time'])
    line3.set_ydata(df['Sensor3'])
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()

# Simulate live data update
while True:
    new_time = df['Time'].iloc[-1] + pd.Timedelta(seconds=1)
    new_data = [new_time, np.random.randn(), np.random.randn(), np.random.randn()]
    update_plot(new_data)
    time.sleep(1)
