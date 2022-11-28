import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-top-10-platforms.csv")

# Group by metrics
df_platform_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index()

df_platform_follow = df_platform_follow.rename(columns = {"follow_count": "total_follows"})

df_platform_hype = df.groupby(["platform_name"])["hype_count"].sum().reset_index()

df_platform_hype = df_platform_hype.rename(columns = {"hype_count": "total_hypes"})

# Analyze data
bar_width = 0.4

plt.bar(df_platform_follow.index - bar_width / 2, df_platform_follow["total_follows"], color = "blue", label = "number_of_follows", width = bar_width)
plt.bar(df_platform_hype.index + bar_width / 2, df_platform_hype["total_hypes"], color = "red", label = "number_of_hypes", width = bar_width)

plt.xticks(df_platform_follow.index, df_platform_follow["platform_name"])

plt.legend(loc = "upper left")
plt.show()