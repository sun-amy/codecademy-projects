"""
In this project, I wrote a program that takes an item's weight and calculates how much it'd cost to ship it using different shipping methods.
"""

weight = 41.5

#Ground Shipping

if weight <= 2 :
  ground_shipping_cost = 20 + 1.5 * weight
elif weight <= 6 :
  ground_shipping_cost = 20 + 3.0 * weight
elif weight <= 10 :
  ground_shipping_cost = 20 + 4.0 * weight
else :
  ground_shipping_cost = 20 + 4.75 * weight

#Ground Shipping Premium

ground_shipping_premium_cost = 125

#Drone Shipping

if weight <= 2 :
  drone_shipping_cost = 4.5 * weight
elif weight <= 6 :
  drone_shipping_cost = 9.0 * weight
elif weight <= 10 :
  drone_shipping_cost = 12.0 * weight
else :
  drone_shipping_cost = 14.25 * weight

print("Ground Shipping Cost: " + str(ground_shipping_cost))

print("Ground Shipping Premium Cost: " + str(ground_shipping_premium_cost))

print("Drone Shipping Cost: " + str(drone_shipping_cost))
