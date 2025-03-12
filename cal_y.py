import calendar

# User chooses whether to see a full year or a specific month
type_choice = input("Would you like to see a full year's calendar or a specific month? (year/month): ").strip().lower()

y = int(input("Input the year: "))

if type_choice == "month":
      m = int(input("Input the month (1-12): "))
      print(calendar.month(y, m))
elif type_choice == "year":
      calendar.pryear(y)
else:
      print("Invalid choice. Please restart and enter 'year' or 'month'.")
