import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style('darkgrid')

def load_data():
    exp_df = pd.read_csv('exp.csv')
    return exp_df

def print_column(exp_df):
   for column in exp_df.columns:
        print(column)


def plot_hist(arr1, arr2, label1, label2):
    plt.hist(arr1, color='r', alpha=0.5, label=label1)
    plt.hist(arr1, color='b', alpha=0.5, label=label1)
    plt.legend()
    plt.show()

def histogram(arg1, arg2, arg3, arg4):
    arg1[successful].hist(alpha = 0.5, bins = 20,label=arg2)
    arg1[failed].hist(alpha = 0.5, bins = 20,label=arg3)
    plt.legend()
    plt.show()
    plt.title(arg4)



if __name__ == '__main__':
  exp_df = load_data()
  print_column(exp_df)
  male = exp_df.query('gender == "M"')
  female = exp_df.query('gender == "F"')

  plot_hist(female.showed_up, male.showed_up, 'F', 'M')
  successful = exp_df.query('showed_up == "True"')
  failed = exp_df.query('showed_up == "False"')
