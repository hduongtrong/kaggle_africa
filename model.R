library(e1071)
library(fields)
library(rARPACK)
library(ggplot2)
library(scatterplot3d)

# Load Data
setwd("~/Documents/kaggle_africa/")
if (!exists("xtrain")) source("data_process.R");

Dst = 1-abs(cor(xtrain))
image.plot(Dst)
n = nrow(Dst)
H = diag(rep(1, n)) - matrix(1/n, n, n)

Dst = (-0.5)*H %*% Dst %*% H / (n/2)
rm(H); gc();
ei = eigs_sym(Dst, 5)
X = ei$vectors*sqrt(ei$values)
out = kmeans(X,centers = 4)

ggplot(data = NULL) + 
  geom_point(aes(x = X[,1], y = X[, 2], color = factor(out$cluster)), 
                                 alpha = 0.3)
getOption("bitmapType")

eigs_sym(cor(xtrain), 10)$values
