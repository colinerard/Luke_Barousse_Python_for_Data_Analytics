def calculate_salary(base_salary, bonus_rate=.1):
    """
    
    Calculate the total salary based on the base salary and a bonus rate.

    Args:
        base_salary (float): the base salary
        bonus_rate (float): the bonus rate. Default is .1
    
    Returns
        float: the total salary
    
    """
    return base_salary * (1 + bonus_rate)

def calculate_bonus(total_salary, base_salary):
    return (total_salary - base_salary) / base_salary