Write a clean and professional EDA synopsis for the *Price Distribution histogram*


Write a clean and professional EDA synopsis for the *Total Sales boxplot* based on this code:

plt.figure(figsize=(8,4))
plt.boxplot(df_featured['sales'], vert=False)
plt.xlabel("Sales")
plt.title("Total Sales - Outlier Detection (Boxplot)")
plt.grid(axis='x', linestyle='--')
plt.show()


# Subplot 1: Line Plot 
plt.subplot(2, 1, 1)  # (rows, columns, index)

# Adjust layout so titles/labels don't overlap
plt.tight_layout()
