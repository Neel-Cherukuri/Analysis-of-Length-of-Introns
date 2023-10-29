# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('~/exgr_test.csv')

#basic information about the data frame and the first few rows
print(data.info())
print(data.head())

# Convert data to a DataFrame
data = pd.DataFrame(data)

# Total number of unique transcripts
total_unique_transcripts = data['transcript_id'].nunique()

# Total number of unique exons
total_unique_exons = data['exon_id'].nunique()

# Print the results
print("Total number of unique transcripts:", total_unique_transcripts)
print("Total number of unique exons:", total_unique_exons)

# Calculate the average length of exons
average_exon_length = data['width'].mean()

# Print the results
print("Average length of exons:", average_exon_length)

# Calculate the median length of exons
median_exon_length = data['width'].median()

# Print the result
print("Median length of exons:", median_exon_length)

# Initialize intron_length with zeros
data['intron_length'] = 0

# Calculate intron lengths
data['intron_length'] = data.groupby('transcript_id').apply(lambda group: [0] + list(group['start'].values[1:] - group['end'].values[:-1])).explode().values
data['intron_length'] = data['intron_length'].clip(lower=0)

# Print some rows to verify the result
print(data.head())

# Bonus task

# Calculate L1, L2, U1, U2
data['L1'] = np.maximum(data['start'] - 100, 1)
data['L2'] = np.minimum(data['start'] + 100, data['end'])
data['U1'] = np.maximum(data['end'] - 100, data['start'])
data['U2'] = data['end'] + 100

# Adjust L and U regions if they overlap or if exon/intron is too short
data['L2'] = np.where(data['L2'] - data['L1'] < 200, data['start'] + (data['end'] - data['start']) / 2, data['L2'])
data['U1'] = np.where(data['U2'] - data['U1'] < 200, data['end'] - (data['end'] - data['start']) / 2, data['U1'])

# Ensure L2 and U1 do not overlap
data['L2'] = np.minimum(data['L2'], data['U1'] - 1)
data['U1'] = np.maximum(data['U1'], data['L2'] + 1)

# Print some rows to verify the result
print(data.head())

# Prepare data for plotting
L_intervals = data['L2'] - data['L1']
U_intervals = data['U2'] - data['U1']

# Plot L intervals
plt.figure(figsize=(10, 5))
plt.hist(L_intervals, bins=range(int(L_intervals.min()), int(L_intervals.max()) + 1), color='skyblue', edgecolor='black')
plt.title('Distribution of Intervals at 5’ End (L1 to L2)')
plt.xlabel('Interval Length')
plt.ylabel('Frequency')
plt.savefig('L_intervals_plot.png')
plt.show()

# Plot U intervals
plt.figure(figsize=(10, 5))
plt.hist(U_intervals, bins=range(int(U_intervals.min()), int(U_intervals.max()) + 1), color='lightgreen', edgecolor='black')
plt.title('Distribution of Intervals at 3’ End (U1 to U2)')
plt.xlabel('Interval Length')
plt.ylabel('Frequency')
plt.savefig('U_intervals_plot.png')
plt.show()

