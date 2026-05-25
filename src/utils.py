import matplotlib.pyplot as plt
import seaborn as sns

def plot_churn_distribution(df):

    plt.figure(figsize=(6,4))

    sns.countplot(x="Churn", data=df)

    plt.title("Churn Distribution")

    plt.show()