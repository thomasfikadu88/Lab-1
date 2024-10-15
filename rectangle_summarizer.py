import csv
csv_file = 'Rectangles.csv'

def calculate_total_area(csv_file):
    total_area = 0

    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        
        for row in csv_reader:
            width = float(row['width'])  
            height = float(row['length'])  
            area = width * height  
            total_area += area  
    
    return total_area


csv_file = 'rectangles.csv'  
total_area = calculate_total_area(csv_file)
print(f"Total area of all rectangles: {total_area}")


import csv

def count_rows_in_csv(csv_file):
    Rectangle_count = 0

    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.reader(file)

        
        next(csv_reader)

        
        for row in csv_reader:
            Rectangle_count += 1
    
    return Rectangle_count


csv_file = 'rectangles.csv'  
total_rows = count_rows_in_csv(csv_file)
print(f"Total number of rows (excluding header): {total_rows}")

import csv
import statistics

def calculate_max_min_area(csv_file):
    areas = []  # List to store the areas

    # Open and read the CSV file
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV
        for row in csv_reader:
            width = float(row['width'])  # Convert width to float
            height = float(row['length'])  # Convert height to float
            area = width * height  # Calculate area
            areas.append(area)  # Add area to the list
    
    # Calculate max and min areas using statistics
    max_area = max(areas)
    min_area = min(areas)

    return max_area, min_area

# Use the function
csv_file = 'rectangles.csv'  # Replace with your CSV file path
max_area, min_area = calculate_max_min_area(csv_file)
print(f"Maximum area: {max_area}")
print(f"Minimum area: {min_area}")

import csv
import statistics

def calculate_average_area(csv_file):
    areas = []  # List to store the areas of rectangles

    # Open and read the CSV file
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV
        for row in csv_reader:
            width = float(row['width'])  # Convert width to float
            height = float(row['length'])  # Convert height to float
            area = width * height  # Calculate area
            areas.append(area)  # Append the area to the list
    
    # Calculate average area
    average_area = statistics.mean(areas) if areas else 0  # Check if areas list is not empty
    return average_area

csv_file = 'rectangles.csv' 
average_area = calculate_average_area(csv_file)
print(f"Average area of rectangles: {average_area}")

import csv
import statistics

def calculate_rectangle_statistics(csv_file):
    areas = []  
    total_count = 0  
    total_area = 0  

    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)

        
        for row in csv_reader:
            width = float(row['width'])  
            height = float(row['length'])  
            area = width * height  

            
            areas.append(area)  
            total_area += area  
            total_count += 1  

    
    average_area = statistics.mean(areas) if areas else 0
    max_area = max(areas) if areas else 0
    min_area = min(areas) if areas else 0

    return total_count, total_area, average_area, max_area, min_area

def write_statistics_to_csv(statistics, output_file):
    
    with open(output_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        
    
        csv_writer.writerow(['Total Count', 'Total Area', 'Average Area', 'Maximum Area', 'Minimum Area'])
        
        
        csv_writer.writerow(statistics)


input_csv_file = 'rectangles.csv'  
output_csv_file = 'summary.csv'  


statistics = calculate_rectangle_statistics(input_csv_file)


write_statistics_to_csv(statistics, output_csv_file)

print(f"Statistics written to {output_csv_file}")














