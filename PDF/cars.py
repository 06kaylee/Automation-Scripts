import json
import locale
import sys
import emails
import reports
import pathlib

def load_data(filename):
  """Reads json data into a python object (dictionary)"""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a formatted name."""
  return f"{car['car_make']} {car['car_model']} ({car['car_year']})"


def process_data(data):
    """Finds the greatest amount of revenue, the greatest amount of sales, and the most popular car year"""
    max_revenue = {'revenue': 0}
    max_sales = {'sales': 0}
    years = {}
    for car in data:
        car_price = float(car['price'].strip('$'))
        total_sales = car['total_sales']
        car_year = car['car']['car_year']
        revenue = car_price * total_sales
        if revenue > max_revenue['revenue']:
            max_revenue['revenue'] = revenue
            max_revenue_car = car
        if total_sales > max_sales['sales']:
            max_sales['sales'] = total_sales
            max_sales_car = car
        if car_year not in years.keys():
            years[car_year] = total_sales
        else:
            years[car_year] += total_sales
    
    
    summary = [
        f"The {format_car(max_revenue_car['car'])} generated the most revenue: {max_revenue['revenue']}",
        f"The {format_car(max_sales_car['car'])} had the most sales: {max_sales['sales']}",
        f"The most popular year was {max(years, key = years.get)} with {max(years.values())} sales"
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists in order to generate a report."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for car in car_data:
      table_data.append([car["id"], format_car(car["car"]), car["price"], car["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data, generate a report, and send the report in an email."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    new_summary_newline = '\n'.join(summary)
    new_summary_br = '<br/>'.join(summary)
    reports.generate_report("car_report.pdf", "Car Report", new_summary_br, cars_dict_to_table(data))
    attachment_path = pathlib.Path('car_report.pdf')
    message = emails.generate_message('<sender>@example.com', '<recipient>@example.com', 'Sales Summary', new_summary_newline, attachment_path)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
