library(e1071)
library(fields)
library(rARPACK)
library(ggplot2)
# Load Data
if (!exists("xtrain")) source("data_process.R");

Dst = 1-abs(cor(xtrain))
n = nrow(Dst)
H = diag(rep(1, n)) - matrix(1/n, n, n)

Dst = (-0.5)*H %*% Dst %*% H / (n/2)
rm(H); gc();
ei = eigs_sym(Dst, 5)
X = ei$vectors*sqrt(ei$values)

ggplot(data = NULL) + geom_point(aes(x = X[,1], y = X[, 2]), alpha = 0.5)
