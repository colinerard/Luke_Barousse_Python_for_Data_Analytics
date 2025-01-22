def calculate_annual_salary(hourly_wage, weekly_hours):
    """
    
    Calculate the total annual salary based on the hourly wage and hours per week. Assumes 52 working weeks / year.

    Args:
        hourly_wage (float): the hourly salary, in dollars / hours
        Weekly hours (float): hours per week
    
    Returns
        float: the total yearly salary
    
    """
    return hourly_wage * weekly_hours * 52