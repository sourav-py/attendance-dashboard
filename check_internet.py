try:

    urlopen("https://www.google.com/")

except urllib2.URLError, e:

    print "Network down."