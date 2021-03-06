library(ggplot2)
library(MASS)
library(plyr)
#Random Random Random
win_random_random_random = read.csv("sim_results_random_random_random_1000.csv", header = FALSE)
colnames(win_random_random_random) <- c("Name", "Points")
plot(win_random_random_random, main = "Random v Random v Random", xlab = "Players", ylab = "Points of the Winner", 
     sub = "1000 games were played")

ggplot(win_random_random_random, aes(Name)) + geom_bar()


win_action_buy = read.csv("sim_results_action_buy_random_1000.csv", header = FALSE)
colnames(win_action_buy) <- c("Name", "Points")
plot(win_action_buy, main = "Actions vs. Buys vs. Random", xlab = "Players", ylab = "Points of the Winner", 
     sub = "1000 games were played")

ggplot(win_action_buy, aes(Name)) + geom_bar()


#Actions, money, balance, random

win_all = read.csv("balance_action_buy_random_1000.csv", header = FALSE)
colnames(win_all) <- c("Name", "Points")
plot(win_all, main = "Balance v Action v Money v Random", xlab = "Players", ylab = "Points of the Winner", 
     sub = "1000 games were played")

ggplot(win_all, aes(Name)) + geom_bar()


#Festival vs. Market vs. Laboratory
#similar and can't tell what is better

fest_v_market = read.csv("festival_v_market.csv", header = FALSE)
colnames(fest_v_market) <- c("Name", "Points")
plot(fest_v_market, main = "Festival vs. Market", xlab = "Players", ylab = "Points of the Winner", 
     sub = "1000 games were played")

ggplot(fest_v_market, aes(Name)) + geom_bar()

#K-MEANS here

big_test = read.csv("bal_act_mon_fest.csv", header = FALSE)
colnames(big_test) <- c("Stategy", "Points", "Margin")
head(big_test)
#plot(big_test$Points, big_test$Margin)
ggplot(big_test, aes(Points, Margin, color = Stategy)) + geom_point() + ggtitle("Colored by actual strategy")

marginCluster <- kmeans(big_test[, 2:3], 4, nstart = 20)
marginCluster$withinss
marginCluster$betweenss

marginCluster$cluster <- as.factor(marginCluster$cluster)
ggplot(big_test, aes(Points, Margin, color = marginCluster$cluster)) + geom_point() +
  scale_fill_identity(name = 'Strategies', guide = 'legend',labels=c("Balance", "festival", "Max Actions", "Max Money")) +
  ggtitle("Coloring with K Means 4")


#Hypothesis Testings

#Question - Is festival significantly different than market
head(fest_v_market)
colnames(fest_v_market) <- c("Name", "Points")
festival_data = fest_v_market[fest_v_market$Name == "sim-festival-0", ]
market_data = fest_v_market[fest_v_market$Name == "sim-market-1", ]

summary(festival_data)
summary(market_data)

#the points clearly aren't statistically different, but number of wins looks like it might be
#we will look at win percentage

n = length(fest_v_market$Points)
prop_fest = length((festival_data$Points)) / n
prop_market = length((market_data$Points)) / n

prop.test(x = c(length((festival_data$Points)), length((market_data$Points))), n = c(n, n), correct = FALSE)

#counts = c()
#for (item in fest_v_market$Name) {
#  if (item == "sim-market-1") {
#    counts = c(counts, 1)
#  } else {
#    counts = c(counts, 0)
#  }
#}
#
#fest_v_market$counts = counts
#prop.test(table(fest_v_market$counts, fest_v_market$Name), correct = FALSE)



#now strategy differences
colnames(win_all) <- c("Name", "Points")
money_v_random = win_all[(win_all$Name == "sim-max_money-2" | win_all$Name == "sim-random-3"), ]

# counts = c()
# for (item in money_v_random$Name) {
#   if (item == "sim-max_money-2") {
#     counts = c(counts, 1)
#   } else {
#     counts = c(counts, 0)
#   }
# }
# money_v_random$counts = counts
# money_v_random$Name <- droplevels(money_v_random$Name)


money_data = money_v_random[money_v_random$Name == "sim-max_money-2", ]
rand_data = money_v_random[money_v_random$Name == "sim-random-3", ]

#the points clearly aren't statistically different, but number of wins looks like it might be
#we will look at win percentage

n = length(money_v_random$Points)
prop_money = length((money_data$Points)) / n
prop_rand = length((rand_data$Points)) / n


prop.test(x = c(length((money_data$Points)), length((rand_data$Points))), n = c(n, n), correct = FALSE)

