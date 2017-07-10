#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

	# Calculate errors
    errors = (net_worths-predictions)**2
    # Create cleaned tuple
    cleaned_data = zip(ages,net_worths,errors)
	# Sort data
    cleaned_data = sorted(cleaned_data, key=lambda x:x[2], reverse=True)
    # Specify limit for amount of data returned
    limit = int(len(net_worths)*0.1)
    
    return cleaned_data[limit:]

