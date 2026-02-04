import functools

def process_data(data, config):
    filter_condition = lambda row: (
        (not config.get("region") or row["Region"] == config["region"]) and
        (not config.get("year") or row["Year"] == config["year"]) and
        (not config.get("country") or row["Country Name"] == config["country"])
    )
    
    filtered_data = list(filter(filter_condition, data))

    if not filtered_data:
        return 0

    gdp_values = list(map(lambda row: row["Value"], filtered_data))
    
    operation = config.get("operation", "average").lower()
    
    if operation == "sum":
        return sum(gdp_values)
    elif operation == "average":
        return sum(gdp_values) / len(gdp_values)

    def get_filtered_data_for_plot(data, config):
    filter_condition = lambda row: (
        (not config.get("country") or row["Country Name"] == config["country"]) and
        (not config.get("region") or row["Region"] == config["region"])
    )
    
    return list(filter(filter_condition, data))
        
    return 0



