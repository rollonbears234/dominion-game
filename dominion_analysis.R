win_random_random_random = read.csv("sim_results_random_random_random_1000.csv", header = FALSE)

plot(win_random_random_random, main = "Random v Random v Random", xlab = "Players", ylab = "Points of the Winner", 
     sub = "1000 games were played")
