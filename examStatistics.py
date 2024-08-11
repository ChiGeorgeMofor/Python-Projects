grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    """Print each grade from the list."""
    for grade in grades_input:
        print(grade)
      
def grades_sum(scores):
    """Return the sum of the grades."""
    total = sum(scores)
    return total
 
def grades_average(grades_input):
    """Calculate and return the average of the grades."""
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average

def grades_variance(grades):
    """Calculate and return the variance of the grades."""
    mean = grades_average(grades)
    variance = sum((grade - mean) ** 2 for grade in grades) / len(grades)
    return variance

def grades_std_deviation(variance):
    """Calculate and return the standard deviation from variance."""
    return variance ** 0.5

# Calculate variance using the correct formula
variance = grades_variance(grades)

# Print individual grades
print("Grades:")
print_grades(grades)

# Print sum, average, variance, and standard deviation
print("Sum of grades:", grades_sum(grades))
print("Average of grades:", grades_average(grades))
print("Variance of grades:", variance)
print("Standard Deviation of grades:", grades_std_deviation(variance))
