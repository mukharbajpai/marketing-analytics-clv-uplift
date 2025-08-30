import pandas as pd

def load_data():
    transactions = pd.read_csv("data/raw/transactions.csv")
    campaigns = pd.read_csv("data/raw/campaign_outcomes.csv")
    return transactions, campaigns

if __name__ == "__main__":
    t, c = load_data()
    print("Transactions shape:", t.shape)
    print("Campaigns shape:", c.shape)
