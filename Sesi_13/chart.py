import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

file_path = "Sesi_13/updated_score.xlsx"  
df = pd.read_excel(file_path)

print("First 5 rows of the dataframe:")
print(df.head())
print("\nDataFrame Info:")
df.info()
print("\nGrade counts before any manipulation (to check for unexpected values):")
print(df['Grade'].value_counts(dropna=False))

grade_counts = df['Grade'].value_counts().sort_index()

grade_percentages = (grade_counts / grade_counts.sum()) * 100

print("\nGrade Counts:")
print(grade_counts)
print("\nGrade Percentages:")
print(grade_percentages)

colors = ['#4CAF50', '#2196F3', '#FFC107', '#FF5722', '#607D8B'] 

plt.figure(figsize=(10, 7))
plt.pie(grade_percentages, labels=grade_percentages.index, autopct='%1.1f%%', startangle=140, colors=colors[:len(grade_percentages)])
plt.title('Persentase Distribusi Kelompok Nilai (Pie Chart)')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('grade_distribution_pie_chart.png')
print("\nPie chart saved as 'grade_distribution_pie_chart.png'")
plt.show() 

plt.figure(figsize=(10, 7)) 
bars = plt.bar(grade_percentages.index, grade_percentages.values, color=colors[:len(grade_percentages)])
plt.title('Persentase Distribusi Kelompok Nilai (Bar Chart)')
plt.xlabel('Kelompok Nilai')
plt.ylabel('Persentase (%)')
plt.ylim(0, max(grade_percentages.values) * 1.15 if not grade_percentages.empty else 100) 
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter()) 

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.savefig('grade_distribution_bar_chart.png')
print("Bar chart saved as 'grade_distribution_bar_chart.png'")
plt.show() 

print("\nMatplotlib's plt.show() command has been called for each chart.")
print("If you are running this in a graphical environment, the charts should appear in separate windows.")