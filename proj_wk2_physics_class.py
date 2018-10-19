def get_force(mass, acceleration):
  force = mass*acceleration
  return force

def get_energy(mass, c=3*10**8):
  energy = mass*c**2
  return energy

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * (5/9)
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return c_temp

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force*distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

print("100F is " + str(f100_in_celsius) + " in Celsius")
print("0C is " + str(c0_in_fahrenheit) + " in Fahrenheit")

train_mass = 22680
train_acceleration = 10
train_distance = 100

train_force = get_force(train_mass, train_acceleration)
train_work = get_work(train_mass, train_acceleration, train_distance)

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print("The GE train supplies " + str(train_force) + " Newtons of force.")
print("The GE train does " + str(train_force) + " Joules of work over " + str(train_distance)+" meters.")
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
