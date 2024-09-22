import time
def age_to_dog(human_age):
    if human_age < 0:
        return 'Возраст не может быть отрицательным.'
    elif human_age <= 2:
        dog_age = human_age * 10.5
    else:
        dog_age = 21 + (human_age - 2) * 4
    return dog_age

age = float(input('Введите возраст в человеческих годах: '))
dog_age = age_to_dog(age)
print(f'Возраст собаки: {dog_age}')
time.sleep(1)
