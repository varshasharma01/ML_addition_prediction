import pandas as pd
import numpy as np

# this function will generate a dataset with 4 columns and 40 rows
# where the 4th column would be the sum of the first 3 columns
def generate_dataset():
    # create a DataFrame with 4 columns and 40 rows
    df = pd.DataFrame(np.random.randint(0, 100, size=(40, 3)), columns=['A', 'B', 'C'])
    
    # add a 4th column which is the sum of the first 3 columns
    df['D'] = df['A'] + df['B'] + df['C']
    
    return df

# we'll save it to a csv file
if __name__ == "__main__":
    dataset = generate_dataset()
    dataset.to_csv('generated_dataset_add.csv', index=False)
    print("Dataset generated and saved to 'generated_dataset.csv'")