import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def chart(a):
    labels_pie = ['Sad', 'Happy', 'Relaxed', 'Angry']
    sizes_pie = a
    colors_pie = ['pink', 'yellow', 'green', 'red']

    labels_bar = ['Sad', 'Happy', 'Relaxed', 'Angry', 'Total']
    sizes_bar = a + [sum(a)]
    colors_bar = ['pink', 'yellow', 'green', 'red', 'blue']

    plt.subplot(121)
    plt.pie(sizes_pie, colors=colors_pie, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Emotions Distribution')

    plt.subplot(122)
    plt.bar(labels_bar, sizes_bar, color=colors_bar)
    plt.xlabel('Emotions')
    plt.ylabel('Time')
    plt.title('Time Taken for Each Emotion')

    legend_elements = [Patch(facecolor=color, label=label) for color, label in zip(colors_bar[:-1], labels_bar[:-1])]
    plt.legend(handles=legend_elements)

    plt.tight_layout(pad=1.0)
    plt.show()
