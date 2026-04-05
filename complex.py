speakers={
    "Alice Johnson": ["Python Best Practices", "Data Science 101"],
    "Bob Smith": ["Machine Learning Basics", "Deep Learning Advanced"],
    "Charlie Brown": ["Web Development with Django", "Flask for Beginners"],
    "Caroline Davis": ["Data Visualization with Matplotlib", "Seaborn for Data Analysis"]
}

for speaker,topics in speakers.items():
     print(f"{speaker} will be speaking on the following topics:")
     for topic in topics:
         print(f"- {topic}")
     print()