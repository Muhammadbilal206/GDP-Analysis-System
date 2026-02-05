import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import data_loader
import data_processor

try:
    plt.style.use('ggplot') 
except:
    pass

def get_strong_colors(n):
    cmap1 = cm.get_cmap('tab10', 10)
    cmap2 = cm.get_cmap('Dark2', 8)
    colors = [cmap1(i) for i in range(10)] + [cmap2(i) for i in range(8)]
    return colors[:n]

def bar_chart(labels, values, title, x_label, y_label):
    plt.figure(figsize=(13, 11))
    
    colors = get_strong_colors(len(labels))
    
    bars = plt.barh(labels, values, color='none', edgecolor=colors, linewidth=3, height=0.7)
    
    plt.title(title, fontsize=16, fontweight='bold', pad=20, color = 'red')
    plt.xlabel(y_label, fontsize=12, fontweight='bold')
    plt.ylabel(x_label, fontsize=12, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    
    ytick_labels = plt.gca().get_yticklabels()
    for label, color in zip(ytick_labels, colors):
        label.set_color(color)
        label.set_fontweight('bold')
        label.set_fontsize(12)

    for bar, color in zip(bars, colors):
        width = bar.get_width()
        plt.text(width * 1.01, bar.get_y() + bar.get_height()/2, 
                 f'{width:,.1f}', 
                 va='center', ha='left', fontsize=11, fontweight='bold', color=color)

    plt.tight_layout()
    plt.show()

def pie_chart(labels, values, title):
    plt.figure(figsize=(15, 15))
    
    colors = get_strong_colors(len(values))
    
    wedges, texts, autotexts = plt.pie(values, labels=labels, autopct='%1.1f%%', 
                                       startangle=180, colors=colors,
                                       pctdistance=1.1, labeldistance=1.25,
                                       wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
    
    for text, color in zip(texts, colors):
        text.set_color(color)
        text.set_fontweight('bold')
        text.set_fontsize(12)

    for autotext, color in zip(autotexts, colors):
        autotext.set_color(color) 
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)
            
    plt.title(title, fontsize=16, fontweight='bold', pad=50, color = 'red')
    plt.tight_layout()
    plt.show()

def line_chart(x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(12, 7))
    plt.plot(x_data, y_data, marker='o', linestyle='-', linewidth=3, color='#d62728', label='GDP')
    plt.fill_between(x_data, y_data, color='#d62728', alpha=0.1)
    
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel(x_label, fontsize=12, fontweight='bold')
    plt.ylabel(y_label, fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.show()

def scatter_chart(x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(12, 7))
    plt.scatter(x_data, y_data, color='#d62728', s=150, alpha=0.9, edgecolors='black', linewidth=1.5, label='GDP Data Points')
    
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel(x_label, fontsize=12, fontweight='bold')
    plt.ylabel(y_label, fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.ticklabel_format(style='plain', axis='y')
    plt.legend()
    plt.tight_layout()
    plt.show()

def dashboard(data, config):
    stat_result = data_processor.process_data(data, config)
    print(f"Computed Result ({config.get('operation')}): {stat_result / 1_000_000_000:,.2f} Billion")

    plot_data = data_processor.get_filtered_data_for_plot(data, config)

    if not plot_data:
        print("No data found for the selected configuration.")
        return

    scale_factor = 1_000_000_000

    if config.get("year"):
        year_data = [row for row in plot_data if row['Year'] == config['year']]
        year_data.sort(key=lambda x: x['Value'], reverse=True)
        
        top_n = 15
        year_data = year_data[:top_n]

        labels = [row['Country Name'] for row in year_data]
        values = [row['Value'] / scale_factor for row in year_data]
        
        region_title = config.get("region", "Global")
        
        plot_type = config.get("plot_type", "bar").lower()
        
        if plot_type == "pie":
            print(f"Generating Pie Chart for {region_title} in {config['year']}")
            pie_chart(labels, values, f"GDP Distribution - {region_title} ({config['year']})")
        else:
            print(f"Generating Bar Chart for {region_title} in {config['year']}")
            bar_chart(labels, values, f"GDP Ranking - {region_title} ({config['year']})", "Country", "GDP (Billions USD)")

    elif config.get("country"):
        plot_data.sort(key=lambda x: x['Year'])
        
        labels = [row['Year'] for row in plot_data]
        values = [row['Value'] / scale_factor for row in plot_data]
        
        plot_type = config.get("plot_type", "line").lower()
        
        if plot_type == "scatter":
            print(f"Generating Scatter Chart for Country: {config['country']}")
            scatter_chart(labels, values, f"GDP Scatter Analysis for {config['country']}", "Year", "GDP (Billions USD)")
        else:
            print(f"Generating Line Chart for Country: {config['country']}")
            line_chart(labels, values, f"GDP Trend for {config['country']}", "Year", "GDP (Billions USD)")
        
    else:
        print("Config not specific enough. Please specify a 'year' or 'country'.")

if __name__ == "__main__":
    config = data_loader.load_config("config.json")
    if config:
        file_path = config.get("file_path", "gdp_with_continent_filled.csv")
        raw_data = data_loader.load_data(file_path)
        if raw_data:
            dashboard(raw_data, config)
        else:
            print("Failed to load data.")
    else:
        print("Failed to load config.")
