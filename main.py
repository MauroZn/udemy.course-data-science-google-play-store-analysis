import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import StrMethodFormatter

sns.set(style="whitegrid")

df = pd.read_csv("data/apps.csv")
df.drop_duplicates(inplace=True)

def run_challenge(description, func):
    print(f"\nChallenge: {description}")
    input("Press ENTER to see the result...\n")
    func()

# Challenge 1: Clean the data by removing NaN, duplicates, and converting data types appropriately
def clean_data():
    global df
    df.dropna(inplace=True)
    df_filtered = df[df['Rating'].apply(lambda x: isinstance(x, (int, float)))]
    df_filtered['Reviews'] = df_filtered['Reviews'].astype(int)
    df_filtered['Installs'] = df_filtered['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False).astype(int)
    df_filtered['Price'] = df_filtered['Price'].str.replace('$', '', regex=False).astype(float)
    df = df_filtered

# Challenge 2: Visualize the number of apps per category
def visualize_apps_per_category():
    category_count = df['Category'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_count.index[:15], y=category_count.values[:15],
                hue=category_count.index[:15], palette='viridis', legend=False)
    plt.xticks(rotation=45)
    plt.title('Top 15 App Categories')
    plt.xlabel('Category')
    plt.ylabel('Number of Apps')
    plt.tight_layout()
    plt.show()

# Challenge 3: Visualize average rating per category
def visualize_avg_rating_per_category():
    avg_rating = df.groupby('Category')['Rating'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=avg_rating.index[:15], y=avg_rating.values[:15],
                hue=avg_rating.index[:15], palette='magma', legend=False)
    plt.xticks(rotation=45)
    plt.title('Top 15 Categories by Average Rating')
    plt.xlabel('Category')
    plt.ylabel('Average Rating')
    plt.tight_layout()
    plt.show()

# Challenge 4: Explore the relationship between number of installs and ratings
def plot_rating_vs_installs():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Installs', y='Rating', hue='Category', legend=False, alpha=0.6)
    plt.xscale('log')
    plt.title('Rating vs Installs')
    plt.xlabel('Installs (log scale)')
    plt.ylabel('Rating')
    plt.tight_layout()
    plt.show()

# Challenge 5: Which genres have the most revenue potential?
def plot_revenue_by_genre():
    df['Revenue'] = df['Price'] * df['Installs']
    revenue_by_genre = df.groupby('Genres')['Revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=revenue_by_genre.index[:15], y=revenue_by_genre.values[:15], hue=revenue_by_genre.index[:15], palette='coolwarm', legend=False)
    plt.xticks(rotation=45)
    plt.title('Top 15 Genres by Revenue')
    plt.xlabel('Genre')
    plt.ylabel('Revenue')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))
    plt.tight_layout()
    plt.show()

# Challenge 6: Find the top-rated apps in each category
def print_top_rated_apps():
    top_rated = df.loc[df.groupby('Category')['Rating'].idxmax()]
    top_rated_sorted = top_rated.sort_values(by='Rating', ascending=False)
    print("Top Rated Apps by Category:")
    print(top_rated_sorted[['App', 'Category', 'Rating', 'Reviews', 'Installs']])


# ------------------ Run Challenges ------------------------------------------------------------------------------------

run_challenge("Clean the data by removing NaN, duplicates, and converting data types appropriately", clean_data)

run_challenge("Visualize the number of apps per category", visualize_apps_per_category)

run_challenge("Visualize average rating per category", visualize_avg_rating_per_category)

run_challenge("Explore the relationship between number of installs and ratings", plot_rating_vs_installs)

run_challenge("Which genres have the most revenue potential?", plot_revenue_by_genre)

run_challenge("Find the top-rated apps in each category", print_top_rated_apps)

