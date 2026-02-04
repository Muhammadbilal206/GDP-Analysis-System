def process_data(data,config):
  filtered_data = [
    row for row in data
    if (not config.get("region") or row["Region"] == config["region"])
    and (not config.get("year") or row["Year"] == config["year"])
    and (not config.get("country") or row["Country Name"] == config["country"])
  ]
  if not filtered_data:
    return 0

  gdp_values = [row["Value"] for row in filtered_data]

  operation = config.get("operation","average").lower()
  if operation = "sum":
    return sum(gdp_values)
  elif operation = "average":
    return sum(gdp_values) / len(gdp_values)

  return 0



