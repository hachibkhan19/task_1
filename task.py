def calculate_current_age(current_date, current_month, current_year,
                          birth_date, birth_month, birth_year):

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if birth_date > current_date:
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    if birth_month > current_month:
        current_year = current_year - 1
        current_month = current_month + 12

    date = current_date - birth_date
    month = current_month - birth_month
    year = current_year - birth_year

    print(f'Years:{year} months:{month} days:{date}')


current_date, current_month, current_year = map(int, input('Please enter your current date in same line and between '
                                                           'space: ').split())
birth_date, birth_month, birth_year = map(int, input(
    'Please enter your birth date in same line and between space: ').split())

calculate_current_age(current_date, current_month, current_year,
                      birth_date, birth_month, birth_year)
