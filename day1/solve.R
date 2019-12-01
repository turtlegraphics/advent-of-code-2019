# Read the data
modules <- scan(file=file.choose())

# Part 1
print(sum(modules %/% 3 -2))

# Part 2
fuel <- function(x) { pmax(0, x %/% 3 - 2) }
v <- modules
total <- 0
while (any(v > 0)) {
  v <- fuel(v)
  total <- total + v
}
print(sum(total))
