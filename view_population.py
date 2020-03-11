import turtle as t

NAME = 0
POINTS = 1
POP = 2


# Create the state layer
state = ["COLORADO", [[-109, 37], [-109, 41], [-102, 41], [-102, 37]], 5187582]

# Cities layer list
# city = [name, [point], population]
cities = []

# Add Denver
cities.append(["DENVER", [-104.98, 39.74], 634265])
# Add Boulder
cities.append(["BOULDER", [-105.27, 40.02], 98889])
# Add Durango
cities.append(["DURANGO", [-107.88, 37.28], 17069])

map_width = 800
map_height = 600


x_min = 180
x_max = -180
y_min = 180
y_max = -180
for (x,y) in state[POINTS]:
    if x >= x_max:
        x_max = x
    if x <= x_min:
        x_min = x

    if y >= y_max:
        y_max = y
    if y <= y_min:
        y_min = y

dist_x = x_max - x_min
dist_y = y_max - y_min
x_ratio = map_width /  dist_x
y_ratio = map_height / dist_y


def convert(point):
    lat = point[0]
    lon = point[1]
    new_lat = map_width - (x_max - lat)*x_ratio
    new_lon = map_height - (y_max - lon)*y_ratio
    # Python turtle graphics start in the middle of the screen
    # so we must offset the points so they are centered
    new_lat = new_lat - (map_width/2)
    new_lon = new_lon - (map_height/2)
    return [new_lat, new_lon]

def draw_state_boundary():
    t.up()
    first_pixel = None
    for cordinate in state[POINTS]:
        converted_pixel = convert(cordinate)
        if not first_pixel:
            first_pixel = converted_pixel
        print(converted_pixel)
        t.goto(converted_pixel)
        t.down()

    t.goto(first_pixel)
    t.up()
    t.goto([0,0])
    t.write(state[NAME], align = 'center', font=("Arial",22,"bold"))

def plot_cities():
    for city in cities:
        pixel = convert(city[POINTS])
        t.up()
        t.goto(pixel)
        # Place a point for the city
        t.dot(10)
        # Label the city
        t.write(city[NAME] + ", Pop.: " + str(city[POP]), 
        align="left", font=("Arial",16))

draw_state_boundary()
plot_cities()


most_populated_city = max(cities, key= lambda city:city[POP])
farthest_south_city = min(cities, key= lambda city:city[POINTS][0])
t.goto(-(map_width/2)+10, -(map_height/2)-20)
t.write("Most densely populated city is "+ most_populated_city[NAME], font=("Arial",16))
t.goto(-(map_width/2)+10, -(map_height/2)-40)
t.write("City situated in the farthest south is "+ farthest_south_city[NAME], font=("Arial",16))


t.pen(shown=False)
t.done()


