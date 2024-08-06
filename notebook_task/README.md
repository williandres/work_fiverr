# Steam Games from 2013 to 2023 success exploration
## by Hessa


## Dataset

**Steam Games from 2013 to 2023**

- games.csv

- t-games-categories.csv

- t-games-tags.csv

The 3 datasets are the work of Kaggle user 'Terenci Claramunt' who took care of cleaning and splitting datasets compiled by Steam API and Steam Spy.

Reference link: https://www.kaggle.com/datasets/terencicp/steam-games-december-2023

The 3 datasets compile the information of the releases that occurred between 2013 and 2023 of the most successful platform for selling video games on PC, Steam. With an estimated number of sales, release dates, among other kinds of variables that we will discuss later.

With these data sets we aim to find the factors that make a video game successful from the commercial to the general critical.

## Summary of Findings

The exploration revealed several key insights:

Price Distribution: A clear divide exists between free or low-priced games and those costing over $30. The growth of indie games has resulted in a significant number of affordable titles, often monetized through in-game purchases rather than upfront costs.

COVID-19 Impact: There was a noticeable dip in game releases in 2022 due to COVID-19, followed by a swift recovery and ongoing post-pandemic effects.

Data Transformations: Few transformations were necessary, aside from adjusting the release date plot. The most contentious issue is the large number of games with missing duration data, which is still useful through tags and categories.

Key Observations:

Ownership: A strong logarithmic correlation is observed between min_owners and max_owners, with clustering in certain ownership ranges.

Review Ratios: The distribution is skewed towards lower ratios, indicating many games receive moderate positive feedback. Games with high ratios are typically highly acclaimed.

Popularity and Reviews: Games with higher ownership numbers generally receive better reviews.

Additional Insights:

Game Length: Shorter games tend to have higher sales, and critically acclaimed games are often shorter in duration.

Release Trends: Game releases peak towards the end of the year, with free-to-play games having a notable impact on sales patterns.
Unexpected Findings:

Critical Acclaim vs. Sales: There is a weak correlation between critical acclaim and sales, suggesting that other factors are also significant in determining a game's success.

Popularity of Game Lengths: The varying popularity of games with extreme playtimes indicates diverse player preferences. The combination of free-to-play and indie games contributes to a strong market presence year-round.


## Key Insights for Presentation

### The relationship between sales, critical acclaim and game length.

Sales and Game Length: Shorter games (under 20 hours) typically have higher sales conversion rates.

Sales and Critical Acclaim: No strong link between sales and critical acclaim; high sales don't guarantee critical praise, and acclaimed games may not be bestsellers.

Critical Acclaim and Game Length: Shorter games (3 to 15 hours) tend to receive better reviews, but game length has a weak correlation with critical acclaim.

### Seasonal Trends in Game Releases

Games priced under $10 reign supreme, creating a distinct divide between indie and big-budget titles at the $20 mark. Indie games, despite their niche appeal, follow a release pattern akin to major productions: a lull in the middle of the year with a surge towards the end. Despite these trends, the overall pace of game launches remains surprisingly steady throughout the year.

### Sales Distribution: High-Priced vs. Modestly Priced Games

Initially, big-budget free-to-play games dominated the modest price category, saturating the market. As a result, higher-priced games achieved notable annual sales.

#### Conclusions

There is a clear split between free/inexpensive games and those over $30. The rise of indie games, often monetized through microtransactions, has significantly increased the number of lower-priced titles. COVID-19 briefly slowed game releases in 2022, but the market has since rebounded with lasting post-pandemic effects.

#### Key Insights:

Ownership and Pricing: Strong logarithmic relationship in ownership ranges.

Review Ratios: Generally low, with high ratios linked to critically acclaimed games.

Popularity and Reviews: Higher ownership tends to result in better reviews.

#### Additional Notes:

Game Length: Shorter games often achieve better sales and are more critically acclaimed.

Release Trends: Peak in releases towards year-end, driven by free-to-play games.

Critical Acclaim: Weak correlation with sales; multiple factors contribute to success.

The market continues to thrive with a dynamic mix of free-to-play and indie titles.