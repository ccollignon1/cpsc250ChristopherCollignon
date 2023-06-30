import pandas as pd

file_name = input()

# TODO: Read in file_name as a dataframe
df = pd.read_csv(file_name, delimiter='\t')

# TODO: Output rows by descending Final scores
df_sorted = df.sort_values('Final', ascending=False)
print(df_sorted)
print("\nMax Scores:")

# TODO: Output the max scores of each assignment
max_scores = df.max(numeric_only=True)
print(max_scores.to_string())
print("\nMedian Scores:")

# TODO: Output the median scores of each assignment
median_scores = df.median(numeric_only=True)
print(median_scores.to_string())
print("\nAverage Scores:")

# TODO: Output the average scores of each assignment.
average_scores = df.mean(numeric_only=True)
print(average_scores.to_string())
print("\nStandard Deviation:")

# TODO: Output the standard devation of each assignment.
std_dev = df.std(numeric_only=True)
print(std_dev.to_string())