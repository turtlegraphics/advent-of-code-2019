library(data.table)
library(readr)

# How many fft's to apply before the message (Part 2 requires 100)
rounds <- 100

instring <- read_file("/Users/bryan/Documents/Puzzles/Advent 2019/day16/input.txt")
input <- as.integer(head(unlist(strsplit(instring,split="")),n=-1))
print(input)
signal <- rep(input,10000)
offset <- as.integer(substr(instring,0,7))
print(offset)

fft <- function(signal) {
  N <- length(signal);
  sums <- c(0,cumsum(signal));
  result <- 0
  for (d in seq((N-1)%/%2,0,-1)) {
    lead <- seq(2*d+2,N+1,2*(d+1));
    trail <- seq(2*d+1,N,2*d+1);
    curlen <- length(trail)
    pad <- rep(N+1,curlen-length(lead));
    lead <- c(lead,pad);
    result <- c(result,rep(0,curlen-length(result)));
    result[1:curlen] <- result[1:curlen] + ((-1)^d*(sums[lead] - sums[trail]))
  }
  abs(result) %% 10;
}

totaltime <- system.time(0)
for (i in 1:rounds) {
  t <- system.time(signal <- fft(signal));
  totaltime <- totaltime + t
  print(i);
  print(totaltime);
}

print(signal[(offset+1):(offset+8)])
