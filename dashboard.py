
import matplotlib.pyplot as plt
import data_loader
import data_processor

def bar_chart(x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(14, 8))
    plt.bar(x_data, y_data, color='skyblue')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def line_chart(x_data, y_data, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, marker='o', linestyle='-', color='green')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

def dashboard(data, config):
    stat_result = data_processor.process_data(data, config)
    print(f"Computed Result ({config.get('operation')}): {stat_result}")

    plot_data = data_processor.get_filtered_data_for_plot(data, config)

    if not plot_data:
        print("No data found for the selected configuration.")
        return

    if config.get("year"):
        labels = [row['Country Name'] for row in plot_data]
        values = [row['Value'] for row in plot_data]
        
        print(f"Generating Bar Chart for Year: {config['year']}")
        bar_chart(labels, values, f"GDP in {config['year']}", "Country", "GDP")
        
    elif config.get("country"):
        labels = [row['Year'] for row in plot_data]
        values = [row['Value'] for row in plot_data]
        
        print(f"Generating Line Chart for Country: {config['country']}")
        line_chart(labels, values, f"GDP Trend for {config['country']}", "Year", "GDP")
        
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
