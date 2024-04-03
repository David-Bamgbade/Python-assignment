principal = input("Enter Principal ")
int(principal)
 
interest_rate = input("Enter rate ")
float(interest_rate)

number_of_years = input("How many years ")
int(number_of_years)

number_of_months_in_a_year = 12

monthly_rate1 = float(interest_rate) / 100

monthly_rate2 = monthly_rate1 / number_of_months_in_a_year

duration = int(number_of_years) * number_of_months_in_a_year
 
formular1 = monthly_rate2 *(1 + monthly_rate2) ** duration

formular2 = (1 + monthly_rate2)** duration - 1

formular3 = formular1 / formular2

monthly_payment = int(principal) * formular3

print('Your monthly payment is' ,round(monthly_payment, 2))




