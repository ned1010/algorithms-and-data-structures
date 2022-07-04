
class Graph_Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.position = (x, y)
    
    def __lt__(self, other):
        return self.name < other.name

thirty_third_and_madison = Graph_Vertex("33rd Street and Madison Avenue", 33, 4)
thirty_third_and_fifth = Graph_Vertex("33rd Street and 5th Avenue", 33, 5)
manhattan_mall = Graph_Vertex("Manhattan Mall", 33, 6)
penn_station = Graph_Vertex('Penn Station', 33, 7)
thirty_fourth_and_madison = Graph_Vertex("34th Street and Madison Avenue", 34, 4)
empire_state_building = Graph_Vertex('Empire State Building', 34, 5)
herald_square = Graph_Vertex('Herald Square', 34, 6)
thirty_fourth_and_seventh = Graph_Vertex("34th Street and 7th Avenue", 34, 7)
thirty_fifth_and_madison = Graph_Vertex("35th Street and Madison Avenue", 35, 4)
cuny_grad_center = Graph_Vertex("CUNY Graduate Center", 35, 5)
thirty_fifth_and_sixth = Graph_Vertex("35th Street and 6th Avenue", 35, 6)
macys = Graph_Vertex("Macy's", 35, 7)
thirty_sixth_and_madison = Graph_Vertex("36th Street and Madison Avenue", 36, 4)
thirty_sixth_and_fifth = Graph_Vertex("36th Street and 5th Avenue", 36, 5)
thirty_sixth_and_sixth = Graph_Vertex("36th Street and 6th Avenue", 36, 6)
thirty_sixth_and_seventh = Graph_Vertex("36th Street and 7th Avenue", 36, 7)
morgan_library = Graph_Vertex("Morgan Library and Museum", 37, 4)
thirty_seventh_and_fifth = Graph_Vertex("37th Street and 5th Avenue", 37, 5)
thirty_seventh_and_sixth = Graph_Vertex("37th Street and 6th Avenue", 37, 6)
thirty_seventh_and_seventh = Graph_Vertex("37th Street and 7th Avenue", 37, 7)
thirty_eighth_and_madison = Graph_Vertex("38th Street and Madison Avenue", 38, 4)
thirty_eighth_and_fifth = Graph_Vertex("38th Street and Fifth Avenue", 38, 5)
thirty_eighth_and_sixth = Graph_Vertex("38th Street and Sixth Avenue", 38, 6)
thirty_eighth_and_seventh = Graph_Vertex("38th Street and Seventh Avenue", 38, 7)
mexican_consulate = Graph_Vertex("Mexican Consulate General", 39, 4)
thirty_ninth_and_fifth = Graph_Vertex("39th Street and Fifth Avenue", 39, 5)
thirty_ninth_and_sixth = Graph_Vertex("39th Street and Sixth Avenue", 39, 6)
thirty_ninth_and_seventh = Graph_Vertex("39th Street and Seventh Avenue", 39, 7)
fortieth_and_madison = Graph_Vertex("40th Street and Madison Avenue", 40, 4)
fortieth_and_fifth = Graph_Vertex("40th Street and Fifth Avenue", 40, 5)
bryant_park_south = Graph_Vertex("Bryant Park South", 40, 6)
times_square_south = Graph_Vertex("Times Square - South", 40, 7)
forty_first_and_madison = Graph_Vertex("41st Street and Madison Avenue", 41, 4)
mid_manhattan_library = Graph_Vertex("Mid-Manhattan Library", 41, 5)
kinokuniya = Graph_Vertex("Kinokuniya", 41, 6)
times_square = Graph_Vertex("Times Square", 41, 7)
grand_central_station = Graph_Vertex("Grand Central Station", 42, 4)
library = Graph_Vertex("New York Public Library", 42, 5)
bryant_park_north = Graph_Vertex("Bryant Park North", 42, 6)
times_square_north = Graph_Vertex("Times Square - North", 42, 7)

manhattan_graph = {
  thirty_third_and_madison: set([(thirty_fourth_and_madison, 1), (thirty_third_and_fifth, 3)]),
  thirty_third_and_fifth: set([(thirty_third_and_madison, 3), (manhattan_mall, 3), (empire_state_building, 1)]),
  manhattan_mall: set([(thirty_third_and_fifth, 3), (penn_station, 3), (herald_square, 1)]),
  penn_station: set([(manhattan_mall, 3), (thirty_fourth_and_seventh, 1)]),
  thirty_fourth_and_madison: set([(thirty_third_and_madison, 1), (empire_state_building, 3), (thirty_fifth_and_madison, 1)]),
  empire_state_building: set([(thirty_fourth_and_madison, 3), (herald_square, 3), (thirty_third_and_fifth, 1), (cuny_grad_center, 1)]),
  herald_square: set([(empire_state_building, 3), (thirty_fourth_and_seventh, 3), (manhattan_mall, 1), (thirty_fifth_and_sixth, 1)]),
  thirty_fourth_and_seventh: set([(herald_square, 3), (macys, 1), (penn_station, 1)]),
  thirty_fifth_and_madison: set([(thirty_fourth_and_madison, 1), (thirty_sixth_and_madison, 1), (cuny_grad_center, 3)]),
  cuny_grad_center: set([(thirty_fifth_and_madison, 3), (thirty_fifth_and_sixth, 3), (empire_state_building, 1), (thirty_sixth_and_fifth, 1)]),
  thirty_fifth_and_sixth: set([(cuny_grad_center, 3), (macys, 3), (herald_square, 1), (thirty_sixth_and_sixth, 1)]),
  macys: set([(thirty_fifth_and_sixth, 3), (thirty_fourth_and_seventh, 1), (thirty_sixth_and_seventh, 1)]),
  thirty_sixth_and_madison: set([(thirty_sixth_and_fifth, 3), (thirty_fifth_and_madison, 1), (morgan_library, 1)]),
  thirty_sixth_and_fifth: set([(thirty_sixth_and_madison, 3), (thirty_sixth_and_sixth, 3), (cuny_grad_center, 1), (thirty_seventh_and_fifth, 1)]),
  thirty_sixth_and_sixth: set([(thirty_sixth_and_fifth, 3), (thirty_sixth_and_seventh, 3), (thirty_fifth_and_sixth, 1), (thirty_seventh_and_sixth, 1)]),
  thirty_sixth_and_seventh: set([(thirty_sixth_and_sixth, 3), (macys, 1), (thirty_seventh_and_seventh, 1)]),
  morgan_library: set([(thirty_seventh_and_fifth, 3), (thirty_sixth_and_madison, 1), (thirty_eighth_and_madison, 1)]),
  thirty_seventh_and_fifth: set([(morgan_library, 3), (thirty_seventh_and_sixth, 3), (thirty_sixth_and_fifth, 1), (thirty_eighth_and_fifth, 1)]),
  thirty_seventh_and_sixth: set([(thirty_seventh_and_fifth, 3), (thirty_seventh_and_seventh, 3), (thirty_sixth_and_sixth, 1)]),
  thirty_seventh_and_seventh: set([(thirty_seventh_and_sixth, 3), (thirty_sixth_and_seventh, 1), (thirty_eighth_and_seventh, 1)]),
  thirty_eighth_and_madison: set([(thirty_eighth_and_fifth, 3), (morgan_library, 1), (mexican_consulate, 1)]),
  thirty_eighth_and_fifth: set([(thirty_eighth_and_madison, 3), (thirty_eighth_and_sixth, 3), (thirty_seventh_and_fifth, 1), (thirty_ninth_and_fifth, 1)]),
  thirty_eighth_and_sixth: set([(thirty_eighth_and_fifth, 3), (thirty_eighth_and_seventh, 3), (thirty_seventh_and_sixth, 1), (thirty_ninth_and_sixth, 1)]),
  thirty_eighth_and_seventh: set([(thirty_eighth_and_sixth, 3), (thirty_seventh_and_seventh, 1), (thirty_ninth_and_seventh, 1)]),
  mexican_consulate: set([(thirty_ninth_and_fifth, 3), (thirty_eighth_and_madison, 1), (fortieth_and_madison, 1)]),
  thirty_ninth_and_fifth: set([(mexican_consulate, 3), (thirty_ninth_and_sixth, 3), (thirty_eighth_and_fifth, 1), (fortieth_and_fifth, 1)]),
  thirty_ninth_and_sixth: set([(thirty_ninth_and_fifth, 3), (thirty_ninth_and_seventh, 3), (thirty_eighth_and_sixth, 1), (bryant_park_south, 1)]),
  thirty_ninth_and_seventh: set([(thirty_ninth_and_sixth, 3), (thirty_eighth_and_seventh, 1), (times_square_south, 1)]),
  fortieth_and_madison: set([(fortieth_and_fifth, 3), (mexican_consulate, 1), (forty_first_and_madison, 1)]),
  fortieth_and_fifth: set([(fortieth_and_madison, 3), (bryant_park_south, 3), (thirty_ninth_and_fifth, 1)]),
  bryant_park_south: set([(fortieth_and_fifth, 3), (times_square_south, 3), (thirty_ninth_and_sixth, 1), (kinokuniya, 1)]),
  times_square_south: set([(bryant_park_south, 3), (times_square, 1), (thirty_ninth_and_seventh, 1)]),
  forty_first_and_madison: set([(fortieth_and_madison, 1), (grand_central_station, 1), (mid_manhattan_library, 3)]),
  mid_manhattan_library: set([(forty_first_and_madison, 3), (library, 1), (fortieth_and_fifth, 1)]),
  kinokuniya: set([(times_square, 3), (bryant_park_north, 1), (bryant_park_south, 1)]),
  times_square: set([(kinokuniya, 3), (times_square_north, 1), (times_square_south, 1)]),
  grand_central_station: set([(library, 3), (forty_first_and_madison, 1)]),
  library: set([(mid_manhattan_library, 1), (grand_central_station, 3), (bryant_park_north, 3)]),
  bryant_park_north: set([(library, 3), (times_square_north, 3), (bryant_park_south, 1)]),
  times_square_north: set([(times_square, 1), (bryant_park_north, 3)])
}