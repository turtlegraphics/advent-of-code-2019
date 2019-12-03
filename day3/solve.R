library(dplyr)
input <- readLines(file.choose())
instructions <- strsplit(input,',')

wire <- function (inst) {
  # Convert a vector of instructions "R10" "U5" ..
  # to a data frame with x,y coordinates for each point on the wire
  distance <- as.integer(substr(inst,2,1000))
  dx <- recode(substr(inst,1,1), R = 1, L = -1, U = 0, D = 0)
  dy <- recode(substr(inst,1,1), R = 0, L =  0, U = 1, D = -1)
  x <- cumsum(rep(dx,distance))
  y <- cumsum(rep(dy,distance))
  data.frame(x,y) %>% mutate(step = row_number())
}

wire1 <- wire(unlist(instructions[1]))
wire2 <- wire(unlist(instructions[2]))

intersections <- inner_join(wire1,wire2,by=c("x","y")) %>%
  mutate(dist = abs(x)+abs(y), steps = step.x + step.y)

# part 1
print(min(intersections$dist))
# part 2
print(min(intersections$steps))