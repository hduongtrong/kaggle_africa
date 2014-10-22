
options(max.print = 1000)
getData = function(train.ratio = 0.7)
{
  # Note that name train test label may be confusing
  train = read.csv("training.csv")
  test  = read.csv("sorted_test.csv")
  # Shuffle the rows
  train = train[sample(nrow(train)),]
  test  = test[sample(nrow(test)), ]
  # Extract the y from data
  label = c("Ca","P","pH","SOC","Sand")
  y = as.matrix(train[label])
  # Data now only contain the x's
  for (i in 1:length(label))
  {  train[label[i]] = NULL}
  train["PIDN"]   = NULL
  test["PIDN"]    = NULL
  # Convert 2 levels data into binary
  train["Depth"] = (train["Depth"] == "Subsoil") + 0
  test["Depth"]  = (test["Depth"]  == "Subsoil") + 0
  # Split train data into train and test.
  n = nrow(train);
  p = round(train.ratio * n)
  xtrain <<- as.matrix(train[1:p,])
  xtest  <<- as.matrix(train[p:n,])
  ytrain <<- as.matrix(y[1:p,])
  ytest  <<- as.matrix(y[p:n,])
  xout   <<- as.matrix(test)
}
getData()


