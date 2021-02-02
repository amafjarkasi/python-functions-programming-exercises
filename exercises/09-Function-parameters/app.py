# Your code goes here:
def render_person(first_name,dob,eye_color,age,gender):
    return ("%s is a %s years old %s born in %s with %s eyes" % (first_name,age,gender,dob,eye_color))


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))