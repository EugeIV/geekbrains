import json

list_firm = []
average_dict = {}
firm_dict = {}
total_revenue = 0
firm_with_revenue = 0

with open("file_5_7.txt", "r", encoding="UTF-8") as file_firms:
    for line in file_firms:
        title, form_of_own, revenue, costs = line.split()
        net_profit = int(revenue) - int(costs)
        if net_profit > 0:
            total_revenue += net_profit
            firm_with_revenue += 1
        firm_dict[title] = net_profit
    list_firm.append(firm_dict)
    average_dict["average_profit"] = total_revenue // firm_with_revenue

list_firm.append(average_dict)
print(list_firm)

with open("json_file_5_7.json", "w") as json_file:
    json.dump(list_firm, json_file)
