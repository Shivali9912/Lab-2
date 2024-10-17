
import csv

area_list=[]

with open('rectangles_data.csv', newline="") as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader:
        width = float(row[1])   #converting from string to float
        length = float(row[2])


        area = width * length
        area_list.append(area)


# calculations

total_count =len(area_list)
total_area = sum(area_list)
average_area = total_area / total_count
maximum_area = max(area_list)
minimum_area = min(area_list)


print(f"Total_Count: {total_count}")
print(f"Total_Area: {total_area}")
print(f"Average_Area: {average_area}")
print(f"Maximum_Area: {maximum_area}")
print(f"Minimum_Area: {minimum_area}")


# Create a csv

import csv
Summary = [
    ('Total_Count',total_count),
    ('Total_Area', total_area),
    ('Average_Area', average_area),
    ('Maximum_Area', maximum_area),
    ('Minimum_Area',minimum_area )
]

for r in Summary:
    print(r)

with open("summary.csv", 'w', newline="" ) as f:
     writer = csv.writer (f)
     writer.writerow([r[0] for r in Summary]), 
     writer.writerow([r[1] for r in Summary])


    
        




