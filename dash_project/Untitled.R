library(xts)
library(tseries)
library(astsa)
comments = read.csv('/Users/janellashu/Desktop/reddit_comments.csv')
submission = read.csv('/Users/janellashu/Desktop/reddit_submissions.csv')

comments$datetime = as.POSIXct(comments$created_utc, origin = "1970-01-01", tz = "GMT")
comments$ind = 1
test = table(as.Date(comments$datetime, format='%m/%d/%Y'))
test1 = as.data.frame(test)
test1[order(test1$Freq, decreasing = TRUE), ]
head(test1[order(test1$Freq, decreasing = TRUE), ], 10)

submission$datetime = as.POSIXct(submission$created_utc, origin = "1970-01-01", tz = "GMT")
test2 = table(as.Date(submission$datetime, format='%m/%d/%Y'))
test3 = as.data.frame(test2)
test3[order(test3$Freq, decreasing = TRUE), ]


plot(NULL, xlim=c(as.Date("2010-01-01"),as.Date("2018-12-31")), ylim=c(0,30))
plot(test2, col = rgb(1,0,0,alpha=0.3), ylim = c(0, 80))
plot(test, col = rgb(0,0,1,alpha=0.3), ylim = c(0, 80))
legend("2015-06-11", 60, legend = c("submission", "comment"), col = c(rgb(1,0,0,alpha=0.3),  rgb(0,0,1,alpha=0.3)))

plot(NULL, xlim = c(0, 10), ylim=c(0,30))
legend(4, 15, legend = c("submission", "comment"), col=c(rgb(1,0,0,alpha=0.3), rgb(0,0,1,alpha=0.3)), lty = c(1,1), lwd = c(4,4))

###peaks
#comment
head(test1[order(test1$Freq, decreasing = TRUE), ], 20)
#submission
head(test3[order(test3$Freq, decreasing = TRUE), ], 20)
