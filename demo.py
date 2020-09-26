try:
    fh = open('question.txt', 'r')
    print(fh.read(10))

except Exception as e:
    print(e)
finally:
    fh.close()



